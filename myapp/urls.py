from django.urls import path
from . import views

urlpatterns = [  # Corregido: urlpatterns
    path('', views.index),
    path('about/', views.about),  # No es necesario poner "/" al inicio del segundo argumento
    path('projects/', views.projects),  # No es necesario poner "/" al inicio del segundo argumento
    path('tasks/', views.tasks),
    path('form/', views.form),
    path('task/<int:id>', views.task)
]
