# confile: config file reader

## Description

confile is a simple config file reader.  
`ini`, `json` and `yaml` formats are supported.

## Installation

To install confile. use pip.
```bash
pip install confile
```

## Usage

```json
{
  "db": {
    "host": "localhost",
    "port": 1234,
    "user": "user",
    "password": "password"
  }
}
```
```python
>>> import confile

>>> config = confile.read_config('sample.json')

>>> config.get_property('db', 'host')
'localhost'

>>> config.get_property('db', 'port')
1234

>>> config.get_property('db')
{'host': 'localhost', 'port': 5432, 'user': 'user', 'password': 'password'}
```