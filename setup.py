from setuptools import setup, find_packages

setup(
    name                = 'aiffel_text_classifier',
    version             = '0.1',
    description         = 'aiffel_text_classifier',
    author              = 'seegong',
    url                 = 'https://github.com/Finerestaurant/pip_distribute_demo',
    download_url        = 'https://github.com/jeakwon/ccpy/archive/0.0.tar.gz',
    install_requires    =  ['tensorflow', 'matplotlib', 'tqdm', 'konlpy','JPype1'],
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