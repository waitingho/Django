from django.shortcuts import render
from datetime import datetime
from .models import Article
def index (request):
    context = {
        'current_date':datetime.now(),
        'title':'食蟻獸ㄉ穴'
    }
    return render(request, 'index.html',context)

def about(request):
    context = {
        'current_date':datetime.now(),
        'title':'About'
    }
    return render(request, 'about.html',context)

def news(request):
    populate_db()
    article = get_articles()

    context = {
        'articles':article,
        'current_date':datetime.now(),
        'title':'News'
    }
    return render(request,'news.html',context)

def get_articles():
    result = Article.objects.all()
    return result

def populate_db():
    if Article.objects.count() == 0:
        Article(title = 'first item',content = 'this is the first db item').save()
        Article(title = 'second item',content = 'this is the second db item').save()
        Article(title = 'third item',content = 'this is the third db item').save()