from django.shortcuts import render
from .forms import ContactForm
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message'] 
            return render(request, "formsapp/success.html", {"name": name})
    else:
        form = ContactForm()
    return render(request, 'formsapp/contact.html', {'form': form})
