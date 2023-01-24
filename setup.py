from setuptools import setup, find_packages

setup(
    name="pyuavcan_v0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    version='1.0.35',
    install_requires=[
        'importlib-metadata; python_version == "3.2"',
    ],
)
