import configparser
import os

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), "../config.ini"))

def get_config_value(key):
    return config['DEFAULT'][key]

def get_bool_value(key):
    return config['DEFAULT'].getboolean(key)

def get_float_value(key):
    return config['DEFAULT'].getfloat(key)