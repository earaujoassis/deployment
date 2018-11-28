# -*- coding: utf-8 -*-

import os
import sys
from mako.template import Template

from deployment.errors import MissingData, MissingDeploymentType
from deployment.utils import DEPLOYMENT_TYPE_STATIC
from deployment.utils import DEPLOYMENT_TYPE_CONTAINERS
from deployment.utils import DEPLOYMENT_TYPE_COMPOSE


def generate_deployment_descriptor(deployment_type=DEPLOYMENT_TYPE_STATIC, template_data=None):
    current_project_path = os.path.dirname(__file__)
    template_filename = None
    if template_data is None:
        raise MissingData('Missing template data')
    if deployment_type is DEPLOYMENT_TYPE_STATIC:
        template_filename = "deployment.static.json"
    elif deployment_type is DEPLOYMENT_TYPE_CONTAINERS:
        template_filename = "deployment.containers.json"
    elif deployment_type is DEPLOYMENT_TYPE_COMPOSE:
        template_filename = "deployment.compose.json"
    else:
        raise MissingDeploymentType('Missing deployment type')
    template_filepath = os.path.join(current_project_path, 'templates', template_filename)
    template = Template(filename=template_filepath)
    return template.render(**template_data)
