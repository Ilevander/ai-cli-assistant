# ai-cli-assistant# AI CLI Assistant

A command-line AI assistant built with Python, Ollama and gemma3/Qwen3.

The project provides an interactive CLI assistant capable of maintaining conversation history and using Python tools to perform actions such as retrieving the current date/time and interacting with files.

The project is designed as a portfolio-quality Python application, with a modular architecture, automated tests and a Git-based development workflow.

---

## Features

### AI conversation

* Interactive command-line conversation mode
* Single-prompt command-line mode
* Local AI inference using Ollama
* Qwen3 8B model
* Conversation history between user and assistant messages

### Tool calling

The assistant can dynamically call Python functions through Ollama's tool-calling mechanism.

Currently implemented tools:

#### Datetime tools

* `get_current_date()`
* `get_current_datetime()`
* `get_current_time()`
* `get_day_of_week()`

#### File tools

* `file_exists(path)`
* `read_file(path)`
* `write_file(path, content)`
* `list_files(path)`

The assistant decides when a tool is required, Ollama generates the tool call, Python executes the corresponding function, and the result is returned to the model before generating the final response.

---

## Architecture

The application follows a modular architecture:

```text
User
 │
 ▼
CLI
 │
 ▼
Assistant
 │
 ├── ConversationHistory
 │
 ├── Available Python Tools
 │       ├── Datetime tools
 │       └── File tools
 │
 ▼
Ollama
 │
 ▼
Qwen3:8b
 │
 ├── Normal response
 │
 └── Tool call
        │
        ▼
     Python tool
        │
        ▼
     Tool result
        │
        ▼
      Qwen3
        │
        ▼
    Final response
```

---

## Project Structure

```text
ai-cli-assistant/
│
├── src/
│   └── ai_assistant/
│       ├── __init__.py
│       ├── cli.py
│       ├── assistant.py
│       ├── config.py
│       ├── history.py
│       │
│       └── tools/
│           ├── __init__.py
│           ├── calculator.py
│           ├── datetime.py
│           ├── files.py
│           ├── system.py
│           └── git.py
│
├── tests/
│   ├── test_cli.py
│   ├── test_assistant.py
│   ├── test_history.py
│   └── test_tools.py
│
├── docs/
│   └── uml/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── .gitignore
├── Dockerfile
├── LICENSE
├── README.md
└── pyproject.toml
```

> Some tool files are currently reserved for future development and are not yet part of the active functionality.

---

# Requirements

Before installing the project, make sure the following software is available.

## Python

Python 3.10 or newer is required.

Check your Python version:

```bash
python --version
```

Example:

```text
Python 3.14.3
```

---

## Ollama

The assistant uses Ollama to run the language model locally.

Install Ollama from the official Ollama website:

https://ollama.com/

After installation, verify that Ollama is available:

```bash
ollama --version
```

---

## Qwen3

The project currently uses the Qwen3 8B model:

```text
qwen3:8b
```

Download it with:

```bash
ollama pull qwen3:8b
```

Verify that the model is available:

```bash
ollama list
```

You should see something similar to:

```text
NAME       ID              SIZE
qwen3:8b   ...             ...
```

> Qwen3 is used because the current implementation relies on Ollama tool calling.

---

# Installation

## 1. Clone the repository

```bash
git clone <repository-url>
```

Move into the project directory:

```bash
cd ai-cli-assistant
```

---

## 2. Create a virtual environment

On Windows:

```bash
python -m venv .venv
```

Activate it with Git Bash:

```bash
source .venv/Scripts/activate
```

Or with Windows Command Prompt:

```cmd
.venv\Scripts\activate
```

Or with PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

---

## 3. Install the project

Install the project and its dependencies:

```bash
pip install -e .
```

Install development dependencies:

```bash
pip install -e ".[dev]"
```

The development dependencies currently include:

* pytest

---

# Running the Application

The application supports two main modes.

## Interactive conversation mode

Start the assistant without a prompt:

```bash
python -m ai_assistant.cli
```

You will see:

```text
AI Assistant - conversation mode
Type 'exit' to quit.
```

You can then interact with the assistant:

```text
You > Bonjour
AI  > Bonjour ! Comment puis-je vous aider ?

You > Quelle est la date aujourd'hui ?
AI  > Nous sommes le ...
```

Type:

```text
exit
```

to leave the application.

---

## Single prompt mode

You can also provide a prompt directly from the command line:

```bash
python -m ai_assistant.cli "Explique-moi Git"
```

The assistant processes the request and returns the response.

---

## Version

Display the application version:

```bash
python -m ai_assistant.cli --version
```

Expected output:

```text
ai-cli-assistant 0.1.0
```

---

# Tool Calling

One of the main features of the project is the integration between Qwen3 and Python tools.

The assistant exposes Python functions to Ollama.

The available tools are registered in:

```text
src/ai_assistant/assistant.py
```

Example:

```python
self.available_tools = {
    "get_current_date": get_current_date,
    "get_current_datetime": get_current_datetime,
    "get_current_time": get_current_time,
    "get_day_of_week": get_day_of_week,
    "file_exists": file_exists,
    "list_files": list_files,
    "read_file": read_file,
    "write_file": write_file,
}
```

The functions are then passed to Ollama:

```python
self.tools = list(self.available_tools.values())
```

---

## Tool Calling Flow

When a user asks:

```text
Est-ce que README.md existe ?
```

the assistant follows this process:

```text
User
 │
 ▼
Qwen3
 │
 │ tool call
 ▼
file_exists("README.md")
 │
 ▼
Python
 │
 │ True
 ▼
Ollama
 │
 ▼
Qwen3
 │
 ▼
Final response
```

For example:

```text
You > Est-ce que README.md existe ?

AI > Le fichier README.md existe.
```

The Python function performs the actual file-system operation instead of asking the language model to guess.

---

# Datetime Tools

Datetime tools are implemented in:

```text
src/ai_assistant/tools/datetime.py
```

## `get_current_datetime()`

Returns the current date and time.

Example:

```python
get_current_datetime()
```

Output:

```text
2026-09-17 15:30:00
```

---

## `get_current_date()`

Returns the current date.

Example:

```python
get_current_date()
```

Output:

```text
2026-09-17
```

---

## `get_current_time()`

Returns the current time.

Example:

```python
get_current_time()
```

Output:

```text
15:30:00
```

---

## `get_day_of_week()`

Returns the current day of the week.

Example:

```python
get_day_of_week()
```

Output:

```text
Thursday
```

---

# File Tools

File tools are implemented in:

```text
src/ai_assistant/tools/files.py
```

## `file_exists(path)`

Checks whether a file exists.

Example:

```python
file_exists("README.md")
```

Returns:

```text
True
```

---

## `read_file(path)`

Reads a UTF-8 text file.

Example:

```python
read_file("README.md")
```

Returns the file content as a string.

---

## `write_file(path, content)`

Creates or overwrites a text file.

Example:

```python
write_file(
    "example.txt",
    "Hello from AI CLI Assistant"
)
```

---

## `list_files(path)`

Lists files contained in a directory.

Example:

```python
list_files(".")
```

Possible result:

```text
[
    ".gitignore",
    "Dockerfile",
    "README.md",
    "pyproject.toml"
]
```

---

# Conversation History

Conversation history is implemented in:

```text
src/ai_assistant/history.py
```

The `ConversationHistory` class stores messages exchanged between the user and the assistant.

Example:

```python
history.add_user_message("Bonjour")
history.add_assistant_message("Bonjour !")
```

The internal representation is:

```python
[
    {
        "role": "user",
        "content": "Bonjour",
    },
    {
        "role": "assistant",
        "content": "Bonjour !",
    },
]
```

This history is then passed to Ollama during subsequent requests.

This allows the assistant to maintain context during an interactive session.

---

# Testing

The project uses `pytest`.

Run all tests:

```bash
python -m pytest -v
```

The current test suite covers:

```text
tests/
├── test_cli.py
├── test_assistant.py
├── test_history.py
└── test_tools.py
```

The project currently contains **16 automated tests** covering:

* CLI behavior
* assistant responses
* conversation history
* datetime tools
* file tools

Example successful result:

```text
============================== 16 passed ==============================
```

---

# Code Quality

Before committing changes, check for whitespace errors:

```bash
git diff --check
```

A clean result produces no output.

Recommended validation sequence:

```bash
python -m pytest -v
git diff --check
git status
```

---

# Git Workflow

The project follows a feature-branch workflow.

The general development process is:

```text
main
 │
 ├── feature/cli
 │
 ├── feature/ai-integration
 │
 ├── feature/ollama-integration
 │
 ├── feature/conversation-history
 │
 └── feature/tools
```

A feature is developed independently before being merged into `main`.

Typical workflow:

```bash
git checkout main
git pull origin main

git checkout -b feature/my-feature
```

Develop the feature and run tests:

```bash
python -m pytest -v
```

Check the changes:

```bash
git diff
git diff --check
git status
```

Stage the required files:

```bash
git add <files>
```

Create a commit:

```bash
git commit -m "feat: add my feature"
```

Push the branch:

```bash
git push -u origin feature/my-feature
```

Then create a Pull Request on GitHub:

```text
feature/my-feature → main
```

After the Pull Request is merged:

```bash
git checkout main
git pull origin main
```

---

# Commit Convention

The project uses conventional commit-style messages.

Examples:

```text
feat: add datetime tool calling
feat: add file tools
fix: correct conversation history handling
test: add file tool tests
docs: update project documentation
refactor: simplify tool registration
chore: update project configuration
```

Common prefixes:

| Prefix     | Usage              |
| ---------- | ------------------ |
| `feat`     | New functionality  |
| `fix`      | Bug fix            |
| `test`     | Tests              |
| `docs`     | Documentation      |
| `refactor` | Code restructuring |
| `chore`    | Maintenance        |

---

# Development Principles

The project follows several development principles.

## Separation of concerns

Each component has a specific responsibility:

```text
cli.py
    ↓
User interface

assistant.py
    ↓
AI orchestration

history.py
    ↓
Conversation management

tools/
    ↓
External actions
```

---

## Test before integration

Tools are first implemented and tested independently.

Then they are integrated into the assistant.

The workflow is:

```text
Implementation
     ↓
Unit tests
     ↓
Integration
     ↓
Manual validation
     ↓
Commit
```

---

## Local-first AI

The project uses Ollama to run the model locally.

Advantages include:

* no dependency on a remote AI API for inference
* local model execution
* no API key required for Ollama inference
* ability to experiment with different local models
* support for tool calling

---

# Configuration

The project currently uses Qwen3 8B through Ollama:

```python
model="qwen3:8b"
```

The model must therefore be available locally through Ollama.

Future versions can move this value to a configuration system or environment variable.

---

# Docker

A Docker configuration is included in the repository:

```text
Dockerfile
```

The Docker setup is intended to make the Python application reproducible across environments.

Because Ollama runs the AI model separately, the complete local AI environment may require Ollama to be available outside the application container or configured as a separate service.

Docker support can therefore be expanded as the project architecture evolves.

---

# CI/CD

The project contains a GitHub Actions workflow:

```text
.github/
└── workflows/
    └── tests.yml
```

The purpose of the workflow is to automatically run the test suite when changes are pushed to GitHub.

The expected CI process is:

```text
Git push
    ↓
GitHub Actions
    ↓
Install dependencies
    ↓
Run pytest
    ↓
Tests pass / fail
```

This helps prevent regressions before changes are merged into `main`.

---

# UML and Technical Documentation

Technical architecture documentation is maintained under:

```text
docs/
```

UML diagrams are stored under:

```text
docs/uml/
```

Planned diagrams include:

* Class diagram
* Sequence diagram
* Component architecture
* Tool-calling sequence

The tool-calling sequence can be represented as:

```text
User
 │
 │ prompt
 ▼
CLI
 │
 ▼
Assistant
 │
 ▼
Ollama / Qwen3
 │
 │ tool call
 ▼
Python Tool
 │
 │ result
 ▼
Ollama / Qwen3
 │
 │ final response
 ▼
Assistant
 │
 ▼
CLI
 │
 ▼
User
```

---

# Roadmap

The project is being developed incrementally.

## Completed

* [x] Python project structure
* [x] CLI interface
* [x] Command-line prompt mode
* [x] Interactive conversation mode
* [x] Ollama integration
* [x] Qwen3 integration
* [x] Conversation history
* [x] Datetime tools
* [x] File tools
* [x] Automated tests
* [x] Git feature-branch workflow
* [x] Pull Request workflow

## Planned

* [ ] System information tools
* [ ] Git tools
* [ ] Calculator tool
* [ ] Improved tool registry
* [ ] Better configuration management
* [ ] Structured logging
* [ ] Streaming responses
* [ ] Improved error handling
* [ ] More comprehensive integration tests
* [ ] Complete UML documentation
* [ ] Docker improvements
* [ ] CI/CD improvements

---

# Known Limitations

The current implementation has several limitations.

### Local model performance

Qwen3 8B runs locally through Ollama, so response speed depends on the available hardware.

Tool calls can also require multiple model interactions:

```text
Initial model request
        ↓
Tool call
        ↓
Python execution
        ↓
Second model request
        ↓
Final response
```

This can make tool-based requests slower than simple responses.

### File operations

The current file tools operate directly on paths supplied to Python.

Future versions should introduce additional safeguards such as:

* restricted directories
* better path validation
* improved error handling
* protection against unintended file modifications

### Conversation history

The complete conversation history is currently kept in memory during the session.

Future versions could support:

* persistent history
* history limits
* context summarization
* database storage

---

# Error Handling

The project is designed to progressively improve error handling.

For example, unknown tools are handled by the assistant:

```python
if function_to_call is None:
    result = f"Unknown tool: {function_name}"
```

Future versions will provide more robust handling for:

* missing files
* invalid paths
* permission errors
* invalid tool arguments
* Ollama connection errors
* unavailable models

---

# Technology Stack

| Technology     | Purpose                      |
| -------------- | ---------------------------- |
| Python         | Application language         |
| Ollama         | Local AI model runtime       |
| Qwen3 8B       | Language model               |
| pytest         | Automated testing            |
| Git            | Version control              |
| GitHub         | Repository and Pull Requests |
| GitHub Actions | CI                           |
| Docker         | Containerization             |

---

# AI Model Selection

## Initial model: Gemma 3

The project initially used **Gemma 3** as the local language model through Ollama.

Gemma 3 was used during the first stages of the project to validate the core AI assistant functionality:

```text
User
 ↓
CLI
 ↓
Assistant
 ↓
Ollama
 ↓
Gemma 3
 ↓
Response
```

At this stage, the main objective was to verify that:

* the CLI could communicate with a local language model;
* Ollama was correctly integrated with Python;
* the `Assistant` class could send prompts to the model;
* the assistant could return generated responses;
* the conversation interface worked correctly.

Gemma 3 therefore served as the **initial local LLM used to validate the basic architecture of the assistant**.

---

## Why switch from Gemma 3 to Qwen3?

The project later introduced **tool calling**, which significantly changed the requirements for the language model.

The assistant needed to be able to ask Python to execute specific functions, for example:

```text
User
 ↓
"Quelle est la date aujourd'hui ?"
 ↓
Qwen3
 ↓
get_current_date()
 ↓
Python
 ↓
Tool result
 ↓
Qwen3
 ↓
Final answer
```

The first Gemma 3 model used in the project did not support the required Ollama tool-calling workflow.

When the assistant attempted to expose Python tools to that model, Ollama returned an error indicating that the selected Gemma 3 model did not support tools:

```text
registry.ollama.ai/library/gemma3:latest does not support tools
```

As a result, Gemma 3 was suitable for the initial conversational stage, but it could not satisfy the new technical requirement for function/tool calling in the selected configuration.

---

## Migration to Qwen3 8B

The project therefore switched to:

```text
qwen3:8b
```

Qwen3 8B supports the tool-calling workflow required by the application.

The architecture became:

```text
User
 │
 ▼
CLI
 │
 ▼
Assistant
 │
 ▼
Ollama
 │
 ▼
Qwen3 8B
 │
 ├── Normal response
 │
 └── Tool call
        │
        ▼
   Python function
        │
        ▼
    Tool result
        │
        ▼
     Qwen3 8B
        │
        ▼
   Final response
```

This allowed the assistant to integrate real Python capabilities such as:

* retrieving the current date;
* retrieving the current time;
* retrieving the current date and time;
* retrieving the day of the week;
* checking whether a file exists;
* reading files;
* writing files;
* listing files.

---

## Evolution of the AI architecture

The evolution of the project can therefore be summarized as follows:

### Phase 1 — Basic AI assistant

```text
CLI
 ↓
Assistant
 ↓
Ollama
 ↓
Gemma 3
 ↓
Response
```

**Objective:** validate the basic conversational architecture.

### Phase 2 — Local AI integration

```text
CLI
 ↓
Assistant
 ↓
Ollama
 ↓
Local LLM
 ↓
Response
```

**Objective:** run the assistant locally without relying on a remote inference API.

### Phase 3 — Tool calling

```text
CLI
 ↓
Assistant
 ↓
Ollama
 ↓
Qwen3 8B
 ↓
Tool call
 ↓
Python tool
 ↓
Tool result
 ↓
Qwen3 8B
 ↓
Final response
```

**Objective:** allow the language model to interact with real Python functionality.

---

## Technical Decision

The switch from Gemma 3 to Qwen3 was therefore not based on response quality or personal preference.

It was driven by a **technical compatibility requirement** introduced by the tool-calling architecture.

| Requirement                              |                            Gemma 3 initially used |  Qwen3 8B |
| ---------------------------------------- | ------------------------------------------------: | --------: |
| Local inference                          |                                               Yes |       Yes |
| Ollama integration                       |                                               Yes |       Yes |
| Basic conversation                       |                                               Yes |       Yes |
| Python tool calling                      | Not supported by the selected model configuration | Supported |
| Suitable for the tool-based architecture |                                                No |       Yes |

The project consequently uses **Qwen3 8B as the current model** because tool calling is a core capability of the assistant architecture.

---

# Project Goals

The main objective of this project is to build a modular and extensible AI assistant that demonstrates practical Python software-engineering skills.

The project focuses on:

* Python development
* CLI application design
* AI integration
* Local LLMs
* Tool calling
* Automated testing
* Software architecture
* Git and GitHub workflows
* CI/CD
* Docker
* Technical documentation
* UML modeling

The architecture is intentionally modular so that additional tools and capabilities can be added without redesigning the entire application.

---

# License

This project is distributed under the license specified in:

```text
LICENSE
```

---

# Author

Developed as a Python and AI engineering portfolio project.

---

## Quick Start

For a quick setup:

```bash
git clone <repository-url>

cd ai-cli-assistant

python -m venv .venv

source .venv/Scripts/activate

pip install -e ".[dev]"

ollama pull qwen3:8b

python -m pytest -v

python -m ai_assistant.cli
```

Then start interacting with the assistant:

```text
You > Quelle est la date aujourd'hui ?

You > Est-ce que README.md existe ?

You > Lis le README.md et résume-le.

You > Liste les fichiers du dossier courant.
```

Type:

```text
exit
```

to exit the application.
