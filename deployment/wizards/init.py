# -*- coding: utf-8 -*-

import os
import sys

from deployment.utils import DEPLOYMENT_TYPE_STATIC
from deployment.utils import DEPLOYMENT_TYPE_CONTAINERS
from deployment.utils import DEPLOYMENT_TYPE_COMPOSE


def init():
    print("> All right, let's setup the current project for deployment")
    if not os.path.isdir(os.path.join(os.getcwd(), '.git')):
        print("Hmm... you're not running in a git-project; skipping")
        sys.exit(1)

    print("> Select the deployment type:")
    print("[{0}] Using a static generate website;".format(DEPLOYMENT_TYPE_STATIC))
    print("[{0}] Using a Dockerfile to build an image and create containers; or".format(DEPLOYMENT_TYPE_CONTAINERS))
    print("[{0}] Using a docker-compose.yml setup".format(DEPLOYMENT_TYPE_COMPOSE))
    deployment_type = None
    options = (DEPLOYMENT_TYPE_STATIC, DEPLOYMENT_TYPE_CONTAINERS, DEPLOYMENT_TYPE_COMPOSE)
    while deployment_type not in options:
        try:
            deployment_type = input('Which one (default: 0): ')
            if deployment_type.strip() == "":
                deployment_type = DEPLOYMENT_TYPE_STATIC
            else:
                deployment_type = int(deployment_type.strip())
        except ValueError as e:
            print("> It must be a valid option")
    print("> Ok, it will be option {0}".format(deployment_type))

    if deployment_type is DEPLOYMENT_TYPE_STATIC:
        origin_folder = ""
        while len(origin_folder) == 0:
            origin_folder = input("Which is the origin folder for the static assets: ").strip()

        destination_folder = ""
        while len(destination_folder) == 0:
            destination_folder = input("Which is the destination folder in the remote upstream: ").strip()

        command = ""
        while len(command) == 0:
            command = input("Finally, which command to generate the the static assets: ").strip()

        print("> Alright! All details obtained. You may check the `.deployment.json` file")

        return {
            "deployment_type": deployment_type,
            "origin_folder": origin_folder,
            "destination_folder": destination_folder,
            "command": command
        }

    if deployment_type is DEPLOYMENT_TYPE_CONTAINERS:
        number_of_instances = None
        while number_of_instances is None:
            try:
                number_of_instances = int(input("What is the number of containers instances to deploy: ").strip())
            except ValueError as e:
                print("> It must be an integer")

        exposed_port = None
        while exposed_port is None:
            try:
                exposed_port = int(input("What is the exposed port (internal) for the containers: ").strip())
            except ValueError as e:
                print("> It must be an integer")

        baseport = None
        while baseport is None:
            try:
                baseport = int(input("What is the baseport (external) for the containers: ").strip())
            except ValueError as e:
                print("> It must be an integer")

        print("> Alright! If there's any environment variable to plug, you may edit the `.deployment.json` file")

        return {
            "deployment_type": deployment_type,
            "number_of_instances": number_of_instances,
            "exposed_port": exposed_port,
            "baseport": baseport,
        }

    if deployment_type is DEPLOYMENT_TYPE_COMPOSE:
        composer_path = input("What is the docker-compose.yml path (default: docker-compose.yml): ").strip()
        if composer_path == "":
            composer_path = "docker-compose.yml"

        print("> Alright! All details obtained. You may check the `.deployment.json` file")

        return {
            "deployment_type": deployment_type,
            "composer_path": composer_path,
        }
