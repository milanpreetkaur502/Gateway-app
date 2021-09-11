import sys
from setuptools import setup
setup(
    name = "gatewayManager",
    version = "1.0",
    author="ScratchNest",
    author_email = "info@scratchnest.com",
    description = "Python module for implementing BLE IoT gateway application",
    keywords= ["Bluetooth","BLE","IoT","IoT gateway"],
    packages=["src"],
    package_data={
        'src': ['mydatabasenew.db']
    },
)
