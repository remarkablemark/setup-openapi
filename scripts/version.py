#!/usr/bin/env python3

import os
import re
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path


MAVEN_METADATA_URL = "https://repo.maven.apache.org/maven2/org/openapitools/openapi-generator-cli/maven-metadata.xml"

ROOT_DIR = Path(__file__).resolve().parent.parent
ACTION_FILE = ROOT_DIR / "action.yml"
README_FILE = ROOT_DIR / "README.md"


def get_latest_version() -> str:
    with urllib.request.urlopen(MAVEN_METADATA_URL) as response:
        metadata = response.read()

    root = ET.fromstring(metadata)
    release = root.findtext("./versioning/release")
    if not release:
        raise RuntimeError("Unable to get latest OpenAPI Generator CLI version")

    return release


def get_current_version() -> str:
    action_text = ACTION_FILE.read_text(encoding="utf-8")
    match = re.search(r"default:\s+([0-9]+(?:\.[0-9]+)*)", action_text)

    if not match:
        raise RuntimeError(f"Unable to get current version in {ACTION_FILE}")

    return match.group(1)


def main() -> None:
    current_version = get_current_version()
    latest_version = get_latest_version()
    github_output = os.environ.get("GITHUB_OUTPUT")

    if github_output:
        with open(github_output, "a", encoding="utf-8") as file:
            file.write(f"current_version={current_version}\n")
            file.write(f"latest_version={latest_version}\n")

    action_text = ACTION_FILE.read_text(encoding="utf-8")
    action_text = action_text.replace(
        f"default: {current_version}",
        f"default: {latest_version}",
        count=1,
    )
    ACTION_FILE.write_text(action_text, encoding="utf-8")

    readme_text = README_FILE.read_text(encoding="utf-8")
    readme_text = readme_text.replace(current_version, latest_version)
    README_FILE.write_text(readme_text, encoding="utf-8")

    print(
        f"Updated OpenAPI Generator CLI version from {current_version} to {latest_version}"
    )


if __name__ == "__main__":
    main()
