Documentation
=============

This guide will help you maintain and build the project documentation.

Prerequisites
-------------

- Python 3.6 or higher
- pip (Python package installer)

Installation
------------

1. **Create a virtual environment:**

   It's recommended to use a virtual environment to manage dependencies. Run the following commands:

   .. code-block:: bash

      python3 -m venv venv
      source venv/bin/activate

2. **Install the required packages:**

   If you haven't already, install the dependencies required for building the documentation:

   .. code-block:: bash

      python3 -m pip install requirements.txt

Building the Documentation
--------------------------

1. **Navigate to the `docs` directory:**

   .. code-block:: bash

      cd docs

2. **Build the HTML documentation:**

   Run the following command to build the HTML version of the documentation:

   .. code-block:: bash

      make html

   The generated documentation will be in the `_build/html` directory.

3. **Build the PDF documentation:**

   To build the PDF version of the documentation, run:

   .. code-block:: bash

      docker run -i -v $(pwd)/..:/app sphinxdoc/sphinx-latexpdf /bin/bash -c "
        cd /app &&
        python3 -m pip install -r requirements.txt &&
        cd /app/docs &&
        make latexpdf
      "

   The generated PDF will be in the `_build/latex` directory.

Maintaining the Documentation
-----------------------------

1. **Update the documentation source files:**

   The source files for the documentation are located in the `docs/source` directory. Update these files as needed.

2. **Add new pages:**

   To add a new page, create a new `.rst` file in the `docs/source` directory and update the `index.rst` file to include a reference to the new page.

3. **Rebuild the documentation:**

   After making changes to the documentation source files, rebuild the documentation to see the updates:

   .. code-block:: bash

      make html

4. **Check for broken links:**

   You can check for broken links in the documentation by running:

   .. code-block:: bash

      make linkcheck

GitHub Actions Workflow
-----------------------

The project includes a GitHub Actions workflow that automatically builds and deploys the documentation to GitHub Pages.

The page is accessible at: `demo-docs.aimodels.ca <https://demo-docs.aimodels.ca>`_

The workflow is defined in the `.github/workflows/docs.yaml` file.

To trigger the workflow manually, navigate to the "Actions" tab in the GitHub repository and select the "Build and Deploy Documentation" workflow.

For more information on GitHub Actions, refer to the `GitHub Actions documentation <https://docs.github.com/en/actions>`_.
