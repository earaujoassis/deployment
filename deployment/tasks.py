# -*- coding: utf-8 -*-

import os

from deployment.wizards import init_wizard, setup_wizard
from deployment.functions import generate_deployment_descriptor


def init():
    data = init_wizard()
    deployment_type = data.pop('deployment_type')
    with open('.deployment.json', 'w') as destination:
        template = generate_deployment_descriptor(
            deployment_type=deployment_type,
            template_data=data)
        destination.write(template)


def setup():
    data = setup_wizard()
    os.system('git remote add deployment {0}'.format(data.pop('upstream')))
    print("> Alright! The upstream is configured; you may check through `git remote -v`")


def push():
    pass
