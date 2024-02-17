from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.cache import never_cache

from .models import *
from django.contrib import messages


# Create your views here.

def toLogin_view(request):
    return render(request, '登录页面.html')


# @login_required
def Login_view(request):
    u = request.POST.get('user', '')
    p = request.POST.get('pwd', '')

    if u and p:
        c = Account.objects.filter(username=u, password=p).count()
        if c >= 1:
            return redirect('main_page')
            # return redirect('main_page')
            # return HttpResponse("登录成功！")
        else:
            # return HttpResponse("账号密码错误！")
            error_message = "请输入正确的账号和密码！"
            return render(request, '登录页面.html', {'error_message': error_message})
    else:
        return HttpResponse("请输入正确的账号和密码！")


def toregister_view(request):
    return render(request, '注册.html')


def register(request):
    u = request.POST.get('user', '')
    p = request.POST.get('pwd', '')

    if u and p:
        acc = Account(username=u, password=p)
        acc.save()
        return HttpResponse("注册成功！")
    else:
        return HttpResponse("请输入完整的账号和密码！")


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # 检查用户名是否已存在
        if Account.objects.filter(username=username).exists():
            messages.error(request, '该用户名已被使用')
            # return render(request, '登录页面.html')
            return redirect('/accounts/toregister/')  # 重定向到注册页面，并显示错误消息

        # 创建新用户记录
        new_user = Account(username=username, password=password)
        new_user.save()

        messages.success(request, '注册成功！')
        return redirect('/accounts/')  # 重定向到登录页面，或者其他你希望的页面


def main_page(request):
    # 主页面
    return render(request, '首页.html')


def get_worldgeopark_data(request):
    # 从数据库中获取Worldgeopark数据
    worldgeopark_data = Worldgeopark.objects.all().values('name', 'longitude', 'latitude')

    # 将数据转换为JSON格式并返回给前端
    return JsonResponse(list(worldgeopark_data), safe=False)


def manage_page(request):
    return render(request, 'manage.html')


def add_page(request):
    return render(request, 'add.html')

@never_cache
def search_page(request):
    return render(request, 'search.html')


def detele_page(request):
    return render(request, 'detele.html')


def list_page(request):
    return render(request, 'list.html')


def add_worldgeopark(request):
    if request.method == 'POST':
        # 获取表单提交的数据
        name = request.POST.get('name')
        address = request.POST.get('address')
        protect = request.POST.get('protect')
        scene = request.POST.get('scene')

        # 创建 Worldgeopark 对象并保存到数据库
        worldgeopark = Worldgeopark(
            name=name,
            address=address,
            protect=protect,
            scene=scene
        )
        worldgeopark.save()

        # 重定向到成功页面或其他页面
        return redirect('success_page')


def success_page(request):
    return render(request, 'success.html')


def delete_worldgeopark(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')

        # 使用 filter() 获取查询集
        worldgeopark_queryset = Worldgeopark.objects.filter(name=name)

        # 检查是否至少有一个对象
        if worldgeopark_queryset.exists():
            # 删除查询集中的所有匹配对象
            worldgeopark_queryset.delete()

    return redirect('success_page')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # 检查用户名是否已存在
        if Account.objects.filter(username=username).exists():
            messages.error(request, '该用户名已被使用')
            return redirect('register')  # 重定向到注册页面，并显示错误消息

        # 创建新用户记录
        new_user = Account(username=username, password=password)
        new_user.save()

        messages.success(request, '注册成功！')
        return redirect('login')  # 重定向到登录页面，或者其他你希望的页面

    return render(request, 'register.html')  # 渲染注册页面



@never_cache
def search_result(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        if name:
            # 非空名称，执行查询
            results = Worldgeopark.objects.filter(name__icontains=name)
            if results.exists():
                print("ok")
                return render(request, 'result.html', {'results': results})
            else:
                # 查询结果为空，传递搜索条件到搜索页面
                print("notok")
                return render(request, 'search.html', {'searched_name': name, 'not_found': True})

    # 如果是 GET 请求或其他情况，可以添加适当的处理
    return redirect('search_page')  # 这里假设你有名为 'search_page' 的 URL 配置

@never_cache
def result_page(request):
    return render(request, 'result.html')

def all_page(request):
    return render(request, 'all.html')

def all2_page(request):
    return render(request, 'all2.html')

def all3_page(request):
    return render(request, 'all3.html')