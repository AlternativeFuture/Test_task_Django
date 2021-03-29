from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Item
from .forms import ItemForm


def all_item(request):
    item = Item.objects.all()
    return render(request, "all_item.html", {"item": item})


def get_item_data(request, item_id):
    item = Item.objects.get(id=item_id)
    return render(request, 'item_data.html', {'item': item})


def create_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item_obj = form.save()
            item_obj.save()
            return HttpResponseRedirect('/')
    else:
        form = ItemForm()
    return render(request, "create_item.html", {"form": form})


def del_item(request, item_id):
    item = Item.objects.get(id=item_id)
    item.delete()
    return HttpResponseRedirect('/')

