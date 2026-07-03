# Python Project Example

This example demonstrates how to use contributor-ready with a Python project.

## Project Structure

```
my-python-project/
├── src/
│   └── my_package/
│       ├── __init__.py
│       ├── main.py
│       ├── utils.py
│       └── models.py
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   └── test_utils.py
├── docs/
│   └── api.md
├── pyproject.toml
├── README.md
├── LICENSE
└── .github/
    └── workflows/
        └── ci.yml
```

## Detection

When analyzing a Python project, contributor-ready detects:

- **Language**: Python (by `.py` files)
- **Package Manager**: pip, poetry, or conda (by lock files)
- **Build System**: setuptools, poetry, or hatch (by pyproject.toml)
- **Test Framework**: pytest, unittest (by test files and config)
- **Linter**: flake8, pylint, ruff (by config files)
- **Formatter**: black, isort (by config files)

## Generated Files

### README.md

```markdown
# My Python Project

A Python package for {description}.

## Installation

### From PyPI

```bash
pip install my-python-project
```

### From Source

```bash
git clone https://github.com/{owner}/{repo}.git
cd {repo}
pip install -e ".[dev]"
```

## Quick Start

```python
from my_package import main

# Basic usage
result = main.do_something("input")
print(result)
```

## Usage

### Advanced Usage

```python
from my_package import main, utils

# Configure the module
config = {
    "option1": "value1",
    "option2": "value2"
}

# Use with configuration
result = main.do_something("input", config=config)

# Use utility functions
processed = utils.process_data(result)
```

### Command Line Interface

```bash
# Basic usage
python -m my_package "input"

# With options
python -m my_package "input" --option1 value1 --option2 value2
```

## API Reference

### `main.do_something(input, config=None)`

Process input data.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `input` | `str` | Input data to process |
| `config` | `dict` | Optional configuration |

**Returns:**

| Type | Description |
|------|-------------|
| `str` | Processed result |

**Example:**

```python
result = main.do_something("hello")
# Output: "processed: hello"
```

### `utils.process_data(data)`

Process data using utility functions.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `data` | `str` | Data to process |

**Returns:**

| Type | Description |
|------|-------------|
| `str` | Processed data |

## Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `MY_PROJECT_OPTION1` | First option | `default1` |
| `MY_PROJECT_OPTION2` | Second option | `default2` |

### Configuration File

Create a `config.yaml` in your project root:

```yaml
option1: value1
option2: value2
debug: false
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT — see [LICENSE](LICENSE) for details.
```

### CONTRIBUTING.md

```markdown
# Contributing to My Python Project

Thank you for your interest in contributing!

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip
- Poetry (optional, for development)

### Development Setup

1. Fork the repository
2. Clone your fork
3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

### Making Changes

1. Create a branch for your changes
2. Make your changes
3. Run tests:
   ```bash
   pytest
   ```
4. Run linter:
   ```bash
   flake8 src/
   ```
5. Format code:
   ```bash
   black src/
   ```
6. Commit your changes

### Commit Convention

```
{type}({scope}): {description}
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Formatting
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance

### Submitting a Pull Request

1. Push your branch
2. Create a pull request
3. Fill out the PR template
4. Wait for review

## Code Style

- Follow PEP 8
- Use Black for formatting
- Use isort for import sorting
- Use flake8 for linting

## Testing

- Write tests for new features
- Maintain test coverage
- Use pytest for testing
- Use descriptive test names

## Questions?

If you have questions, feel free to:

- Open a discussion
- Ask in Discord
- Create an issue with the `question` label
```

### SECURITY.md

```markdown
# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| 1.0.x   | ✅ |
| < 1.0   | ❌ |

## Reporting a Vulnerability

If you discover a security vulnerability, please send an email to security@example.com.

**Please do NOT report security vulnerabilities through public GitHub issues.**

## Response Timeline

- **Acknowledgment**: Within 48 hours
- **Initial Assessment**: Within 1 week
- **Fix Released**: Within 30 days

## Security Best Practices

- Keep dependencies up to date
- Use environment variables for secrets
- Validate all user input
- Use HTTPS in production

## Contact

For security-related questions, please contact security@example.com.
```

### .github/workflows/ci.yml

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.8', '3.9', '3.10', '3.11', '3.12']
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -e ".[dev]"
      
      - name: Lint with flake8
        run: |
          flake8 src/
      
      - name: Format with black
        run: |
          black --check src/
      
      - name: Test with pytest
        run: |
          pytest --cov=my_package
```

### pyproject.toml

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "my-python-project"
version = "0.1.0"
description = "A Python package for {description}"
readme = "README.md"
license = "MIT"
requires-python = ">=3.8"
authors = [
    { name = "{author}", email = "{email}" }
]
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
]
dependencies = []

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "pytest-cov>=4.0.0",
    "flake8>=6.0.0",
    "black>=23.0.0",
    "isort>=5.0.0",
]

[project.scripts]
my-package = "my_package.main:main"

[tool.pytest.ini_options]
testpaths = ["tests"]
coverage = ["src/my_package"]

[tool.black]
line-length = 88
target-version = ["py38", "py39", "py310", "py311", "py312"]

[tool.isort]
profile = "black"

[tool.flake8]
max-line-length = 88
extend-ignore = ["E203", "W503"]
```

## Checklist

When using contributor-ready with a Python project:

- [ ] Detect Python version and package manager
- [ ] Check for pyproject.toml, setup.py, or setup.cfg
- [ ] Detect testing framework (pytest, unittest)
- [ ] Detect linter (flake8, pylint, ruff)
- [ ] Detect formatter (black, isort)
- [ ] Check for type hints
- [ ] Check for documentation
- [ ] Generate Python-specific README
- [ ] Generate Python-specific CONTRIBUTING.md
- [ ] Generate Python-specific CI workflow
- [ ] Generate Python-specific SECURITY.md
