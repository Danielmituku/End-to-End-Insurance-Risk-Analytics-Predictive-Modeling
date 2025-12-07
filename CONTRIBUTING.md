# Contributing Guidelines

## Development Workflow

1. **Create a branch** for your task:
   ```bash
   git checkout -b task-1
   ```

2. **Make changes** and commit frequently with descriptive messages:
   ```bash
   git add .
   git commit -m "feat: add EDA analysis for loss ratio by province"
   ```

3. **Push your branch**:
   ```bash
   git push origin task-1
   ```

4. **Create a Pull Request** to merge into main

## Commit Message Convention

We follow [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `test:` Adding or updating tests
- `refactor:` Code refactoring
- `style:` Code style changes (formatting, etc.)
- `chore:` Maintenance tasks

## Code Style

- Use **Black** for code formatting (line length: 100)
- Follow **PEP 8** guidelines
- Use type hints where appropriate
- Write docstrings for all functions and classes (Google style)

## Testing

- Write tests for all new functionality
- Ensure all tests pass before submitting a PR
- Aim for >80% code coverage

## Documentation

- Update README.md if adding new features
- Document all functions and classes
- Include examples in docstrings

