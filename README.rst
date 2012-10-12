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


Using the Code
--------------

Create a virtual env for the new project.

.. code:: bash

    mkvirtualenv {{project_name}}-env
    cd $VIRTUAL_ENV

create the projects

Project default
~~~~~~~~~~~~~~~~

.. code:: bash

    django-admin.py startproject --template=/path/to/default/template/ <project_name> -e py,rst
    mkdir {db,tmp}
    mkdir tmp/email
    cd project_name
    pip install -r requirements.txt

then edit the README.rst

App Standalone_app
~~~~~~~~~~~~~~~~~~

.. code:: bash

    django-admin.py startproject --template=/path/to/standanle_app/template/ <project_name> -e py,rst
    cd project_name
    pip install -r requirements.txt

Don't forget to edit the `setup.py` file and README.rst
