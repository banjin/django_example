#!/usr/bin/env python

import sys
import os

from app import simple_app


def wsgi_to_bytes (s): 
    return s.encode()


def run_with_cgi(application):
    environ = dict(os.environ.items()) 
    environ ['wsgi.input'] = sys.stdin.buffer 
    environ['wsgi.errors'] =sys.stderr 
    environ['wsgi.version'] = (1, 0)
    environ['wsgi.multithread'] = False 
    environ['wsgi.multiprocess'] = True
    environ['wsgi.run_once'] = True
    if environ.get('HTTPS', 'off') in ('on','1'): 
        environ['wsgi.url_scheme'] = 'https'
    else:
        environ['wsgi.url_scheme']='http'

    headers_set = [] 
    headers_sent = []

    def write(data) :
        out = sys.stdout.buffer
        if not headers_set :
            raise AssertionError ("write () before start_response ()”)
        elif not headers sent:
            #在输 出 第一行数据之前，允发送响应头
            status , response_headers = headers_sent[:] = headers_set
            out.write(wsgi_to_bytes('Status: %s\r\n' % status))
            for header in response_headers :
                out.write(wsgi_to_bytes('%s: %s\r\n' % header))
            out.write(wsgi_to_bytes ('\r\n'))
        out.write(data) 
        out.flush()
    
    def start_response(status, response_headers, exc_info=None):
        """
        回调函数，设置response状态和header
        """
        if exc_info:
            try:
                if headers sent:
                    #如果已经发送了 header，则重新抛出原始异常信息
                    raise (exc_info[0], exc_info[1] , exc info[2])
            finally:
                exc_info = None #避免循环引用
        elif headers set:
            raise AssertionError("Headers already set ! ”)
        headers_set[:] = [status, response_headers] 
        return write

    result = application(environ, start_response)
    try:
        for data in result:
            if data:
                write(data)
        if not headers_sent:
            write('')
    finally:
        if hasattr(result, 'close'):
            result.close()


if __name__ == "__main__":
    run_with_cgi(simple_app)
