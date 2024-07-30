from django.shortcuts import render
from django.views import View
from .models import Blog
from .helpers import Pagination
# Create your views here.
class BlogView(View):
    def get(self, request):
        page = int(request.GET.get('page', 1))
        blogs = Blog.get_query_set()
        pages = Pagination.page_pagination(blogs, 3, page)
        return render(request, 'blog.html', context={'pages':pages, 'page':page, 'previous_page': page-1, 'next_page': page+1})