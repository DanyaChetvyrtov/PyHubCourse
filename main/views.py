from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': 'Home',
        'content': 'Main page of the shop - HOME',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'bool': True
    }
    return render(request, 'main/index.html', context)


def about(request):
    return render(request, 'about.html')
