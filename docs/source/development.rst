Development Setup
=================

This guide will help you set up your development environment with the necessary tools for contributing to the project.

Prerequisites
-------------

- Python 3.6 or higher
- pip (Python package installer)
- git

Installation
------------

1. **Clone the repository:**

   Open your terminal and run the following command:

   .. code-block:: bash

      git clone git@github.com:AIModelsTech/Demo-SourceCodeDocumentation.git
      cd Demo-SourceCodeDocumentation

2. **Create a virtual environment:**

   It's recommended to use a virtual environment to manage dependencies. Run the following commands:

   .. code-block:: bash

      python3 -m venv venv
      source venv/bin/activate

3. **Install the required packages:**

   Install the dependencies listed in the `requirements.txt` file:

   .. code-block:: bash

      pip install -r requirements.txt

4. **Install pre-commit hooks:**

   This project uses `pre-commit` to manage git hooks. Install the hooks by running:

   .. code-block:: bash

      pre-commit install

   You can manually run the pre-commit hooks on all files with:

   .. code-block:: bash

      pre-commit run --all-files

Development Workflow
--------------------

1. **Create a new branch:**

   Create a new branch for your feature or bugfix:

   .. code-block:: bash

      git checkout -b your-feature-name

2. **Make your changes:**

   Make your changes and commit them with a meaningful commit message:

   .. code-block:: bash

      git add .
      git commit -m "Add your commit message here"

3. **Push your changes:**

   Push your changes to the repository:

   .. code-block:: bash

      git push origin your-feature-name

4. **Create a pull request:**

   Open a pull request on GitHub and describe your changes.

License
-------

This project is licensed under the MIT License. See the `LICENSE` file for more details.
