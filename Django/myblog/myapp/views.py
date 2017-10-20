from django.shortcuts import render
from django.shortcuts import redirect
from . import models
import math

def index(request):
    size_per_page = 3
    count = models.Article.objects.count()
    count2 = math.ceil(count/size_per_page)

    page_num = int(request.GET.get('page', '1'))
    page_num = 1 if page_num < 1 else page_num
    page_num = count2 if page_num >count2 else page_num

    start = size_per_page * (page_num - 1)
    end = start + size_per_page

    articles = models.Article.objects.order_by("-add_temptime")[start:end]

    return render(request, 'index.html', {'articles': articles, 'count': count, 'count2':count2, 'pr': range(1,count2+1), 'page_num': page_num})

def article_page(request, article_id):
    article = models.Article.objects.get(pk = article_id)
    return render(request, 'article_page.html', {'article': article})

def edit_page(request, article_id):
    if str(article_id) == '0':
        return render(request, 'edit_page.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'edit_page.html', {'article': article})

def edit_action(request):
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    article_id = request.POST.get('article_id', '0')

    if article_id == '0':
        models.Article.objects.create(title=title, content=content)
        articles = models.Article.objects.all()
        return render(request, 'index.html', {'articles': articles})

    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()
    return redirect('/index/article/' + article_id)

def delete_action(request):
    article_id = request.POST.get('article_id', '0')
    article = models.Article.objects.get(pk=article_id)
    article.delete()
    articles = models.Article.objects.all()
    return render(request, 'index.html', {'articles': articles})
