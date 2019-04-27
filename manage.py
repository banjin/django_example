#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_example.settings")
    # 通过读取系统环境变量中的 DJANGO_EXAMPLE_PROF工LE django加载不同的 settings文件
    profile = os.environ.get('DJANGO_EXAMPLE_PROF工LE' , 'develop')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',"django_example.settings.%s" % profile)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
