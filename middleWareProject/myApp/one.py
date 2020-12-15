from django.shortcuts import render
from django.http import HttpResponse

class SimpleMdiddleWare:
    def __init__(self, get_response):
        self.get_response=get_response

    def __call__(self, request):
        print("Preprocessing the request")
        response=self.get_response(request)
        print(response)
        print("Post processing the response")
        return response

    def process_exception(self, request, exception):
        return HttpResponse('Exception')