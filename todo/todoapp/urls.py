from django.urls import path
from . import views


urlpatterns = [
    path("", views.all_item, name="to do list"),
    path("<int:item_id>", views.get_item_data, name="item data"),
    path("create/", views.create_item, name="create item"),
    path("del_item/<int:item_id>", views.del_item, name="delete item"),
    path("update_item/<int:item_id>", views.update_item, name="update item"),
]
