#在views.py中，後端Django 自動會為我們把這個類別中的設定對應到資料庫系統中
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post        #先將在models.py 中自己所定義的function引入
from datetime import datetime

def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request,'index.html',locals())

def showpost(request,slug):
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            return render(request,'post.html',locals())
    except:
        return redirect('/')    #發生找不到文章的情況時的例外處理，直接返回首頁



'''
def homepage(request):       #設計一個迴圈，將此資料夾中的內容用for取出，並透過HttpResponse()輸出到網頁上
    posts = Post.objects.all()
    post_lists = []
    for count, post in enumerate(posts):
        post_lists.append("No.{}: {}".format(count, post))
        post_lists.append("<hr>")
        post_lists.append("<small>{}</small><br></br>".format(post.body))
    
    content = '\n'.join(post_lists)  # 将列表中的内容连接为字符串
    
    # 创建响应对象并设置正确的编码
    response = HttpResponse(content, content_type='text/html; charset=utf-8')
    
    return response

'''