# -*- coding: utf-8 -*-

from deployment.wizards import init_wizard
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
    pass


def push():
    pass
