import os

import pytest

import confile

SAMPLE_CONFIG_DIR = os.path.join(os.path.dirname(__file__), 'sample_configs')


class TestIniConfig(object):

    @classmethod
    def setup_class(cls):
        config_path = os.path.join(SAMPLE_CONFIG_DIR, 'test.ini')
        cls.config = confile.IniConfig(config_path)

    def test_get_string_value(self):
        value = self.config.get_property('test', 'string')
        assert type(value) is str
        assert value == 'string'

    def test_get_int_value(self):
        value = self.config.get_property('test', 'int')
        assert type(value) is int
        assert value == 0

    def test_get_float_value(self):
        value = self.config.get_property('test', 'float')
        assert type(value) is float
        assert value == 0.0

    def test_get_date(self):
        value = self.config.get_property('test', 'date')
        assert type(value) is str
        assert value == '2001-01-23'

    def test_get_boolean_true(self):
        value = self.config.get_property('test', 'boolean_true')
        assert type(value) is bool
        assert value is True

    def test_get_boolean_false(self):
        value = self.config.get_property('test', 'boolean_false')
        assert type(value) is bool
        assert value is False

    def test_get_list(self):
        value = self.config.get_property('test', 'list')
        assert type(value) is list
        assert value == ['a', 'b', 'c']

    def test_get_dict(self):
        value = self.config.get_property('test', 'dict')
        assert type(value) is dict
        assert value == {'a': 1, 'b': 2, 'c': 3}

    def test_get_unknown_section(self):
        value = self.config.get_property('unknown_section')
        assert value is None

    def test_get_unknown_key(self):
        value = self.config.get_property('test', 'known_key')
        assert value is None

    def test_get_default_section(self):
        assert self.config.get_property('test', 'default_string') == 'default_string'
        assert self.config.get_property('test', 'default_int') == 1
        assert self.config.get_property('test', 'default_float') == 1.0
        assert self.config.get_property('test', 'default_date') == '1999-12-31'


class TestJsonConfig(object):

    @classmethod
    def setup_class(cls):
        config_path = os.path.join(SAMPLE_CONFIG_DIR, 'test.json')
        cls.config = confile.JsonConfig(config_path)

    def test_get_string_value(self):
        value = self.config.get_property('test', 'string')
        assert type(value) is str
        assert value == 'string'

    def test_get_int_value(self):
        value = self.config.get_property('test', 'int')
        assert type(value) is int
        assert value == 0

    def test_get_float_value(self):
        value = self.config.get_property('test', 'float')
        assert type(value) is float
        assert value == 0.0

    def test_get_date(self):
        value = self.config.get_property('test', 'date')
        assert type(value) is str
        assert value == '2001-01-23'

    def test_get_boolean_true(self):
        value = self.config.get_property('test', 'boolean_true')
        assert type(value) is bool
        assert value is True

    def test_get_boolean_false(self):
        value = self.config.get_property('test', 'boolean_false')
        assert type(value) is bool
        assert value is False

    def test_get_list(self):
        value = self.config.get_property('test', 'list')
        assert type(value) is list
        assert value == ['a', 'b', 'c']

    def test_get_dict(self):
        value = self.config.get_property('test', 'dict')
        assert type(value) is dict
        assert value == {'a': 1, 'b': 2, 'c': 3}

    def test_get_unknown_section(self):
        value = self.config.get_property('unknown_section')
        assert value is None

    def test_get_unknown_key(self):
        value = self.config.get_property('test', 'known_key')
        assert value is None


class TestYamlConfig(object):

    @classmethod
    def setup_class(cls):
        config_path = os.path.join(SAMPLE_CONFIG_DIR, 'test.yml')
        cls.config = confile.YamlConfig(config_path)

    def test_get_string_value(self):
        value = self.config.get_property('test', 'string')
        assert type(value) is str
        assert value == 'string'

    def test_get_int_value(self):
        value = self.config.get_property('test', 'int')
        assert type(value) is int
        assert value == 0

    def test_get_float_value(self):
        value = self.config.get_property('test', 'float')
        assert type(value) is float
        assert value == 0.0

    def test_get_date(self):
        value = self.config.get_property('test', 'date')
        assert type(value) is str
        assert value == '2001-01-23'

    def test_get_boolean_true(self):
        value = self.config.get_property('test', 'boolean_true')
        assert type(value) is bool
        assert value is True

    def test_get_boolean_false(self):
        value = self.config.get_property('test', 'boolean_false')
        assert type(value) is bool
        assert value is False

    def test_get_list(self):
        value = self.config.get_property('test', 'list')
        assert type(value) is list
        assert value == ['a', 'b', 'c']

    def test_get_dict(self):
        value = self.config.get_property('test', 'dict')
        assert type(value) is dict
        assert value == {'a': 1, 'b': 2, 'c': 3}

    def test_get_unknown_section(self):
        value = self.config.get_property('unknown_section')
        assert value is None

    def test_get_unknown_key(self):
        value = self.config.get_property('test', 'known_key')
        assert value is None


def test_read_config_ini_file():
    config_file = os.path.join(SAMPLE_CONFIG_DIR, 'test.ini')

    assert type(confile.read_config(config_file)) is confile.IniConfig


def test_read_config_json_file():
    config_file = os.path.join(SAMPLE_CONFIG_DIR, 'test.json')

    assert type(confile.read_config(config_file)) is confile.JsonConfig


def test_read_config_yaml_file():
    config_file = os.path.join(SAMPLE_CONFIG_DIR, 'test.yml')

    assert type(confile.read_config(config_file)) is confile.YamlConfig


def test_read_config_unknown_ext():
    config_file = os.path.join(SAMPLE_CONFIG_DIR, 'test.ini')

    with pytest.raises(TypeError):
        confile.read_config(config_file, 'conf')
