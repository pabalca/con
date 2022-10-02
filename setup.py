from setuptools import setup

setup(
    name="con",
    version=1.0,
    packages=["con"],
    install_requires=["click"],
    entry_points={"console_scripts": ["con = con.cli:cli"]},
)
