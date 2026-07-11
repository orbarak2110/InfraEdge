<div align="center">

# InfraEdge

## Wikipedia UI & API Test Automation Framework

Automation testing project built with **Python**, **Pytest**, **Playwright** and **Requests**.

The project validates Wikipedia content through both the browser UI and the Wikipedia API.

</div>

---

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies](#technologies)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Clone the Repository](#clone-the-repository)
- [Create a Virtual Environment](#create-a-virtual-environment)
- [Install Dependencies](#install-dependencies)
- [Install Playwright Browsers](#install-playwright-browsers)
- [Run the Tests](#run-the-tests)
- [Test Logging](#test-logging)
- [Pytest Configuration](#pytest-configuration)
- [Architecture](#architecture)
- [Troubleshooting](#troubleshooting)
- [Git Ignore](#git-ignore)
- [Author](#author)

---

# Project Overview

This project is an automation testing framework that validates a specific section from Wikipedia.

The framework retrieves the same Wikipedia content through two different sources:

1. The Wikipedia website using Playwright.
2. The Wikipedia API using HTTP requests.

The project then:

- Extracts the section title.
- Extracts the section content.
- Counts the words in the content.
- Validates that the results are not empty.
- Compares the normalized UI and API word counts.
- Creates a separate log file for every test file.

---

# Technologies

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pytest | Test framework and fixtures |
| Playwright | Browser automation |
| Requests | HTTP API requests |
| Page Object Model | UI architecture |
| API Object Model | API architecture |
| Logging | Test execution logs |
| Git | Version control |

---

# Repository

SSH:

```bash
git@github.com:orbarak2110/InfraEdge.git
```

HTTPS:

```text
https://github.com/orbarak2110/InfraEdge
```

---

# Project Structure

```text
InfraEdge/
├── config/
│   ├── __init__.py
│   └── settings.py
│
├── infra_edge_flow/
│   ├── __init__.py
│   ├── infra_edge_flow.py
│   │
│   ├── api_flow/
│   │   ├── __init__.py
│   │   ├── base_api.py
│   │   └── wikipedia_api.py
│   │
│   └── ui_flow/
│       ├── __init__.py
│       └── ui_flow.py
│
├── pages/
│   ├── __init__.py
│   └── wikipedia_page.py
│
├── tests/
│   ├── __init__.py
│   ├── test_wikipedia_api.py
│   ├── test_wikipedia_ui.py
│   └── test_wikipedia_ui_and_api_word_counts.py
│
├── utils/
│   ├── __init__.py
│   └── text_utils.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Prerequisites

Before installing the project, make sure the following tools are installed:

- Python 3.10 or newer
- Git
- pip

Check the Python version:

```bash
python3 --version
```

Check Git:

```bash
git --version
```

Check pip:

```bash
python3 -m pip --version
```

---

# Clone the Repository

## Clone with SSH

```bash
git clone git@github.com:orbarak2110/InfraEdge.git
```

Enter the project directory:

```bash
cd InfraEdge
```

To verify that your GitHub SSH key is configured correctly:

```bash
ssh -T git@github.com
```

## Clone with HTTPS

```bash
git clone https://github.com/orbarak2110/InfraEdge.git
```

Then enter the project directory:

```bash
cd InfraEdge
```

---

# Create a Virtual Environment

Using a virtual environment keeps the project dependencies separate from the global Python installation.

## macOS and Linux

Create the virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

## Windows PowerShell

Create the virtual environment:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\Activate.ps1
```

## Windows Command Prompt

Create the virtual environment:

```cmd
python -m venv .venv
```

Activate it:

```cmd
.venv\Scripts\activate
```

After activation, the terminal should display `.venv`.

Example:

```text
(.venv) user@computer InfraEdge %
```

---

# Install Dependencies

Upgrade pip:

```bash
python -m pip install --upgrade pip
```

Install all project dependencies:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file installs the Python packages required by the project.

For example:

- Pytest
- Playwright
- Requests
- pytest-playwright

---

# Install Playwright Browsers

Installing the Playwright Python package does not automatically install the browser binaries.

Install all supported browsers:

```bash
playwright install
```

To install only Chromium:

```bash
playwright install chromium
```

For most local test executions, Chromium is enough.

On Linux or in a CI environment, use:

```bash
playwright install --with-deps chromium
```

---

# Verify the Installation

Check that Pytest is installed:

```bash
pytest --version
```

Check that Playwright is installed:

```bash
playwright --version
```

Check that the tests are discovered:

```bash
pytest --collect-only
```

---

# Configuration

The main project configuration is located in:

```text
config/settings.py
```

This file contains configuration values such as:

- Wikipedia page URL
- Wikipedia API URL
- Wikipedia page title
- Wikipedia section title
- Default Playwright timeout

Example:

```python
WIKIPEDIA_PAGE_URL = (
    "https://en.wikipedia.org/wiki/"
    "Test_automation#Test-driven_development"
)

WIKIPEDIA_API_URL = "https://en.wikipedia.org/w/api.php"

PAGE_TITLE = "Test automation"

SECTION_TITLE = "Test-driven development"

DEFAULT_TIMEOUT = 10_000
```

Playwright timeout values are defined in milliseconds.

For example:

```python
DEFAULT_TIMEOUT = 10_000
```

means a timeout of 10 seconds.

---

# Run the Tests

All commands should be executed from the project root directory.

The project root is the directory containing:

```text
pytest.ini
requirements.txt
conftest.py
README.md
```

## Run All Tests

```bash
pytest
```

The default Pytest options are already defined inside `pytest.ini`.

---

## Run All Tests in Headed Mode

By default, Playwright runs the browser in headless mode.

To display the browser during test execution:

```bash
pytest --headed
```

Headed mode is useful for:

- Debugging selectors
- Watching the test execution
- Investigating UI failures
- Understanding the browser flow

---

## Run the UI Tests

```bash
pytest tests/test_wikipedia_ui.py
```

Run the UI tests with a visible browser:

```bash
pytest tests/test_wikipedia_ui.py --headed
```

---

## Run the API Tests

```bash
pytest tests/test_wikipedia_api.py
```

API tests do not require opening a browser.

---

## Run the UI and API Comparison Tests

```bash
pytest tests/test_wikipedia_ui_and_api_word_counts.py
```

Run them in headed mode:

```bash
pytest tests/test_wikipedia_ui_and_api_word_counts.py --headed
```

---

## Run a Specific Test

Use the following format:

```bash
pytest path/to/test_file.py::test_function_name
```

Example:

```bash
pytest tests/test_wikipedia_ui.py::test_wikipedia_ui_word_counts
```

Run the same test in headed mode:

```bash
pytest tests/test_wikipedia_ui.py::test_wikipedia_ui_word_counts --headed
```

---

## Run Tests by Keyword

Run tests containing `api` in their name:

```bash
pytest -k api
```

Run tests containing `ui`:

```bash
pytest -k ui
```

Run tests containing `word_counts`:

```bash
pytest -k word_counts
```

---

## Run with a Specific Browser

Run with Chromium:

```bash
pytest --browser chromium
```

Run with Firefox:

```bash
pytest --browser firefox
```

Run with WebKit:

```bash
pytest --browser webkit
```

The required browser must be installed first.

Example:

```bash
playwright install firefox
```

---

## Run the Last Failed Tests

```bash
pytest --lf
```

`--lf` means:

```text
last failed
```

---

## Run Failed Tests First

```bash
pytest --ff
```

`--ff` means:

```text
failed first
```

---

## Stop After the First Failure

```bash
pytest -x
```

---

## Stop After Two Failures

```bash
pytest --maxfail=2
```

---

## Display Available Fixtures

```bash
pytest --fixtures
```

---

# Test Logging

The project creates a separate log file for every test module.

The log file is created inside the `tests` directory, next to the relevant test file.

For example, running:

```text
tests/test_wikipedia_ui.py
```

creates:

```text
tests/test_wikipedia_ui.log
```

Running:

```text
tests/test_wikipedia_api.py
```

creates:

```text
tests/test_wikipedia_api.log
```

Running:

```text
tests/test_wikipedia_ui_and_api_word_counts.py
```

creates:

```text
tests/test_wikipedia_ui_and_api_word_counts.log
```

## Log Format

Each log line contains:

```text
timestamp | log level | logger name | message
```

Example:

```text
2026-07-11 15:26:26,931 | INFO | conftest | Opening Wikipedia page
2026-07-11 15:26:27,668 | INFO | pages.wikipedia_page | Section title: Test-driven development
2026-07-11 15:26:27,671 | INFO | pages.wikipedia_page | Section content retrieved
2026-07-11 15:26:27,672 | INFO | utils.text_utils | Counting words
```

The log file is recreated for every test-module execution because the file handler uses:

```python
mode="w"
```

This means that logs from previous runs are replaced by the latest execution logs.

The logs are also displayed in the terminal.

---

# Pytest Configuration

The Pytest configuration is located in:

```text
pytest.ini
```

Recommended configuration:

```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_functions = test_*
addopts =
    -v
    -s
```

## Configuration Explanation

| Setting | Description |
|---|---|
| `testpaths = tests` | Pytest searches for tests inside the `tests` directory |
| `python_files = test_*.py` | Test files must start with `test_` |
| `python_functions = test_*` | Test functions must start with `test_` |
| `-v` | Displays detailed test names and results |
| `-s` | Displays logs and printed output in the terminal |

The browser runs headless by default.

To open the browser, use:

```bash
pytest --headed
```

---

# Tests Included in the Project

## UI Tests

The UI flow opens the configured Wikipedia page and extracts:

- The section title
- The full section content
- All text belonging to the section until the next heading

The UI tests validate that:

- The title is not empty
- The content is not empty
- The word-count result is not empty

---

## API Tests

The API flow sends HTTP requests to the Wikipedia API.

The API tests validate that:

- The Wikipedia page exists
- The requested section exists
- The section index can be found
- The section content is returned
- The word-count result is not empty

---

## UI and API Comparison

The comparison test retrieves the same Wikipedia section through:

- The Wikipedia website
- The Wikipedia API

The content is normalized, and the word-count dictionaries are compared.

This validates that the content returned through the browser matches the content returned through the API.

---

# Architecture

## Page Object Model

UI selectors and UI operations are stored inside page objects.

Example:

```text
pages/wikipedia_page.py
```

The tests do not interact directly with selectors.

Instead, they use page-object methods such as:

```python
get_section_title()
get_section_content()
```

This separates the test logic from the page implementation.

---

## API Object Model

API request logic is separated from the test files.

Example:

```text
infra_edge_flow/api_flow/wikipedia_api.py
```

The API layer is responsible for:

- Finding the section index
- Retrieving the section content
- Sending requests to Wikipedia
- Returning parsed response data

---

## Base API

Common HTTP request logic is located in:

```text
infra_edge_flow/api_flow/base_api.py
```

The base API layer is responsible for:

- Sending HTTP requests
- Applying request timeouts
- Validating HTTP status codes
- Parsing JSON responses
- Logging request information

---

## InfraEdgeFlow

The main flow object provides one central access point to the project components.

Example usage:

```python
infra_edge_flow.ui_flow.wikipedia_page
infra_edge_flow.api_flow.wikipedia_api
infra_edge_flow.utils
```

This allows the tests to use one shared fixture instead of creating each object separately.

---

## Fixtures

Shared fixtures are located in:

```text
conftest.py
```

The fixtures are responsible for:

- Setting the Playwright timeout
- Opening the Wikipedia page
- Creating the main flow object
- Creating a separate log file for each test module
- Cleaning up resources after the tests finish

---

# Troubleshooting

## `pytest: command not found`

Make sure the virtual environment is activated.

macOS or Linux:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Then install the dependencies:

```bash
pip install -r requirements.txt
```

You can also run Pytest through Python:

```bash
python -m pytest
```

---

## Playwright Browser Is Missing

Example error:

```text
Executable doesn't exist
```

Install Chromium:

```bash
playwright install chromium
```

Or install all browsers:

```bash
playwright install
```

---

## Browser Does Not Open

The project runs headless by default.

Use:

```bash
pytest --headed
```

---

## Import Errors

Make sure the test command is executed from the project root:

```bash
cd InfraEdge
pytest
```

Recommended:

```bash
pytest tests/test_wikipedia_ui.py
```

Avoid running the command from inside the `tests` directory.

---

## Tests Are Not Discovered

Verify that:

- Test files start with `test_`
- Test functions start with `test_`
- Test files are inside the `tests` directory
- `pytest.ini` is located in the project root

Check test discovery:

```bash
pytest --collect-only
```

---

## API Test Failure

Possible reasons:

- No internet connection
- Wikipedia is temporarily unavailable
- The page title is incorrect
- The section title changed
- The API response structure changed

Review the relevant log file inside the `tests` directory.

Example:

```text
tests/test_wikipedia_api.log
```

---

## UI Test Failure

Possible reasons:

- The Wikipedia HTML structure changed
- A selector is no longer valid
- The section title changed
- The page did not finish loading
- A Playwright timeout occurred

Run the test in headed mode:

```bash
pytest tests/test_wikipedia_ui.py --headed
```

Then review:

```text
tests/test_wikipedia_ui.log
```

---

# Clean Generated Files

## macOS and Linux

Remove generated log files:

```bash
find tests -name "*.log" -delete
```

Remove the Pytest cache:

```bash
rm -rf .pytest_cache
```

Remove Python cache directories:

```bash
find . -type d -name "__pycache__" -exec rm -rf {} +
```

## Windows PowerShell

Remove generated log files:

```powershell
Get-ChildItem -Path tests -Filter *.log -Recurse | Remove-Item
```

Remove the Pytest cache:

```powershell
Remove-Item -Recurse -Force .pytest_cache
```

Remove Python cache directories:

```powershell
Get-ChildItem -Recurse -Directory -Filter __pycache__ |
    Remove-Item -Recurse -Force
```

---

# Git Ignore

Generated files should not be committed to Git.

Recommended `.gitignore`:

```gitignore
# Virtual environments
.venv/
venv/

# Python cache
__pycache__/
*.py[cod]
*$py.class

# Pytest
.pytest_cache/
.coverage
htmlcov/

# Logs
*.log

# IDE
.idea/
.vscode/

# macOS
.DS_Store

# Playwright
test-results/
playwright-report/

# Environment files
.env
.env.*
```

The following rule prevents test log files from being committed:

```gitignore
*.log
```

---

# Complete Installation Example

## macOS and Linux

```bash
git clone git@github.com:orbarak2110/InfraEdge.git
cd InfraEdge

python3 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
pip install -r requirements.txt

playwright install chromium

pytest
```

Run the UI test with a visible browser:

```bash
pytest tests/test_wikipedia_ui.py --headed
```

Run the API tests:

```bash
pytest tests/test_wikipedia_api.py
```

Run the UI and API comparison tests:

```bash
pytest tests/test_wikipedia_ui_and_api_word_counts.py
```

After the execution, review the generated log files inside:

```text
tests/
```

---

# Deactivate the Virtual Environment

When you finish working on the project:

```bash
deactivate
```

---

<div align="center">

## Author

**Or Barak**

Automation Engineer

</div>