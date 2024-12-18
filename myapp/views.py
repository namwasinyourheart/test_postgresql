from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Item

def item_list(request):
    items = list(Item.objects.values())
    return JsonResponse(items, safe=False)
