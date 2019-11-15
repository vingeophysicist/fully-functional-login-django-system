from __future__ import unicode_literals
from django.db import models
from django.utils.timezone import now
from django.contrib.auth import get_user_model
import json
from django.utils.text import slugify



class Category(models.Model):
    category = models.CharField(max_length=250)
    
    
    class Meta:
        verbose_name = ("Subject")
        verbose_name_plural = ("Subjects")

    def __str__(self):
        return self.category

class Quiz(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField("Description", help_text=("a description of the quiz"))
    url = models.SlugField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Category")
    single_attempt = models.BooleanField(blank=False, default=False)
    draft = models.BooleanField(blank=True, default=False)

    def save(self, *args, **kwargs):
        self.url = slugify(self.title)
        super(Quiz, self).save(*args, **kwargs)
 
    class Meta:
        verbose_name = ("Quiz")
        verbose_name_plural = ("Quizzes")

    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, blank=True, null=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)
    question_text = models.TextField(blank=False)
    
    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"
        ordering = ['category']

    def __str__(self):
        return self.question_text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='Answers')
    text_answers = models.CharField("Answers text", max_length=1000)
    correct = models.BooleanField("Correct", default=False, blank=False)

    
    def __str__(self):
        return self.text_answers

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"


class Candidate(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    start = models.DateTimeField(verbose_name="Start", auto_now_add=True)
    end = models.DateTimeField(verbose_name="End", null=True, blank=True)




    







    






