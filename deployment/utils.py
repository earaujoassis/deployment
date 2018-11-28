# -*- coding: utf-8 -*-

import os
import sys


DEPLOYMENT_TYPE_STATIC     = 0
DEPLOYMENT_TYPE_CONTAINERS = 1
DEPLOYMENT_TYPE_COMPOSE    = 2


class ConsoleColors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_error(message):
    sys.stderr.write(ConsoleColors.FAIL + message + ConsoleColors.END + '\n')


def print_success(message):
    sys.stdout.write(ConsoleColors.GREEN + message + ConsoleColors.END + '\n')


def print_step(message):
    sys.stdout.write(ConsoleColors.BOLD + message + ConsoleColors.END + '\n')
