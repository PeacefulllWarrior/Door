from django.urls import path
from .views import *

app_name = 'shop'
urlpatterns = [
    path('', main, name='main'),
    path('model/<int:model_id>/', modelview, name='model'),
    path('add_comment/', add_comment, name='add_comment'),
    path('edit_commet/<int:comment_id>/', edit_comment, name='edit_comment')
]