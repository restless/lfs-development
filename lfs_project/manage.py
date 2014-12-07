#!/usr/bin/env python
import glob
import os
import sys

BASE_DIR = dirname(dirname(__file__))

if __name__ == "__main__":
    # Let's use some env variables
    # just put a file named after variable name you want to set into envdir directory
    # and fill it with variable value.
    # More:
    # http://bruno.im/2013/may/18/django-stop-writing-settings-files/
    # http://envdir.readthedocs.org/en/latest/usage.html
    if 'test' in sys.argv:
        env_dir = os.path.join(BASE_DIR, 'tests', 'envdir')
    else:
        env_dir = os.path.join(BASE_DIR, 'envdir')

    env_vars = glob.glob(os.path.join(env_dir, '*'))
    for env_var in env_vars:
        with open(env_var, 'r') as env_var_file:
            os.environ.setdefault(env_var.split(os.sep)[-1],
                                  env_var_file.read().strip())


    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config")
    os.environ.setdefault("DJANGO_CONFIGURATION", "Local")

    from configurations.management import execute_from_command_line

    execute_from_command_line(sys.argv)