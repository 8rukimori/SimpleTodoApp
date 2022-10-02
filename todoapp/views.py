from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Todo
from django.urls import reverse_lazy

#modelをインポート

#Class-based viewで作成(Djangoで用意されているListViewクラスを継承)
class TodoList(ListView):
    template_name = 'list.html' #テンプレートファイルの位置を上書きする
    model = Todo

class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = Todo

class TodoCreate(CreateView):
    template_name = 'create.html'
    model = Todo
    fields = ('title', 'memo', 'priority', 'due_date')
    success_url = reverse_lazy('list')

class TodoDelete(DeleteView):
    template_name = 'delete.html'
    model = Todo
    success_url = reverse_lazy('list')

class TodoUpdate(UpdateView):
    template_name = 'update.html'
    model = Todo
    fields = ('title', 'memo', 'priority', 'due_date')
    success_url = reverse_lazy('list')