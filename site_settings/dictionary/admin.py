from django.contrib import admin
from .models import Word



class WordAdmin(admin.ModelAdmin):
    list_display = ('id', 'word', 'translation', 'topic')


admin.site.register(Word, WordAdmin)
