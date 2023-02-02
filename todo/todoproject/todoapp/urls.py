from django.urls import path

from . import views

urlpatterns = [
    path('', views.demo,name='demo'),
    path('delete/<int:taskid>/',views.delete,name='deleted'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('cbvtodo/', views.tasklistview.as_view(), name='cbvtodo'),
    path('cbvdetails/<int:pk>/', views.taskdetailview.as_view(), name='cbvdetails'),
    path('cbvupdate/<int:pk>/', views.taskupdate.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.taskdelete.as_view(), name='cbvdelete'),

#     here views.tasklist.as.view() because its a function tasklist not like a normal functio

]