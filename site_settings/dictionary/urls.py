from django.urls import path
from . import views


urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("words/", views.words_table_page, name="words_page"),
    path("learn/", views.learning_game_page, name="game_page"),
]