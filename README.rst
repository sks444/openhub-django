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

Install openhub-django::

    pip install openhub-django

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'openhub_django.apps.OpenhubDjangoConfig',
        ...
    )

Add openhub-django's URL patterns:

.. code-block:: python

    from openhub_django import urls as openhub_django_urls


    urlpatterns = [
        ...
        url(r'^', include(openhub_django_urls)),
        ...
    ]

Features
--------

* TODO

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
