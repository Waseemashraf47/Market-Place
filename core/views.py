from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignupForm
# Create your views here.


def index (request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render (request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact (request):
    return render (request, 'core/contact.html')

def signup(requset):
    if requset.method == 'POST':
        form = SignupForm(requset.POST)
        if form.is_valid():
            form.save()
            
            return redirect('/login/')
    else:    
        form = SignupForm()
        return render (requset, 'core/signup.html', {
            'form': form
        })
