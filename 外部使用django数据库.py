#！/usr/bin/env python
# coding:utf-8

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.pardir))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Project.settings")

import django
django.setup()


# 导入数据库

def write_data():
   pass

if __name__=='__main__':
    write_data()