# Contributing to ResponsiveCapture

First off, thank you for considering contributing to **ResponsiveCapture**! 🎉 Your contributions help make this project better for everyone.

The following guidelines outline how you can contribute to the project effectively. By participating, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Enhancements](#suggesting-enhancements)
  - [Pull Requests](#pull-requests)
- [Development Setup](#development-setup)
  - [Prerequisites](#prerequisites)
  - [Setting Up the Environment](#setting-up-the-environment)
- [Coding Guidelines](#coding-guidelines)
  - [Style Guide](#style-guide)
  - [Commit Messages](#commit-messages)
- [License](#license)
- [Questions?](#questions)

## Code of Conduct

Please read and follow our [Code of Conduct](CODE_OF_CONDUCT.md) to ensure a welcoming and respectful environment for all contributors.

## How Can I Contribute?

### Reporting Bugs

**Great!** Reporting bugs helps us improve the project. Here's how you can help:

1. **Search for existing issues**: Before opening a new issue, check if it has already been reported.
2. **Open a new issue**: If the bug hasn't been reported, open a new issue with the following details:
   - **Descriptive title**: Clearly summarize the bug.
   - **Detailed description**: Explain what you expected to happen and what actually happened.
   - **Steps to reproduce**: Provide a step-by-step guide to reproduce the issue.
   - **Screenshots**: If applicable, include screenshots to illustrate the problem.
   - **Environment details**: Include information about your setup (e.g., OS, Docker version, Python version).

### Suggesting Enhancements

**Awesome!** Enhancements help us add new features and improve existing ones. Here's how you can suggest enhancements:

1. **Search for existing suggestions**: Ensure your enhancement hasn't already been proposed.
2. **Open a new issue**: If it's a new idea, open an issue with the following:
   - **Descriptive title**: Clearly state the enhancement.
   - **Detailed description**: Explain the enhancement and its benefits.
   - **Use cases**: Provide examples of how the enhancement would be used.

### Pull Requests

**Fantastic!** Pull Requests (PRs) are the way to go. Here's how to make them smooth:

1. **Fork the repository**: Click the "Fork" button at the top right of the repository page.
2. **Clone your fork**:
   ```bash
   git clone https://github.com/your-username/ResponsiveCapture.git
   cd ResponsiveCapture
   ```
3. **Create a new branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Make your changes**: Implement your feature or fix.
5. **Commit your changes**:
   ```bash
   git commit -m "feat: add feature X to improve Y"
   ```
6. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Open a Pull Request**: Go to the original repository and click the "New Pull Request" button.

**Before submitting a Pull Request**, please ensure that:

- Your code follows the project's coding guidelines.
- Your changes have been tested.
- You have updated documentation as needed.

## Development Setup

To contribute effectively, set up your development environment as follows:

### Prerequisites

- **Docker**: Ensure Docker is installed and running on your machine.
- **Git**: Version control system installed.
- **Python**: Python 3.8 or higher is required.

### Setting Up the Environment

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/ResponsiveCapture.git
   cd ResponsiveCapture
   ```
2. **Build the Docker image**:
   ```bash
   docker build -t responsive-capture .
   ```
3. **Run the Docker container**:
   ```bash
   docker run -it --name responsive-capture-container \
     -v "$(pwd)":/workspace \
     -v "$(pwd)/logs":/workspace/logs \
     -v "$(pwd)/screenshots":/workspace/screenshots \
     responsive-capture
   ```
4. **Install dependencies** (if not already handled in Dockerfile):
   ```bash
   pip install -r requirements.txt
   playwright install
   ```
5. **Copy and edit the configuration file**:
   ```bash
   cp config/config.yaml.example config/config.yaml
   ```
   - **Edit `config/config.yaml`**: Update the configuration with your target URLs, browser settings, and other necessary parameters.

6. **Run the script**:
   ```bash
   python scripts/take_screenshots.py
   ```

## Coding Guidelines

### Style Guide

- **Follow PEP 8**: Adhere to the [PEP 8](https://pep8.org/) style guide for Python code.
- **Meaningful Names**: Use clear and descriptive variable and function names.
- **Documentation**: Write clear and concise documentation/comments.
- **Modular Code**: Organize code into reusable and maintainable modules.

### Commit Messages

- **Clear and Descriptive**: Ensure commit messages clearly describe the changes.
- **Consistent Format**: Follow the format `type(scope): description`.
  - **type**: feat, fix, docs, style, refactor, test, chore
  - **scope**: (optional) e.g., script, config
  - **description**: Brief summary of changes

**Examples**:
```
feat(scripts): add retry mechanism to screenshot capture
fix(config): correct typo in config.yaml.example
docs: update README with installation steps
```

## License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).

## Questions?

If you have any questions, feel free to open an issue or reach out to the maintainers.
