# setup-openapi

[![version](https://badgen.net/github/release/remarkablemark/setup-openapi)](https://github.com/remarkablemark/setup-openapi/releases)
[![test](https://github.com/remarkablemark/setup-openapi/actions/workflows/test.yml/badge.svg)](https://github.com/remarkablemark/setup-openapi/actions/workflows/test.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

⚙️ Set up GitHub Actions workflow with [OpenAPI Generator](https://openapi-generator.tech/docs/installation/).

## Quick Start

```yaml
# .github/workflows/openapi.yml
on: push
jobs:
  openapi:
    runs-on: ubuntu-latest
    steps:
      - name: Setup OpenAPI
        uses: remarkablemark/setup-openapi@v1

      - name: Generate Ruby Client
        run: openapi-generator-cli generate -i petstore.yaml -g ruby -o /tmp/test/
```

## Usage

Install OpenAPI Generator CLI tool:

```yaml
- uses: remarkablemark/setup-openapi@v1
```

Generate a Ruby client from a valid [petstore.yaml](https://petstore3.swagger.io/) doc:

```yaml
- run: openapi-generator-cli generate -i petstore.yaml -g ruby -o /tmp/test/
```

See [action.yml](action.yml)

## Inputs

### `version`

**Optional**: The OpenAPI Generator version. Defaults to latest.

```yaml
- uses: remarkablemark/setup-openapi@v1
  with:
    version: 7.9.0
```

## License

[MIT](LICENSE)
