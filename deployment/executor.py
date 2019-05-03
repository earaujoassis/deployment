# Version: 1.2
# -*- coding: utf-8 -*-

import sys
import os
import json

from deployment.utils import call, assert_step


def receiver(project, oldrev, newrev, options={}):
    if not oldrev or not newrev:
        sys.stdout.write('> Missing revision code; skipping\n')
        sys.stdout.write('> Revision not deployed\n')
        sys.exit(1)

    for key, value in options["env"].items():
        os.environ[key] = value
    docker = 'sudo docker'
    old_image_label = '{0}-{1}'.format(project, oldrev)
    new_image_label = '{0}-{1}'.format(project, newrev)
    exposed_port = options.get("exposed_port")
    baseport = options.get("baseport")
    number_of_instances = options.get("number_of_instances")
    env = options.get("env")

    sys.stdout.write('> Starting to deploy revision {0}\n'.format(newrev))

    # Build image
    sys.stdout.write('> Starting to build image {}\n'.format(new_image_label))
    command = '{0} build -t {1} .'.format(docker, new_image_label)
    print('> ' + command)
    sys.stdout.flush()
    r = call(command)
    assert_step(r)

    # Replace each container/port
    sys.stdout.write('> Replacing containers\n')
    for i in list(range(number_of_instances)):
        port = baseport + i
        new_container_label = '{0}-p{1}'.format(new_image_label, port)
        old_container_label = '{0}-p{1}'.format(old_image_label, port)
        sys.stdout.write('> Replacing container {0} for {1}\n'.format(
            old_container_label, new_container_label))

        ##
        # The following command may fail
        command = '{0} stop {1}'.format(docker, old_container_label)
        print('> ' + command)
        sys.stdout.flush()
        r = call(command)

        ##
        # The following command may fail
        command = '{0} rm {1}'.format(docker, old_container_label)
        print('> ' + command)
        sys.stdout.flush()
        r = call(command)
        command = '{0} run --restart=always --name {1} -p {2}:{3} -d {4}'.format(
            docker, new_container_label, port, exposed_port, new_image_label)
        print('> ' + command)
        sys.stdout.flush()
        r = call(command)
        assert_step(r)

    ##
    # The following command may fail
    # Remove old image
    sys.stdout.write('> Remove previous image {0}\n'.format(old_image_label))
    command = '{0} rmi {1}'.format(docker, old_image_label)
    print('> ' + command)
    sys.stdout.flush()
    r = call(command)

    sys.stdout.write('> Revision {0} deployed successfully\n'.format(newrev))
