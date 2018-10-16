from django.shortcuts import render
from lists.models import Item

def home_page(request):
    return render(request, 'home.html', {
        'new_item_text': request.POST.get('item_text', ''),
    })
