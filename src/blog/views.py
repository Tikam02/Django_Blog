from django.shortcuts import render



def blog_home(request):
    return render(request,'blog_index.html',{})

def blog(request):
    return render(request,'blog.html',{})

def post(request):
    return render(request,'blog/post.html',{})
