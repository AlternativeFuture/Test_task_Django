from django.urls import path
from . import views


urlpatterns = [
    path("", views.all_item),
    path("<int:item_id>", views.get_item_data),
    path("create/", views.create_item),
    path("del_item/<int:item_id>", views.del_item),
]
