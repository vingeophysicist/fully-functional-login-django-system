from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from core.forms import SignUpForm
from .models import Category, Quiz
from django.views.generic import DetailView

@login_required
def home(request):
    count = User.objects.count()
    category_list = Category.objects.all()
    return render( request, 'home.html', {'category_list':category_list})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form })

@login_required
def secret_page(request):
    return render(request, 'secret_page.html',)

class QuizDetailView(DetailView):
    model = Quiz
    slug_field = 'url'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        
        context = self.get_context_data(object=self.object)
        return self.render_to_response("qiuz_detail.html")





