from setuptools import find_packages, setup


with open('README.md') as readme_file:
    readme = readme_file.read()


with open('CHANGELOG.md') as changelog_file:
    changelog = changelog_file.read()

version = '2.6.0'

setup(
    name='django-pgcrypto-fields',
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    version=version,
    python_requires='>=3.12',
    license_expression='BSD-2-Clause',
    description='Encrypted fields for Django dealing with pgcrypto postgres extension.',
    long_description=readme + '\n\n' + changelog,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Framework :: Django :: 5.2',
        'Framework :: Django :: 6.0',
        'Framework :: Django :: 6.1',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
        'Programming Language :: Python :: 3.15',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Database',
        'Topic :: Security :: Cryptography',
    ],
    author='Incuna Ltd',
    author_email='admin@incuna.com',
    url='https://github.com/incuna/django-pgcrypto-fields',
)
