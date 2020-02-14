from django.urls import path
from . import views

urlpatterns = [
    path('base',views.base),
    path('add',views.add),
    path('delete',views.delete),
    path('todos/',views.todos),

]