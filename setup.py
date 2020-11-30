#! /usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


setup(
    name='OpenFisca-canada',
    version='12.0.0',
    author='Government of Canada, Digital Technology Solutions - Solutions de technologies numériques',
    author_email='michael.bungay@hrsdc-rhdcc.gc.ca,tjharrop@gmail.com',
    description=u'OpenFisca tax and benefit system for Canada',
    keywords='benefit microsimulation social tax',
    license='http://www.fsf.org/licensing/licenses/agpl-3.0.html',
    url='https://github.com/DTS-STN/openfisca-canada-dts',
    include_package_data=True,  # Will read MANIFEST.in
    install_requires=[
        'OpenFisca-Core == 34.8.0',
        ],
    extras_require={
        'test': [
            'flake8 >=3.4.0,<3.7.0',
            'flake8-print',
            'nose',
            'yamllint'
            ]
        },
    packages=find_packages(),
    test_suite='nose.collector',
    )
