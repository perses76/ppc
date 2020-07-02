from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='ppc',
    version='0.1.0',
    description='Python Programming Challenge',
    long_description=readme,
    author='Vadim Ovcearenco',
    author_email='wadim@veles-soft.com',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    python_requires='>=3.6',
    install_requires=['pandas', 'mysql-connector-python', 'attr', 'django', 'mysqlclient'],
    extras_require={
        'dev': ['pytest']
    }
)
