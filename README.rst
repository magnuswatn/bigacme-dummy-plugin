bigacme-dummy-plugin
====================

Dummy plugin for `bigacme <https://github.com/magnuswatn/bigacme>`_ for testing purposes. It just prints out the DNS record that you should add.

Installation
------------

To download and install:

.. code-block:: bash

    $ pip install git+https://github.com/magnuswatn/bigacme-dummy-plugin.git

After installation the following must be added to the bigacme configuration file:

.. code-block:: ini

    [Plugin]
    sleeptime = 12

(sleeptime can of course be adjusted as needed)

