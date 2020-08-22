from distutils.log import Log
from time import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView, FormMixin
from django.views.generic.detail import DetailView
from django.views.generic import FormView
from post.forms import PostSearchForm, CreatePost
from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import date, datetime

class PostTodayList(ListView):
    model = Post
    paginate_by = 5
    template_name_suffix = '_today'
    today = date.today()
    start_date = datetime.strptime(str(today.year) + " " + str(today.month) + " " + str(today.day), '%Y %m %d')
    #datetime.strptime(str(today.year) + " " + str(today.month) + " " + str(today.day), '%Y %m %d')

    def get_queryset(self, today=today):
        post_list = Post.objects.all().filter(created__year = today.year, created__month = today.month, created__day = today.day)
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

class PostMonthList(ListView):
    model = Post
    paginate_by = 5
    template_name_suffix = '_month'
    today = date.today()

    def get_queryset(self, today=today):
        post_list = Post.objects.all().filter(created__year = today.year, created__month = today.month)
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
    context_object_name = 'update_post'
    fields = ['title', 'text', 'image']
    template_name_suffix = '_update'
    success_url = '/'

    def get_object(self):
        update_post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return update_post


class PostDelete(DeleteView):
    model = Post
    template_name_suffix = '_delete'
    success_url = '/'

class PostDetail(DetailView):
    model = Post
    template_name_suffix = '_detail'

class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name_suffix = '_search'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        post_list = Post.objects.filter(Q(title__icontains=searchWord) |
                                        Q(text__icontains=searchWord) | Q(author__icontains=searchWord)).distinct()
        # Q객체: filter메소드의 매칭 조건을 다양하게 해줌
        #icontatins연산자: 대소문자를 구분하지 않고 단어가 포함되어있는지 검사 ,  distinct메소드: 중복된개체 검사
        context ={}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = post_list

        return render(self.request, self.template_name, context) #no redirection

def search(request):
    posts = Post.objects.all().order_by('-id')
    template_name_suffix = '_search'
    q = request.POST.get('q', "")

    if q:
        posts = posts.filter(Q(title__icontains=q) or Q(text__icontains=q) or Q(author__icontains=q)).distinct()
        return render(request, 'post/post_search.html', {'posts': posts, 'q': q})
    #필터 넣기 제목, 제목+작성자, 글내용
    else:
        return render(request, 'post/post_search.html')

