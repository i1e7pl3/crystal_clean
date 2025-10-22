from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import OrderForm

def index(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False) 
            order.creator = request.user 
            order.save()
            messages.success(request, 'Ваша заявка успешно отправлена!')
            return redirect('homepage:index')
    else:
        form = OrderForm()
    return render(request, 'homepage/index.html', {'form': form})
