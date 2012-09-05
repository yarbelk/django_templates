Django Templates
================

Templates for Django 1.4.1 projects and (eventually) apps.  These are layouts
that I prefer to the vanilla django project layout.

Requirements
------------

* python >= 2.5
* pip
* django >= 1.4
* virtualenvwrapper

Installation
------------

Get the code
~~~~~~~~~~~~

.. code:: bash:

    git clone https://github.com/yarbelk/django_templates.git


Create a virtual env for the new project.

.. code:: bash

    mkvirtualenv {{project_name}}-env
    cd $VIRTUAL_ENV

create the projects

.. code:: bash

    django-admin.py startproject --template=/path/to/project/template/ <project_name>
    mkdir {db,tmp}
    mkdir tmp/email
