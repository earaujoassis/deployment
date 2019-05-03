# -*- coding: utf-8 -*-

import sys
import json


def load_deployment_file(deployment_options_filepath):
    options = None

    with open(deployment_options_filepath) as deployment_options_file:
        try:
            deployment_options = json.load(deployment_options_file)
        except Exception as e:
            sys.stdout.write('> Problem reading the deployment file; skipping\n')
            sys.stdout.write('> Revision not deployed\n')
            sys.exit(1)
        project_name = deployment_options.get('project')
        exposed_port = deployment_options.get('exposed_port', 8080)
        baseport = deployment_options.get('baseport', 3000)
        number_of_instances = deployment_options.get('number_of_instances', 1)
        number_of_instances = number_of_instances if number_of_instances > 0 else 1
        env = deployment_options.get('env', dict())
        options = {
            "project_name": project_name,
            "number_of_instances": number_of_instances,
            "exposed_port": exposed_port,
            "baseport": baseport,
            "env": env
        }

    return options
