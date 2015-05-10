#!/usr/bin/env python
import dotenv
import environ
import os
import sys
from os.path import dirname

# Let's use some env variables from .env file
BASE_DIR = dirname(__file__)
ROOT_DIR = environ.Path(dirname(__file__))
dotenv.load_dotenv(str(ROOT_DIR.path('.env')))

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)