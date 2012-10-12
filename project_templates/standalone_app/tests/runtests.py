#!/usr/bin/env python
import os
import sys

from argparse import ArgumentParser
from path import path

from django.conf import settings
from django.core.management import call_command

def run_tests():
    """
    Setup the environment to run the tests as stand alone
    uses sqlite3 in memory db
    """
    argument_parser = ArgumentParser(description="Run all tests for {{project name}}")
    #TODO add some configuration here

    settings.configure(**{
        "DATABASE_ENGINE"   : "django.db.backends.sqlite3",
        "DATABASE_NAME"     : "sqlite://:memory:",
        "ROOT_URLCONF"      : "tests.urls",
        "TEMPLATE_LOADERS"  : (
            "django.template.loaders.filesystem.load_template_source",
            "django.template.loaders.app_directory.load_template_source",
            ),
        "TEMPLATE_DIRS"     : (
            path(__file__).dirname() / 'templates',
            ),
        "INSTALLED_APPS"    : (
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.sites',
            '{{ project_name }},
            ),
        })
    call_command("test")

if __name__ == "__main__":
    return run_tests()

