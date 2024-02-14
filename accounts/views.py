from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import *


# Create your views here.

def toLogin_view(request):
    return render(request, '登录页面.html')

#@login_required
def Login_view(request):
    u = request.POST.get('user', '')
    p = request.POST.get('pwd', '')

    if u and p:
        c = Account.objects.filter(username=u, password=p).count()
        if c >= 1:
            return redirect('main_page')
            #return redirect('main_page')
            # return HttpResponse("登录成功！")
        else:
            #return HttpResponse("账号密码错误！")
            error_message = "请输入正确的账号和密码！"
            return render(request, '登录页面.html', {'error_message': error_message})
    else:
        return HttpResponse("请输入正确的账号和密码！")


def toregister_view(request):
    return render(request, 'register.html')


def register_view(request):
    u = request.POST.get('user', '')
    p = request.POST.get('pwd', '')

    if u and p:
        acc = Account(username=u, password=p)
        acc.save()
        return HttpResponse("注册成功！")
    else:
        return HttpResponse("请输入完整的账号和密码！")



def main_page(request):
    # 主页面
    return render(request, 'try.html')

def main(request):
    return render(request, 'main.html')

def get_worldgeopark_data(request):
    # 从数据库中获取Worldgeopark数据
    worldgeopark_data = Worldgeopark.objects.all().values('name', 'longitude', 'latitude')

    # 将数据转换为JSON格式并返回给前端
    return JsonResponse(list(worldgeopark_data), safe=False)