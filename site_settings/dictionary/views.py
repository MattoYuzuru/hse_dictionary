from django.shortcuts import render

from .models import Word


def main_page(request):
    return render(request, 'main_page.html')


def words_table_page(request):
    words = Word.objects.all()

    context = {
        "words": words,
    }

    return render(request, 'words_page.html', context)


def learning_game_page(request):
    return render(request, 'game_page.html')
