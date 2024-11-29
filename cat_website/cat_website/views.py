from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Cat
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.http import HttpResponse


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


def product_view(request, product_id):
    # current_cake = CustomCake.objects.get(id=1)
    cat = get_object_or_404(Cat, id=product_id)
    return render(request, 'cat.html', {'cat': cat})


def product_list(request):
    cats = Cat.objects.all()
    return render(request, 'cats_list.html', {'cats': cats})


@login_required
def home(request):
    return render(request, 'main.html')


def logout_now(request):
    # return HttpResponse('<h1>Вы вышли из аккаунта</h1>')
    return render(request, 'logout_now.html')

def how_help(request):
    return HttpResponse('<img src="templates/default.png" alt="Не удалось загрузить изображение."></img><p>Контакты - +7 000 000 00 00.</p>')


def about_us(request):
    return HttpResponse('<h3>Это сайт - приют для кошек.</h3><p>Форма для записи - Имя, Фамилия, Номер телефона.</p>')
