#主要負責定義要存取的資料模型，都用class來定義
from django.db import models
from django.utils import timezone

#設計一個用來儲存文章的資料表，格式欄位那些都要自己定義
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)   #文章網址
    body = models.TextField()                 #文章內容
    pub_date = models.DateField(default=timezone.now)    #本文發表時間

    class Meta:                    #指定文章順序是以pub_date為依據
        ordering = ('-pub_date',)

    def __str__(self):             #提供此類別所產生的資料項目，一個以文章標題當作顯示的內容，增加操作可讀性
        return self.title