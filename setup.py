from setuptools import setup, find_packages
 
setup(
    name='django-coutries',
    version='0.1.3',
    description='Provides fixtures and models for a "complete" list of world countries',
    author='Fredrik Sjöblom',
    url='http://code.google.com/p/django-countries/',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools'],
    setup_requires=['setuptools_git'],
)