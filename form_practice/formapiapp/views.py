from django.shortcuts import render,redirect
from . forms import contactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings
# Create your views here.
def form(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            subject = 'Contact'
            body = {
                'first_name': form.cleaned_data['first_name'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            
            print("Sending email...")  # Debug print

            try:
                send_mail(
                    subject,
                    message,
                    'your-email@example.com',  # Replace with a valid sender email
                    ['aliakbartutul749@gmail.com'],
                    fail_silently=False,
                )
                print("Email sent successfully!")  # Debug print
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('home')

    else:
        form = contactForm()

    return render(request, 'index.html', {'form': form})