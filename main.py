"""Sample application exercising requests, urllib3, Jinja2, and PyYAML."""

import sys

import requests
import yaml
from jinja2 import Template


def load_config(path="config.yaml"):
    with open(path) as f:
        return yaml.safe_load(f)


def render_greeting(name):
    template = Template("Hello, {{ name }}! Welcome to the sample app.")
    return template.render(name=name)


def fetch_status(url):
    response = requests.get(url, timeout=5)
    return response.status_code


def main():
    config = load_config()

    print(render_greeting(config.get("user_name", "World")))

    url = config.get("check_url", "https://example.com")
    try:
        status = fetch_status(url)
        print(f"Checked {url}: HTTP {status}")
    except requests.RequestException as exc:
        print(f"Failed to reach {url}: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
