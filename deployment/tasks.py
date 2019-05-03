# -*- coding: utf-8 -*-

import os
import sys

from giturlparse import parse

from deployment.wizards import init_wizard, setup_wizard
from deployment.functions import generate_deployment_descriptor
from deployment.loaders import load_deployment_file
from deployment.executor import receiver
from deployment.utils import run, get_deployment_filepath_or_die


def init():
    data = init_wizard()
    deployment_type = data.pop('deployment_type')
    with open('.deployment.json', 'w') as destination:
        template = generate_deployment_descriptor(
            deployment_type=deployment_type,
            template_data=data)
        destination.write(template)


def setup():
    current_project_path = os.path.dirname(__file__)
    template_filepath = os.path.join(current_project_path, 'templates', 'post-receive')
    deployment_options_filepath = get_deployment_filepath_or_die()
    options = load_deployment_file(deployment_options_filepath)
    data = setup_wizard()
    upstream = data.pop('upstream')
    project_name = options.get('project_name')
    run("ssh -t {0} 'mkdir -p ploys/{1}.git && cd ploys/{1}.git && git init --bare'".format(upstream, project_name))
    run("ssh -t {0} 'mkdir -p ploys/{1}.deployment'".format(upstream, project_name))
    run("scp {2} {0}:ploys/{1}.git/hooks".format(upstream, project_name, template_filepath))
    run("ssh -t {0} 'chmod +x ploys/{1}.git/hooks/post-receive'".format(upstream, project_name))
    run('git remote add deployment {0}:ploys/{1}.git'.format(upstream, project_name))
    print("> Alright! The upstream is configured; you may check through `git remote -v`")


def push():
    run('git push deployment master')


def drop(filepath):
    result = run("git config --get remote.deployment.url")
    upstream = result.stdout.decode("utf-8").strip().replace(".git", ".deployment")
    fullpath = os.path.join(os.getcwd(), filepath)
    run("scp {0} {1}".format(fullpath, upstream))


def receive(project, oldrev, newrev):
    sys.stdout.write("Revision {0} received. Deploying master branch to production...\n".format(newrev))
    call("git --work-tree=$HOME/ploys/{0}.deployment --git-dir=$HOME/ploys/{0}.git checkout -f".format(project))
    os.chdir("$HOME/ploys/{0}.deployment".format(project))
    deployment_options_filepath = get_deployment_filepath_or_die()
    options = load_deployment_file(deployment_options_filepath)
    return receiver(project, oldrev, newrev, options)
