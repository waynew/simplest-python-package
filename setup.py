from setuptools import setup, find_packages

setup(
    name='myproj',
    version='0.1.0',
    packages=find_packages(),
    entry_points='''
        [console_scripts]
        myproj=myproj.__main__:run
    ''', 
    install_requires=[
    ],
    tests_require=[
    ],
)
