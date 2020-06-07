#!/usr/bin/env python

def simple_app(environ, start_response):
    '''
    simple web application
    '''

    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return [b'hello world -by me \n']



class AppClass(object):
    """
    类结构的application
    """
    status = ’200 OK’
    response_headers = [('Content-type','text/plain')]
    def __call__ (self, environ, start_response): 
        print(en.viron, start_response) 
        start_response(self.status, self response headers) 
        return [b'Hello AppClass.__call__\n']
application = AppClass()



from queue import Queue