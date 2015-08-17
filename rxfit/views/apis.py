from django.http import HttpResponse
from django.http import JsonResponse



def login(request):
    if request.method == 'GET':
        return do_login_get(request)
    elif request.method == 'POST':
        return do_login_post(request)
    else :
        return HttpResponse('{name="zhangsan",age=20,method="None"}')

def do_login_get(req):
    if 'type' in req.GET :
        if req.GET['type'] == 'json':
            print('json')
            return JsonResponse({'name':"zhangsan",'age':20,'method':'get','type':'json'})
        elif req.GET['type'] == 'xml' :
            return HttpResponse('<xml version="1.0"><name>zhangsan</name></xml>')
    else :
        return HttpResponse('{name="zhangsan",age=20,method="get"}')
def do_login_post(req):
    return HttpResponse('{name="zhangsan",age=20,method="post"}')