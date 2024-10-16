from django import forms

from .models import Word


class TopicForm(forms.Form):
    topics = forms.MultipleChoiceField(
        choices=[(topic, topic) for topic in Word.objects.values_list('topic', flat=True).distinct()],
        widget=forms.CheckboxSelectMultiple
    )
