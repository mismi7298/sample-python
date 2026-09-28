from setuptools import setup

setup(
    name="sample-python",
    version="0.1.0",
    description="Sample Python project for dependency vulnerability scanning",
    py_modules=["main"],
    install_requires=[
        "requests==2.34.2",
        "urllib3==1.24.1",
        "Jinja2==2.10",
        "PyYAML==5.3",
    ],
    entry_points={
        "console_scripts": [
            "sample-app=main:main",
        ],
    },
)
