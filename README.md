Automation Testing with Python, Tox and Github Actions

📌 Project Description
---

This project is an automation setup built with Python, tox, pytest, and GitHub Actions. The goal was to create a reliable continuous integration (CI) workflow that automatically runs tests in different environments, ensuring consistent quality and maintainability of the codebase.

🛠️ Tools Used
---

Python – core programming language for building and running the tests

tox – to automate testing across multiple Python environments

pytest – framework for writing and executing unit tests

GitHub Actions – for continuous integration and automated testing

📋 Prerequisites
---

Before running the project locally, ensure you have the following installed:

- Python 3.10+

- pip (Python package manager)

- tox

- pytest

Clone the repository and install dependencies:

````
git clone https://github.com/Olympiah/AutomatedTest.git
cd AutomatedTest
pip install -r requirements.txt
````
On the command-line use the following to affirm tests are working
````
mypy src
pytest

````

▶️ Usage / How It Works
---
1. Local Testing with tox

tox creates isolated environments for testing.

It installs the required dependencies and runs pytest automatically.

To run locally:
````
tox
````

Test results will be shown in the console for each environment configured in tox.ini.

2. Automated CI with GitHub Actions

On every push or pull request to the repository, GitHub Actions triggers the CI workflow.

The workflow runs the following steps:

- Sets up the specified Python version(s)

- Installs dependencies

- Runs tox to execute all tests

If all tests pass, the workflow succeeds ✅

If any test fails, the workflow fails ❌ and reports the error in the GitHub Actions log

This ensures that every change is tested automatically before being merged, preventing broken code from entering the main branch.

Lessons Learned from Debugging😅
---

While setting up the CI workflow, I encountered a recurring issue with the GitHub Actions YAML configuration:

*Problem*: The workflow was failing because the Python version 3.10 kept being read as 3.1 instead of 3.10

*Impact*: This caused the workflow to consistently break, as GitHub Actions tried to fetch a non-existent Python version.

*Solution*: Updating the YAML file to explicitly use 3.10 fixed the issue.

