#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from deployment.cli import DeploymentCLI


name = "deployment"
version = "0.1.0"


def main():
    code = DeploymentCLI.apply(sys.argv)
    sys.exit(code)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as e:
        sys.exit(0)
