from tokenize import group
from urllib import request
from django.shortcuts import HttpResponse, redirect

def unauthenticated_user(view_func):
    def warpper_func(request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('blog-home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def full_access(allowed_roles=[]):
    def decotrator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = none    
            
            return view_func(request, *args, **kwargs)
        return wrapper_func
    return decotrator