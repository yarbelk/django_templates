{{ project_name|title }} Django Project
=======================================

Requirements
------------

* python >= 2.5
* pip
* django >= 1.4

Installation
------------

Virtualenvwrapper
~~~~~~~~~~~~~~~~~

..code::bash:
    mkvirtualenv {{project_name}}-env
    cd $VIRTUAL_ENV
    mkdir {db,tmp}
    mkdir tmp/email

get the code

..code::bash:
    git clone <GIT_URL> {{ project_name }}

Install the Requirements
..code::bash:
    cd {{ project_name }}
    pip install -r requirements.txt

update the activate script to set the correct Django settings module and
PYTHONPATH

..code::bash:
    # $VIRTUAL_ENV/bin/activate
    ...
    export DJANGO_SETINGS_MODULE="{{ project_name }}.config.settings.devel"

Sync DB
~~~~~~~

..code::bash:
    ./manage.py syncdb
    ./manage.py migrate --all
