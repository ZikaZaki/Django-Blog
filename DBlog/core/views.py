from .models import Core
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class IndexView(ListView):
    model = Core
    template_name = 'core/index.html'
    context_object_name = 'index'


class SingleView(DetailView):
    model = Core
    template_name = 'core/single.html'
    context_object_name = 'post'


class PostsView(ListView):
    model = Core
    template_name = 'core/posts.html'
    context_object_name = 'post_list'


class AddView(CreateView):
    model = Core
    # fields = ['name']
    template_name = 'core/add.html'
    fields = '__all__'
    success_url = reverse_lazy('core:posts')


class EditView(UpdateView):
    model = Core
    template_name = 'core/edit.html'
    fields = '__all__'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('core:posts')


class DeleteView(DeleteView):
    model = Core
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('core:posts')
    template_name = 'core/confirm-delete.html'
