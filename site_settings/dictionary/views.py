import random

from django.http import JsonResponse
from django.shortcuts import render, redirect

from .forms import TopicForm
from .models import Word


def main_page(request):
    return render(request, 'main_page.html')


def words_table_page(request):
    words = Word.objects.all()
    return render(request, 'words_page.html', {"words": words})


def start_game(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            selected_topics = form.cleaned_data['topics']
            words = Word.objects.filter(topic__in=selected_topics)
            request.session['words'] = list(words.values('id', 'word', 'translation'))
            request.session['score'] = 0
            request.session['total'] = 0
            return redirect('play_game')
    else:
        form = TopicForm()

    return render(request, 'start_game.html', {'form': form})


def play_game(request):
    if 'words' not in request.session or not request.session['words']:
        return redirect('game_over')

    word_list = request.session['words']

    if request.method == 'POST':
        answer = request.POST.get('answer')
        correct_word = request.POST.get('correct_word')

        if str(answer).strip().lower() == correct_word.lower():
            request.session['score'] += 1
            message = "Correct"
        else:
            message = "Incorrect"

        request.session['total'] += 1

        word_list = [word for word in word_list if word['word'] != correct_word]
        request.session['words'] = word_list

        if not word_list:
            return JsonResponse({'game_over': True})

        new_word = random.choice(word_list)

        return JsonResponse({
            'message': message,
            'correct_translation': correct_word,
            'new_word': new_word,
            'game_over': False
        })

    if request.method == 'GET':
        if not word_list:
            return redirect('game_over')

        current_word = random.choice(word_list)
        return render(request, 'play_game.html', {'word': current_word})


def game_over(request):
    score = request.session.get('score', 0)
    total = request.session.get('total', 1)
    return render(request, 'game_over.html', {'score': score, 'total': total})


def reset_game(request):
    request.session.flush()
    return redirect('start_game')
