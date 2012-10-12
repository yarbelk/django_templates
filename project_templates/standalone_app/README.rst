==============================================================================
 {{ project_name|title }} Django App
==============================================================================

Requirements
------------

* python >= 2.5
* pip
* django >= 1.4

Installation
------------

Virtualenvwrapper
~~~~~~~~~~~~~~~~~

.. code:: bash

    mkvirtualenv {{project_name}}-env
    cd $VIRTUAL_ENV
    mkdir {db,tmp}
    mkdir tmp/email

get the code

.. code:: bash

    git clone <GIT_URL> {{ project_name }}

Install the Requirements

.. code:: bash

    cd {{ project_name }}
    pip install -r requirements.txt

Running the tests

.. code:: bash
