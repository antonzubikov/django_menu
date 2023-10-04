from django.shortcuts import render
from .models import MenuItem


def menu_view(request):
    return render(request, 'menu/menu.html', {'menu_items': MenuItem.objects.all()})
