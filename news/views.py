from django.shortcuts import render


def archive_handler(request):
    context = {}
    return render(request, 'newstest/archive.html', context)


def category_handler(request):

    context = {}
    return render(request, 'newstest/category.html', context)


def contact_handler(request):
    context = {}
    return render(request, 'newstest/contact.html', context)


def index_handler(request):
    context = {}
    return render(request, 'newstest/index.html', context)


def blog_handler(request):
    context = {}
    return render(request, 'newstest/blog.html', context)


def robots_handler(request):
    context = {}
    return render(request, 'newstest/robots.txt', context, content_type='text/plain')
