from setuptools import setup

setup(
    name='mining_control',
    version='0.0.1',
    description='A package that stops mining when the python program starts and restart mining when the python '
                'program exit',
    url='https://github.com/Entropy-xcy/mining_control',
    author='Entropy Xu',
    author_email='entropy.xuceyu@gmail.com',
    license='BSD 2-clause',
    packages=['mining_control'],
    install_requires=['docker'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3'
    ],
)
