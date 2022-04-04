from django.shortcuts import render

# Create your views here.
from formapp.forms import ContactForm, SnippetForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm (request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            print(name, email)
    form = ContactForm()
    return render(request,'contact.html', {'form' : form})


def snippet_detail(request):
    print('INVALID')
    if request.method == 'POST':
        print('May be valid')
        form = SnippetForm(request.POST)
        if form.is_valid():
            print('VALID')
            form.save()
    form = SnippetForm()
    return render(request,'contact.html', {'form' : form})






