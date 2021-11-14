from django.shortcuts import render
from .forms import ContactForm


def contact(request):
    # Check to see if request is a POST
    # if this is a POST request, we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # print (form.cleaned_data['email']) # for example,email can be accessed using form.cleaned_data['email']
            form.save()
            # redirect to a new URL:
            return render(request, 'contact/thanks.html')
        else:
            # Form data is not valid
            # You can generate an error message to inform the user
            form = ContactForm()
            context = {'form': form, 'error_message': 'The data entered is not valid!'}
            return render(request, 'contact/contact.html', context)
    else:
        # if the request is not a POST (e.g., for the first time, page is loaded)
        # we'll create a blank form and render the page with the form
        form = ContactForm()
        context = {'form': form}
        return render(request, 'contact/contact.html', context)
