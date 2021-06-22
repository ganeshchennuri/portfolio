from django.db.models import query
from django.shortcuts import get_object_or_404, redirect, render
from .forms import BlogPostForm
from .models import BlogPost
from django.views.generic import ListView
from django.contrib.admin.views.decorators import staff_member_required

def index(request):
    return render(request,'index.html')

def blogs_list_view(request):
    """
    function based list View
    """
    queryset = BlogPost.objects.all().published()
    if request.user.is_authenticated:
        my_queryset = BlogPost.objects.filter(user=request.user)
        queryset = (queryset | my_queryset).distinct()
    context = {'object_list': queryset}
    return render(request, 'blog/list.html', context)

'''
class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog/list.html'
    # ordering = ['-date_created']
    # context_object_name = 'blogs' #default object_list

    # Search => BlogPost.objects.filter(title__icontains='hello')
'''
# @login_required
@staff_member_required
def blog_post_create_view(request):
    # template_name = 'blog/create.html'
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('/blog')
        else:
            print(form.errors)

    form = BlogPostForm()
    context = {'title':'Create BlogPost', 'form': form}
    return render(request,'blog/create.html',context)

def blog_post_detail_view(request,slug):
    obj = get_object_or_404(BlogPost,slug=slug)
    template_name = 'blog/detail.html'
    context ={'title':obj.title, 'object': obj}
    return render(request,template_name,context)

@staff_member_required
def blog_post_update_view(request,slug):
    obj = get_object_or_404(BlogPost,slug=slug)
    form = BlogPostForm(instance=obj)
    context ={
        'title':f'Update BlogPost {obj.title}', 
        'form': form,
        'object': obj
    }
    if request.method == 'POST':
        form = BlogPostForm(request.POST,request.FILES, instance=obj)
        if form.is_valid():
            obj = form.save()
            return redirect('/blog')
        else:
            print(form.errors)
    return render(request,'blog/edit.html',context)

@staff_member_required
def blog_post_delete_view(request,slug):
    obj = get_object_or_404(BlogPost,slug=slug)
    template_name = 'blog/delete.html'
    context_dict ={'title':obj.title}
    if request.method == 'POST':
        obj.delete()
        return redirect('/blog')
    return render(request,template_name,context_dict)