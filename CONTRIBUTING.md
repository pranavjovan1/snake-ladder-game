# Contributing to Snake and Ladder Game

Thank you for your interest in contributing to the Snake and Ladder Game project! We appreciate all contributions.

## How to Contribute

### Reporting Bugs

Before creating a bug report, please check the issue list as you might find out that you don't need to create one. When you create a bug report, please include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps which reproduce the problem**
- **Provide specific examples to demonstrate the steps**
- **Describe the behavior you observed after following the steps**
- **Explain which behavior you expected to see instead and why**
- **Include screenshots and animated GIFs if possible**
- **Include your Python version and OS**

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

- **Use a clear and descriptive title**
- **Provide a step-by-step description of the suggested enhancement**
- **Provide specific examples to demonstrate the steps**
- **Describe the current behavior and expected behavior**
- **Include screenshots and animated GIFs if possible**

### Pull Requests

- Fill in the required template
- Follow the Python style guide
- Include appropriate test cases
- Update documentation as needed
- End all files with a newline

## Development Setup

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/snake-ladder-game.git
   cd snake-ladder-game
   ```

3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

### Running Tests

```bash
python -m pytest test_game.py -v
```

### Code Style

- Follow PEP 8
- Use descriptive variable names
- Add docstrings to functions and classes
- Keep lines under 100 characters

### Commit Messages

- Use clear and meaningful commit messages
- Start with a verb (Add, Fix, Update, etc.)
- Reference issues when applicable

Example:
```
Add multiplayer support for up to 4 players
Fix snake collision detection bug
Update README with new examples
```

## Pull Request Process

1. Update tests for any new functionality
2. Run tests and ensure they pass
3. Update documentation if needed
4. Add your changes to the CHANGELOG.md
5. Push to your fork and submit a pull request

## Code of Conduct

Please be respectful and constructive in all interactions.

## Questions?

Feel free to open an issue or contact the maintainers.

Thank you for contributing! 🎉
