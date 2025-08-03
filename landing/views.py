from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

# Create your views here.

def landing_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your interest! We\'ll be in touch soon.')
            return redirect('landing_page')
    else:
        form = ContactForm()
    
    return render(request, 'landing/landing_page.html', {'form': form})
