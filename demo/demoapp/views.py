from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail

#from Demo.settings import EMAIL_HOST_USER
from demoapp.forms import ContactForm

# Create your views here.
def index(request):
    return render (request, 'index.html', {'page':'home'})

def about(request):
    return render (request, 'about.html', {'page':'about'})

def send_mail(contact_form_data):
    email_message_format = 'name: %s\nemail: %s\nMessage: %s\n'
    name     = contact_form_data.get('name','')
    messages = contact_form_data.get('message','')
    email    = contact_form_data.get('email')
    email_message_format = email_message_format % (name, email, message)
    send_mail('Demo Website', email_message_format, EMAIL_HOST_USER, [EMAIL_HOST_USER], fail_silenty=False,)

def contact_us(request):
    #try:
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_email(form.cleaned_data)
            message.success(request,'your response has been recorded')
    else:
        form = ContactForm()
    #except:
        #messages.error(request,'contact.html',{'page':'contact','form':form})
    return render(request, 'contact.html',{'page':'contact','form':form})
def clear(request):
    form = ContactForm()
    messages.error(request, 'Fields cleared successfully')
    return render(request, 'contact.html',{'page':'contact','form':form})
