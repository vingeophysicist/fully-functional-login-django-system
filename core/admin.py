from django.contrib import admin
from .models import Category, Quiz, Question, Candidate, Answer


admin.site.register(Category)
admin.site.register(Quiz)



class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    fields = ['question_text', 'category', 'quiz']
    inlines = [AnswerInline]

class QuizAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Question, QuestionAdmin)






