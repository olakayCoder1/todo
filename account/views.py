from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages
from client.models import TodoItem
from client.forms import TodoForm
from .forms import  CustomUserCreationForm
from django.utils.http import urlsafe_base64_encode ,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str
from .tokens import get_token
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.conf import settings
from .models import AccountActivation
# Create your views here.

def register(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            if User.objects.filter(email = form.cleaned_data['email']).count():
                messages.error(request, 'EMAIL ALREADY EXIST')
                return redirect('register')
            #ACTIVATION EMAIL SETUP CONFIG
            ''''
            user = form.save(commit=False)               
            user.is_active = False 
            token = get_token()
            new_tok = AccountActivation(active_token=token)
            new_tok.save()
            user_mail= request.POST['email']
            print(user_mail)
            template = render_to_string('account/confirm-mail.html', {'usern': user ,
                'uid': urlsafe_base64_encode(force_bytes(user.id)),
                'token': token, 'domain': get_current_site(request)
                })
            verification_mail = EmailMessage(
                    settings.SITE_NAME,
                    template,
                    to=[ user_mail]
                )
            verification_mail.send()


            '''
            form.save()
            messages.success(request, 'YOUR ACCOUNT HAS BEEN CREATED. YOU CAN NOW LOGIN')
            return redirect('/account/login/')

        print(form.errors)

    return render(request, 'account/register.html', {'form':form})


'''''
def activate_account(request, uidb64 , token ):
    try:  
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    check_token = AccountActivation.objects.filter(active_token=token)
    if user is not None and check_token.count():  
        user.is_active = True  
        user.save()  
        return redirect('login/')  
    else:  
        return HttpResponse('Activation link is invalid!') 


        '''