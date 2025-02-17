from django.urls import path
from .views import (
note_list,
note_create,
note_update,
note_delete,
)

urlpatterns = [
    path('', note_list, name='note_list'),
    path('note/new/', note_create, name='note_create'),
    path('update/<int:pk>/', note_update, name='note_update'),
    path('delete/<int:pk>/', note_delete, name='note_delete'),
]
