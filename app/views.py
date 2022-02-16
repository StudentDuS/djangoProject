from django.shortcuts import render, HttpResponse, redirect
import requests


# Create your views here.
def index(request):
    return HttpResponse('欢迎使用')


def user_list(request):
    return render(request, "user_list.html")  # 在app中的templates文件夹中寻找


def user_add(request):
    return render(request, "user_add.html")


def tpl(request):
    name = '小杜'
    roles = ["管理员", "CEO", "保安"]
    user_info = {"name": "小杜", "salary": 10000, "role": "CTO"}
    data_list = [
        {"name": "小杜", "salary": 20000, "role": "CTO"},
        {"name": "小王", "salary": 10000, "role": "CFO"},
        {"name": "小李", "salary": 30000, "role": "CEO"},
    ]
    return render(request, 'tpl.html', {"n1": name, "n2": roles, "n3": user_info, "n4": data_list})


# 定义自己的新闻页面
def news(req):
    res = requests.get("http://www.chinaunicom.com.cn/api/pv/updatePv")
    data_list = res.json()
    # print(data_list)
    return render(req, "news.html")


#
def something(request):
    # request是一个对象，封装了用户发过来的所有请求相关的数据
    # 获取请求方式
    print(request.method)
    return HttpResponse('欢迎使用')


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    if request.method == "POST":
        username = request.POST.get("user")
        password = request.POST.get("pwd")
        if username == "root" and password == "123":
            return redirect("https://www.bilibili.com/?spm_id_from=333.788.0.0")
        else:
            return render(request, 'login.html', {"error_msg": "用户名或密码输入错误"})
