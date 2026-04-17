from django.urls import path
from .views import *

urlpatterns = [
    path('',post_list,name='home'),
    path('<int:post_id>/',detail,name='detail'),
    path('add/',create,name='add'),
    path('<int:post_id>/edit',edit,name='edit'),
    path('<int:post_id>/delete',delete,name='delete'),
    
]
