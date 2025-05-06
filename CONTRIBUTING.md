# Contributing to SimpleWeb

Thank you for considering contributing to SimpleWeb! This document provides guidelines and instructions for contributing to this project.

## Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct. Please be respectful and considerate of others.

## Getting Started

### Development Environment Setup

1. **Fork and clone the repository**:
   ```bash
   git clone https://github.com/yourusername/simple-webpage.git
   cd simple-webpage
   ```

2. **Set up the development environment**:
   ```bash
   # Run the installation script
   chmod +x install.sh
   ./install.sh
   
   # Activate the virtual environment
   source venv/bin/activate
   ```

3. **Run the development server**:
   ```bash
   python src/app.py
   ```

4. **Access the application**:
   Open your browser and navigate to `http://localhost:8000`

### Development Workflow

1. **Create a new branch for your feature or bugfix**:
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/issue-you-are-fixing
   ```

2. **Make your changes and test them locally**

3. **Run the tests to ensure everything works**:
   ```bash
   pytest
   ```

4. **Format and lint your code**:
   ```bash
   # Install development dependencies if not already installed
   pip install black isort flake8 mypy
   
   # Format code
   black src tests
   isort src tests
   
   # Lint code
   flake8 src tests
   mypy src
   ```

5. **Commit your changes with a descriptive message**:
   ```bash
   git add .
   git commit -m "Add feature: your feature description"
   ```

6. **Push your branch to GitHub**:
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request on GitHub**

## Pull Request Guidelines

When submitting a pull request, please ensure:

1. Your code follows the project's coding style and conventions
2. You have added tests for your changes
3. All tests pass
4. Your PR includes a clear description of the changes and why they are needed
5. Your PR addresses a specific issue or adds a specific feature

## Coding Standards

### Python

- Follow PEP 8 style guide
- Use type hints for all function parameters and return values
- Write docstrings for all functions, classes, and modules
- Keep functions small and focused on a single responsibility
- Use meaningful variable and function names

### HTML/CSS/JavaScript

- Use 2-space indentation for HTML and CSS
- Follow BEM methodology for CSS class naming
- Write semantic HTML
- Ensure accessibility (WCAG 2.1 AA compliance)
- Keep JavaScript modular and well-commented

## Testing

- Write unit tests for all new functionality
- Ensure existing tests pass with your changes
- Aim for high test coverage

## Documentation

- Update documentation when changing functionality
- Document new features thoroughly
- Keep the README.md up to date

## Reporting Bugs

When reporting bugs, please include:

1. A clear and descriptive title
2. Steps to reproduce the issue
3. Expected behavior
4. Actual behavior
5. Screenshots if applicable
6. Your environment (OS, browser, etc.)

## Feature Requests

Feature requests are welcome! Please provide:

1. A clear and descriptive title
2. A detailed description of the proposed feature
3. Any relevant examples or mockups
4. Why this feature would be useful to most users

## Questions?

If you have any questions about contributing, please open an issue with your question.

Thank you for contributing to SimpleWeb!