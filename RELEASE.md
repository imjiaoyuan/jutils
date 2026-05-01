# Release Checklist

## Before release

- [ ] Tests pass: `uv run --extra dev --extra all pytest tests/`
- [ ] Lint: `uv run ruff check src/`
- [ ] Format: `uv run black --check src/ tests/`

## Version bump

- [ ] Update `version` in `pyproject.toml`
- [ ] Update `__version__` in `src/jsrc/__init__.py`
- [ ] Verify both match

## Docs

- [ ] Update docs if CLI flags or behavior changed
- [ ] Update module maturity level in docs if applicable (see STABILITY.md)

## Build verification

- [ ] Build wheel and sdist: `uv build`
- [ ] Verify wheel installs clean: `pip install dist/jsrc-*.whl && jsrc --help`
- [ ] Check sdist contains expected files: `tar tf dist/jsrc-*.tar.gz`

## Tag and publish

- [ ] Tag: `git tag v<version>`
- [ ] Push tag: `git push origin v<version>`
- [ ] Verify CI publish succeeds (GitHub Actions)

## Post-release

- [ ] Verify PyPI page renders correctly: `https://pypi.org/project/jsrc/`
