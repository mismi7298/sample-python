# sample-python

A minimal sample project: [main.py](main.py) loads [config.yaml](config.yaml) with PyYAML, renders a greeting with Jinja2, and checks a URL's status with requests (which pulls in urllib3).

## Run

```
pip install -r requirements.txt
python main.py
```

## Intentionally vulnerable dependencies

The pinned versions below are outdated on purpose, each with a known CVE fixable by bumping to the listed patch/minor version — useful for testing SCA/dependency scanners.

| Package  | Pinned  | CVE             | Fixed in |
|----------|---------|-----------------|----------|
| requests | 2.19.1  | CVE-2018-18074  | 2.20.0   |
| urllib3  | 1.24.1  | CVE-2019-11324  | 1.24.2   |
| Jinja2   | 2.10    | CVE-2019-10906  | 2.10.1   |
| PyYAML   | 5.3     | CVE-2020-1747   | 5.3.1    |

To remediate, bump each dependency in [requirements.txt](requirements.txt), [setup.py](setup.py), and [pyproject.toml](pyproject.toml) to the "Fixed in" version.
