from django.shortcuts import HttpResponseRedirect
from django.urls import resolve

def simple_middelware(get_respons):
     def middelware(reqeust):
          url_name = resolve(reqeust.path_info).url_name
          if reqeust.user.is_authenticated:
               # response = HttpResponseRedirect('login')
               response = get_respons(reqeust)
               
          else:
               response = get_respons(reqeust)
          return response
     return middelware


class Simplemiddelware:
     def __init__(self,get_respons):
          self.get_response = get_respons
     def __call__(self,reqeust):
          url_name = resolve(reqeust.path_info).url_name
          if reqeust.user.is_authenticated:
               # response = HttpResponseRedirect('login')
               response = self.get_response(reqeust)
               
          else:
               response = self.get_response(reqeust)
          return response