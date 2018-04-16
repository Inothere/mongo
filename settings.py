# coding: utf-8
import os

SETTINGS_ROOT = os.path.dirname(__file__)
INPUT = os.path.join(SETTINGS_ROOT, 'input')
PARSE_OUTPUT = os.path.join(SETTINGS_ROOT, 'output')

DATABASES = {
    'host': '192.168.56.109',
    'port': 27017,
    'name': 'security'
}

if not os.path.isdir(PARSE_OUTPUT):
    os.mkdir(PARSE_OUTPUT)
