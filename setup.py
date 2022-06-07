from setuptools import setup, find_packages

setup(
    name                = 'aiffel_korean_tokenizer',
    version             = '0.0.0.3',
    description         = 'aiffel_korean_tokenizer for node',
    author              = 'seegong',
    url                 = 'https://github.com/Finerestaurant/pip_distribute_demo',
    install_requires    =  ['tensorflow', 'konlpy','JPype1'],
    license='MIT',
    packages            = find_packages(exclude = []),
    keywords            = ['aiffel'],
    python_requires     = '>=3',
    package_data        = {},
    zip_safe            = False,
    classifiers         = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)