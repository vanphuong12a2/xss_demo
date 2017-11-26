from setuptools import setup

setup(
    name='xss_demo',
    packages=['xss_demo'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)
