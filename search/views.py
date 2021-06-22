from django.shortcuts import redirect, render
from .models import SearchQuery
from blog.models import BlogPost

def search_view(request):
    search_query = request.GET.get('q')
    if len(search_query.strip()) == 0:
        return redirect('/')

    user = None
    if request.user.is_authenticated:
        user = request.user

    SearchQuery.objects.create(user=user, query=search_query)
    blog_list = BlogPost.objects.search(search_query)
    context = {'query': search_query, 'object_list': blog_list}
    return render(request,'search/view.html',context)
