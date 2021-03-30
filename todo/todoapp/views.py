from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm, ItemUpdateForm


def all_item(request):
    item = Item.objects.all()
    context = {"item": item}

    return render(request, "all_item.html", context)


def get_item_data(request, item_id):
    item = Item.objects.get(id=item_id)
    context = {"item": item}

    return render(request, 'item_data.html', context)


def update_item(request, item_id):
    item = Item.objects.get(id=item_id)

    if request.method == "POST":
        form = ItemUpdateForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ItemUpdateForm(instance=item)

    context = {"form": form}

    return render(request, "update_item.html", context)


def create_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ItemForm()

    context = {"form": form}

    return render(request, "create_item.html", context)


def del_item(request, item_id):
    item = Item.objects.get(id=item_id)
    item.delete()

    return redirect('/')
