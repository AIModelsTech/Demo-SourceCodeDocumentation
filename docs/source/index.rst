Welcome to Sphinx Documentation Demo!
=====================================================

.. toctree::
   :hidden:

   getting-started
   development
   documentation
   reference/index

.. toctree::
   :caption: Useful links
   :hidden:

   github <https://github.com/AIModelsTech/Demo-SourceCodeDocumentation>

.. module:: area

``area`` is a demo module to showcase the use of Sphinx documentation.

A quick example of using this module
-------------------------------------

.. code-block:: python

   import lib.area as area

   side = 5
   print(f"Area of square with side length of {side} is {area.square(side)}.")

The output of the above code would look something like this:

.. code-block:: python

   Area of square with side length of 5 is 25.
