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
    # Check if there are any words in the session
    if 'words' not in request.session or not request.session['words']:
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'message': 'Game over', 'game_over': True})
        return redirect('game_over')

    word_list = request.session['words']
    current_word = random.choice(word_list)

    if request.method == 'POST':
        answer = request.POST.get('answer')
        correct_word = request.POST.get('correct_word')

        if str(answer).strip().lower() == correct_word.lower():
            request.session['score'] += 1
            message = "Correct"
        else:
            message = f"Incorrect, the right word is {correct_word}"

        request.session['total'] += 1
        request.session['words'].remove(current_word)

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            if request.session['words']:
                new_word = random.choice(request.session['words'])
                return JsonResponse({
                    'message': message,
                    'correct_translation': correct_word,
                    'new_word': {
                        'translation': new_word['translation'],
                        'word': new_word['word']
                    }
                })
            else:
                return JsonResponse({'message': 'Game over', 'game_over': True})

    return render(request, 'play_game.html', {'word': current_word})


def game_over(request):
    score = request.session.get('score', 0)
    total = request.session.get('total', 1)
    return render(request, 'game_over.html', {'score': score, 'total': total})


def reset_game(request):
    request.session.flush()
    return redirect('start_game')
