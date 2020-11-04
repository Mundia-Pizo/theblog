from django.shortcuts import render
from django.views.generic import ListView
from .models import Article


class  ArticleListView(ListView):
    model = Article
    template_name = 'core/article_list.html'
