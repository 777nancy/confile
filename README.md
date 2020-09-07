# confile: config file reader

## Description

Confile is a simple config file reader.  
`ini`, `json` and `yaml` formats are supported.

## Installation

To install confile, use pip.
```bash
pip install confile
```

## Usage

following file is sample config file called `sample.json`.

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

>>> config.to_dict()
{'db': {'host': 'localhost', 'port': 5432, 'user': 'user', 'password': 'password'}}
```

## Documentation

Confile’s documentation is [here](https://777nancy.github.io/confile/).