=============================
openhub-django
=============================

.. image:: https://badge.fury.io/py/openhub-django.svg
    :target: https://badge.fury.io/py/openhub-django

.. image:: https://travis-ci.org/sks444/openhub-django.svg?branch=master
    :target: https://travis-ci.org/sks444/openhub-django

.. image:: https://codecov.io/gh/sks444/openhub-django/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/sks444/openhub-django

Integrate openhub APIs with Django

Documentation
-------------

The full documentation is at https://openhub-django.readthedocs.io.

Quickstart
----------

I. **Install openhub-django:**

.. code-block:: bash

   pip install openhub-django


II. Add it to your :code:`INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'openhub_django.apps.OpenhubDjangoConfig',
        ...
    )


III. **Add openhub-django's URL patterns:**

.. code-block:: python


    urlpatterns = [
        ...
        url(r'^', include('openhub_django.urls')),
        ...
    ]

IV. **Configure following environment variables:**

    * **OpenHub Token**

      How to get OpenHub Token?

      1. Signup with GitHub on OpenHub_
      2. Go to your profile settings to create a new API Key.
      3. Choose "API Keys" from the section and create a new one by clicking on button "Request New API Key"
      4. Fill in the required fields and Save it.
      5. Copy the :code:`API Key` for the generated token to add it to your environment.

      Add it to your Linux (or Ubuntu) environment-

      1. Open the terminal and run `cat ~/.bashrc`.
      2. Find this peice of code

      .. code-block:: bash

        if [ -f ~/.bash_aliases ]; then
             . ~/.bash_aliases
        fi

      3. In this case we will create a new file in :code:`$HOME` directory named
         :code:`.bash_aliases` to store our environment variables. As it will execute
         everytime we open a new terminal window.

      .. code-block:: bash

        vi ~/.bash_aliases

      4. Enter into the insert mode and add the value of token that you generated from OpenHub settings.

      .. code-block:: bash

        export OH_TOKEN=<PASTE THE COPIED API KEY OF TOKEN>

      5. Exit the insert mode by pressing :code:`esc` key and the editor.
      6. Restart your terminal and run :code:`printenv` to verify the API Key added.


    * **Organization name**

      Set the environment variable :code:`ORG_NAME` following the above mentioned steps like you
      did adding the environment variable :code:`OH_TOKEN`. Once you setup these two environment
      variables, you're ready to run a management command to fetch the organization related
      information from OpenHub.

V. **Run management command**

.. code-block:: bash

  python manage.py migrate

  python manage.py import_openhub_data

VI. **View the fetched data:**

.. code-block:: bash

  python manage.py runserver

  # Open http://127.0.0.1:8000/openhub/ in browser

Features
--------

* Import all the organization *portfolio projects* data
* Import all the organization *outside projects* data such as dependencies
* Import all the *affiliated committers* data who made contributions to the projects
* Import all the *outside committers* data
* Import the *organization* related information
* Generate the static web-pages of all the imported data with an interactive UI/UX design.


Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
.. _OpenHub: https://www.openhub.net/accounts/new
