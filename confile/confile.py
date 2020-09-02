import ast
import configparser
import json
import os
from abc import ABCMeta
from abc import abstractmethod

import yaml


class NoDatesSafeLoader(yaml.SafeLoader):
    @classmethod
    def remove_implicit_resolver(cls):

        if 'yaml_implicit_resolvers' not in cls.__dict__:
            cls.yaml_implicit_resolvers = cls.yaml_implicit_resolvers.copy()

        for first_letter, mappings in cls.yaml_implicit_resolvers.items():
            cls.yaml_implicit_resolvers[first_letter] = [(tag, regexp)
                                                         for tag, regexp in mappings
                                                         if tag != 'tag:yaml.org,2002:timestamp']


class BaseConfig(metaclass=ABCMeta):

    @abstractmethod
    def get_property(self, key, *keys):
        pass

    @abstractmethod
    def to_dict(self):
        pass


class IniConfig(BaseConfig):

    def __init__(self, config_path, encoding=None, default_section='DEFAULT'):
        self._default_section = default_section
        self._config_dict = {}
        self._has_default_section = False
        parser = configparser.ConfigParser(default_section=None)
        parser.read(config_path, encoding)

        for section in parser.sections():
            if section == default_section:
                self._has_default_section = True
            section_dict = {}
            for key, value in parser.items(section):
                try:
                    value = ast.literal_eval(value)
                except (SyntaxError, ValueError):
                    pass
                section_dict[key] = value

            self._config_dict[section] = section_dict

    def get_property(self, section, key=None):

        section_dict = self._config_dict.get(section)

        if key and section_dict is not None:
            value = section_dict.get(key)

            if value is None and self._has_default_section:
                value = self._config_dict.get(self._default_section).get(key)

            return value
        else:
            return section_dict

    def to_dict(self):

        return self._config_dict


class SerializedConfig(BaseConfig):

    def __init__(self, config_path, file_type, encoding=None):
        file_type = file_type.lower()
        with open(config_path, encoding=encoding) as fin:
            if file_type == 'json':
                self._config_dict = json.load(fin)
            elif file_type in ['yml', 'yaml']:
                NoDatesSafeLoader.remove_implicit_resolver()
                self._config_dict = yaml.load(fin, Loader=NoDatesSafeLoader)
            else:
                raise TypeError('Unknown file type {}'.format(file_type))

    def get_property(self, key, *keys):

        if type(self._config_dict) is list:
            return None

        sub_config_dict = self._config_dict.get(key)

        if keys and sub_config_dict is not None:
            for k in keys:
                value = sub_config_dict.get(k)
                if value is None:
                    return None
                sub_config_dict = value
            return sub_config_dict
        else:
            return sub_config_dict

    def to_dict(self):

        return self._config_dict


class JsonConfig(SerializedConfig):

    def __init__(self, config_path, encoding=None):
        super().__init__(config_path, 'json', encoding)


class YamlConfig(SerializedConfig):

    def __init__(self, config_path, encoding=None):
        super().__init__(config_path, 'yaml', encoding)


def read_config(config_path, file_type=None, encoding=None, default_section=None):
    if file_type is None:
        _, ext = os.path.splitext(config_path)
        file_type = ext[1:]
    file_type = file_type.lower()

    if file_type == 'ini':
        return IniConfig(config_path, encoding, default_section)
    elif file_type == 'json':
        return JsonConfig(config_path, encoding)
    elif file_type in ['yml', 'yaml']:
        return YamlConfig(config_path, encoding)
    else:
        raise TypeError('Unknown file type {}'.format(file_type))
