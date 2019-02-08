#!python

from setuptools import setup

setup(
    name='uart MQTT gateway',
    version='0.0.1',
    description='uart MQTT gateway',
    author='Josef Janda',
    author_email='josef.janda@gmail.com',
    license='MIT',
    scripts=[
        'uart-mqtt.py',
    ],
    packages=['uart_utils'],
    install_requires=['pyserial', 'paho-mqtt', 'argparse']
)
