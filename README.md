# setup-openapi

[![version](https://badgen.net/github/release/remarkablemark/setup-openapi)](https://github.com/remarkablemark/setup-openapi/releases)
[![test](https://github.com/remarkablemark/setup-openapi/actions/workflows/test.yml/badge.svg)](https://github.com/remarkablemark/setup-openapi/actions/workflows/test.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

🟢 Set up GitHub Actions workflow with [OpenAPI Generator CLI](https://openapi-generator.tech/docs/installation/).

This action installs Java, downloads the OpenAPI Generator CLI JAR, caches it by version, and exposes a binary on `PATH`.

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

Generate a Ruby client from an [OpenAPI spec](https://petstore3.swagger.io/):

```yaml
- run: openapi-generator-cli generate -i petstore.yaml -g ruby -o /tmp/test/
```

See [action.yml](action.yml)

## Inputs

### `version`

**Optional**: The OpenAPI Generator CLI version. Defaults to [7.21.0](https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/7.21.0/).

```yaml
- uses: remarkablemark/setup-openapi@v1
  with:
    version: 7.21.0
```

### `name`

**Optional**: The OpenAPI Generator CLI binary name. Defaults to `openapi-generator-cli`.

```yaml
- uses: remarkablemark/setup-openapi@v1
  with:
    name: openapi-generator-cli
```

## License

[MIT](LICENSE)
