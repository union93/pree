from django.shortcuts import render
from django.db.models import Q
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView, FormMixin
from django.views.generic.detail import DetailView
from django.views.generic import FormView
from django.shortcuts import render,get_object_or_404,redirect
from .models import Community

class CommunityList(ListView):
    model = Community
    paginate_by = 10
    template_name_suffix = '_list'
    context_object_name = 'community_lsit'

    def get_queryset(self):
        community_list = Community.objects.order_by('-id')
        return community_list

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

class CommunityCreate(CreateView):
    model = Community
    fields = ['title', 'text', 'image']
    template_name_suffix = '_create'
    success_url = '/community'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/community')
        else:
            return self.render_to_response({'form': form})

class CommunityDelete(DeleteView):
    model = Community
    template_name_suffix = '_delete'
    success_url = '/community'

class CommunityUpdate(UpdateView):
    model = Community
    context_object_name = 'update_community'
    fields = ['title', 'text', 'image']
    template_name_suffix = '_update'
    success_url = '/community'

    def get_object(self):
        update_community = get_object_or_404(Community, pk=self.kwargs['pk'])
        return update_community

class CommunityDetail(DetailView):
    model = Community
    template_name_suffix = '_detail'

def Communitysearch(request):
    communitys = Community.objects.all().order_by('-id')
    template_name_suffix = '_search'
    q = request.POST.get('q', "")

    if q:
        communitys = communitys.filter(Q(title__icontains=q) or Q(text__icontains=q) or Q(author__icontains=q)).distinct()
        return render(request, 'community/community_search.html', {'communitys': communitys, 'q': q})
    #필터 넣기 제목, 제목+작성자, 글내용
    else:
        return render(request, 'community/community_search.html')
