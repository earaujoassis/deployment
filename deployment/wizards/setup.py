# -*- coding: utf-8 -*-

import os
import sys


def setup():
    print("> All right, let's setup the current project for deployment")
    if not os.path.isfile(os.path.join(os.getcwd(), '.deployment.json')):
        print("Hmm... you haven't setup the currect project; please run `ploy init`; skipping")
        sys.exit(1)

    upstream = ""
    while len(upstream) == 0:
        upstream = input("Which is the upstream URL: ").strip()

    return {
        "upstream": upstream,
    }
