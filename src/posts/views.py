from django.db.models import Count,Q
from django.core.paginator import  Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Post
from marketing.models import  Signup


def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)

        ).distinct()

    context = {
        'queryset' : queryset
    }
    return  render(request, 'search_result.html', context)

def get_category_count():
    queryset = Post\
        .objects\
        .values('categories__title')\
        .annotate(Count('categories__title'))
    return queryset


def blog_home(request):
    featured = Post.objects.filter(featured=True)
    latest   = Post.objects.order_by('-timestamp')[0:3]


    if request.method == 'POST':
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()




    context = {
               'objects_list':featured,
               'latest':latest
               }
    return render(request,'blog_index.html',context)

def blog(request):
    category_count = get_category_count()
    most_recent = Post.objects.order_by('-timestamp')[:3]
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 2)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset =  paginator.page(paginator.num_pages)
    context = {
        'queryset': paginated_queryset,
        'most_recent': most_recent,
        'page_request_var':page_request_var,
        'category_count':category_count
    }
    return render(request,'blog.html',context)

def post(request, id):
    return render(request,'blog/post.html',{})

def contact(request):
    return render(request,'blog/contact.html',{})
