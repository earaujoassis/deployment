# -*- coding: utf-8 -*-

import argparse
import sys
import os
import re

try:
    import tasks
    import utils
except ImportError as e:
    from deployment import tasks,  utils


parser = argparse.ArgumentParser(description='Deployment CLI tool and manager')
subparsers = parser.add_subparsers(dest='parent')
init_command = subparsers.add_parser(
    'init',
    help='create initial configuration files')
init_command.add_argument(
    '--force',
    action='store_true',
    default=False,
    help='forcefully overrides configuration files', dest='argument')
setup_command = subparsers.add_parser(
    'setup',
    help='create configuration files in the remote upstream and add it to the current project')
push_command = subparsers.add_parser(
    'push',
    help='push the current project\'s branch and its commit history to the remote upstream')
drop_command = subparsers.add_parser(
    'drop',
    help='drop a git-ignored file to the remote upstream project folder (ideally config files)')
drop_command.add_argument('filepath', action='store', help='the path to the file (folder not supported)')
receive_command = subparsers.add_parser(
    'receive',
    help='receive a new revision and deploy it; used in git remote')
receive_command.add_argument('project_folder', action='store', help='the project folder basename (<project>.git)')
receive_command.add_argument('oldrev', action='store', help='old revision hash')
receive_command.add_argument('newrev', action='store', help='new revision hash')


class DeploymentCLI(object):
    def __init__(self, namespace=None):
        self.namespace = namespace

    def get_module_attribute_safely(self, reference, module):
        namespace = self.namespace
        if hasattr(namespace, reference):
            attr = getattr(namespace, reference)
            attrname = attr.replace('-', '_')
            if hasattr(module, attrname):
                return getattr(module, attrname)
        return None

    def get_task_arguments(self):
        args = vars(self.namespace)
        args.pop('parent')
        return args

    def action(self):
        task_function = self.get_module_attribute_safely('parent', tasks)
        if task_function is None:
            utils.print_error('# Command is not implemented yet')
            return
        args = self.get_task_arguments()
        return task_function(**args)

    @staticmethod
    def apply(argv):
        namespace = parser.parse_args(argv[1:])
        return DeploymentCLI(namespace).action()
