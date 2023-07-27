from django.contrib import admin
from django.urls import include, path
from mainsite.views import homepage,showpost


urlpatterns = [
    path('admin/', admin.site.urls),  #將Django的管理介面添加到你的網站中，並將'admin/'路徑與管理介面相關聯。
    path('', homepage, name='root'),  #將根路徑對應到 views.py 中的 index 視圖函式，並使用名稱 'root' 
                                #來識別該路由。當你訪問根路徑時，Django 將呼叫 index 函式，並顯示相應的內容。
    path('post/<slug:slug>/',showpost),    #把所有post/開頭的網址後面的字串都找出來，當作第二個參數(第一個預設為request)，傳遞給showpost處理
                             
]