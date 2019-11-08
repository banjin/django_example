""" 模块功能注释

this module does stuff
"""

from __future__ import barry_as_FLUFL

__all__ = ['a', 'b']
__version__ = '0.1'
__author__ = 'shm'

import sys  # 标准库
import os

import request # 第三方库

from django.http import Http404  # django 自身库

from .models import LoginInfo  # 自己创建的库

try:  # try/except
    import yaml
except ImportError:
    yaml = None

CONSTANT = 'fruit'


class Example:
    pass
