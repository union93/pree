from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Post
from django.shortcuts import redirect

class PostList(ListView):
    model = Post
    paginate_by = 5
    template_name_suffix = '_list'
    context_object_name = 'post_lsit'

    def get_queryset(self):
        post_list = Post.objects.order_by('-id')
        return post_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5
        max_index = len(paginator.page_range)
        page = self.request.GET.get('page')
        current_page = int(page) if page else 1
        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range

        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range

        return context

class PostCreate(CreateView):
    model = Post
    fields = ['title', 'text', 'image']
    template_name_suffix = '_create'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form': form})


class PostUpdate(UpdateView):
    model = Post
    fields = ['text', 'image']
    template_name_suffix = '_update'
    success_url = '/'

class PostDelete(DeleteView):
    model = Post
    template_name_suffix = '_delete'
    success_url = '/'

class PostDetail(DetailView):
    model = Post
    template_name_suffix = '_detail'
