# Aiffel korean tokenizer

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PyPi license](https://badgen.net/pypi/license/pip/)](https://pypi.org/project/aiffel-korean-tokenizer/)
[![PyPI version fury.io](https://badge.fury.io/py/ansicolortags.svg)](https://pypi.org/project/aiffel-korean-tokenizer/)
<br>

## File Tree

```
.
├─── aiffel_korean_tokenizer
│   ├─── __init__.py
│   └─── tokenizer.py
│
├─── LICENSE
├─── setup.cfg
├─── setup.py
└─── README.md
```

## Quick usage

This module requires Mecab. You need to download Mecab in local.

```python 
import os

os.system('apt-get update')
os.system('apt-get install g++ openjdk-8-jdk python-dev python3-dev')
os.environ['JAVA_HOME'] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.system("curl -s -L https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh | bash")
os.system('pip3 install /tmp/mecab-python-0.996')
```

<br>
After download Mecab, you can use this module as tokenizer.


```console
pip install aiffel-korean-tokenizer
```

<br>

You can add stopwords in instance.


And the rest of the usage is all the same as Keras tokenizer.

```python 
from aiffel_korean_tokenizer.tokenizer import Korean_tokenizer

stopwords = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다']

korean_tokenizer = Korean_tokenizer(stopwords=stopwords)
korean_tokenizer.fit_on_texts(texts)
```
