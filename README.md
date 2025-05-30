# be-llm101

A Python package for LLM-related utilities and functions.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/bearingpoint-no/LLM101/blob/main/notebooks/LLM101_FINAL.ipynb)

## 📚 Interactive Tutorial

Try the interactive tutorial in Google Colab: **[LLM101 Final Tutorial](https://colab.research.google.com/github/bearingpoint-no/LLM101/blob/main/notebooks/LLM101_FINAL.ipynb)**

## Description

This package provides utilities and functions for working with Large Language Models (LLMs). It's designed to be a beginner-friendly introduction to using language models in Python applications.

## Installation

You can install the package using pip:

```bash
pip install be-llm101
```

For development installation:

```bash
git clone <repository-url>
cd LLM101
uv sync
```

## Usage

### Basic Usage

```python
from be_llm101 import hello_llm101, get_package_info, LLMUtility

# Simple greeting function
print(hello_llm101("Alice"))
# Output: Hello, Alice! Welcome to be-llm101 package!

# Get package information
info = get_package_info()
print(f"Package version: {info['version']}")

# Use the LLM utility class
llm = LLMUtility("gpt-4")
result = llm.process_text("Hello, world!")
print(result)
# Output: Processed by gpt-4: Hello, world!
```

## Development

This package uses `uv` for dependency management and `hatchling` for building.

### Building the Package

```bash
uv build
```

### Running Tests

```bash
uv run pytest
```

## Dependencies

- langchain-core>=0.3.35
- langchain-openai>=0.3.6
- python-dotenv>=1.0.1
- openpyxl>=3.1.5
- pandas>=2.2.3

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.