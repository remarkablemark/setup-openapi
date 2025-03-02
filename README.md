# github-actions-composite-template

[![version](https://badgen.net/github/release/remarkablemark/github-actions-composite-template)](https://github.com/remarkablemark/github-actions-composite-template/releases)
[![test](https://github.com/remarkablemark/github-actions-composite-template/actions/workflows/test.yml/badge.svg)](https://github.com/remarkablemark/github-actions-composite-template/actions/workflows/test.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

⚙️ GitHub Actions Composite Template. Inspired by [remarkablemark/hello-world-composite-action](https://github.com/remarkablemark/hello-world-composite-action).

## Quick Start

```yaml
# .github/workflows/github-actions-composite-template.yml
on: push
jobs:
  github-actions-composite-template:
    runs-on: ubuntu-latest
    steps:
      - name: GitHub Actions Composite Template
        uses: remarkablemark/github-actions-composite-template@v1
```

## Usage

**Basic:**

```yaml
- uses: remarkablemark/github-actions-composite-template@v1
```

See [action.yml](action.yml)

## Inputs

### `version`

**Optional**: The version. Defaults to `1.2.3`:

```yaml
- uses: remarkablemark/github-actions-composite-template@v1
  with:
    version: 1.2.3
```

## Contributions

Contributions are welcome! 👋

## License

[MIT](LICENSE)
