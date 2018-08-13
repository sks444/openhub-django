=====
Usage
=====

To use openhub-django in a project, add it to your `INSTALLED_APPS`:

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
