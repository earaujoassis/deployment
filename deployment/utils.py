# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import shlex


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


def call(c, shell=True):
    subprocess.call(c, shell=shell)


def run(c):
    process = subprocess.Popen(shlex.split(c), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout, stderr = process.communicate()
    retcode = process.poll()
    return {"retcode": retcode, "stdout": stdout, "stderr": stderr}


def assert_step(r):
    if r is not 0:
        sys.stdout.write('> Something went wrong, aborting...\n')
        sys.exit(1)


def get_deployment_filepath_or_die():
    deployment_options_filepath = os.path.join(os.getcwd(), '.deployment.json')
    if not os.path.isfile(deployment_options_filepath):
        sys.stdout.write('> Missing deployment file; skipping\n')
        sys.exit(1)
    return deployment_options_filepath
