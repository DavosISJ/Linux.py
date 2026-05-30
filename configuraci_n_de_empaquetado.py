from setuptools import setup, find_packages

setup(
    name='linux-baremetal',
    version='1.0.0',
    description='Acceso puro a hardware de Linux (Bare-Metal).',
    author='Davos Vision',
    packages=find_packages(),
    python_requires='>=3.8',
    classifiers=[
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
    ],
)