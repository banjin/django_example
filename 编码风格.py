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



# models 文件编码规范(顺序)
# > 1. 字段
# > 2. 自定义managers属性
# > 3 class Meta 定义
# > 4 __str__方法
# > 5 def save 方法
# > 6 def get_absolute_url 方法
# > 7 其他方法定义


# 3.3 自带venv模块以后创建虚拟环境
python3 -m venv project-env
sourceproject-env/bin/activite
deactivate


# 通用项目结构

project
    |__ LICENSE
    |__ MANIFEST.in
    |__ README.md
    |__ conf/   # 部署使用的nginx,supervisor等配置
    |__ fabfile/
    |__ others/
    |__ requirements.txt
    |__ setup.py  # 用来打包项目
    |__ src/

# django 项目目录结构

project
  |_project(src)
    |__ app1
    |__ app2
    |__ project
        |__settins
            |____init__.py
            |__base.py
            |__develop.py
            |__product.py
    |__ manage.py
