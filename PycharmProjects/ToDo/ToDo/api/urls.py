from django.conf.urls import url, include

from ToDo.ToDoList import views

urlpatterns = [
    url('', views.ListTodo.as_view()),
    url('<int:pk>/', views.DetailTodo.as_view()),
    url('rest-auth/', include('rest_auth.urls'))
]