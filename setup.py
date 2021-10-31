from setuptools import setup, find_namespace_packages

setup(
    name='Game of life simulation',
    packages=find_namespace_packages(include=['game_of_life_simulation_package']),
  #  install_requires=['PyQt5>=5.15.6'],  # for some reason installing QT5 with setuptool doesn't work properly
)