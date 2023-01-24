from setuptools import setup
import pyuavcan_v0.version as version

setup(
    name="pyuavcan_v0",
    packages=["pyuavcan_v0", "pyuavcan_v0.app", "pyuavcan_v0.driver", "pyuavcan_v0.dsdl"],
    version=version.__version__,
    install_requires=[
        'importlib-metadata; python_version == "3.2"',
    ],
)
