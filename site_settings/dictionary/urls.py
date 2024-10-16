from django.urls import path

from . import views

urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("words/", views.words_table_page, name="words_page"),
    path('init_play/', views.start_game, name="start_game"),
    path('play/', views.play_game, name='play_game'),
    path('gameover/', views.game_over, name='game_over'),
    path('reset/', views.reset_game, name='reset_game'),
]
