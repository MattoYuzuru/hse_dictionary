from django.shortcuts import render

from .models import Word


def main_page(request):

    words = Word.objects.all()

    # for word in words:
        # print(word)
    # print('\n', words[0].translation)

    context = {
        "words": words,
    }

    return render(request, 'main_page.html', context)
