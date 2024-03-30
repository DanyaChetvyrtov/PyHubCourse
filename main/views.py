from django.shortcuts import render
from goods.models import Categories

# Create your views here.
def index(request):
    categories = Categories.objects.all()

    context = {
        'title': 'Home - главная',
        'content': 'Магазин мебели HOME',
        'categories': categories
    }
    
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст о том, почему этот магазин такой классный, и какой хороший тут товар.',
    }
    return render(request, 'main/about.html', context)
