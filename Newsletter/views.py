from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives
from django.template import loader
from .models import Newsletter

# Create your views here.



## TEMPLATE MAIL

def index(request):
    if request.method == 'POST':
        
        email = request.POST['user_email']
        subscribe = Newsletter(email = email)
        subscribe.save()
            
       
        
        template = loader.get_template('pages/contact_form.txt')
       
        context = {
         'user_email': email,
        }
        
        message = template.render(context)
        
        email = EmailMultiAlternatives(
            'Welcome To VEEPAY Telecom 💙', message,
            'VEEPAY <veepay.ng@gmail.com>', [email]  
        )
        
        #converting the text file to html
        
        email.content_subtype = 'html'
        
        #sending the email
        email.send()
      
        # message to be printed out on the terminal       
        print( 'Subscription Successful')
        
        # where to redirect to after sending mail
        return redirect ('success/')
    
    return render(request, 'pages/index.html')
    
   
   
   
   
# def index(request):
#     if request.method == 'POST':
        
#         email = request.POST['user_email']
#         subscribe = Newsletter(email = email)
#         subscribe.save()
            
       
        
#         template = loader.get_template('pages/contact_form.txt')
       
#         context = {
#          'user_email': email,
#         }
        
#         message = template.render(context)
        
#         email = EmailMultiAlternatives(
#             'Welcome To VEEPAY Telecom 💙', message,
#             'VEEPAY <veepay.ng@gmail.com>', [email]  
#         )
        
#         #converting the text file to html
        
#         email.content_subtype = 'html'
        
#         #sending the email
#         email.send()
      
#         # message to be printed out on the terminal       
#         print( 'Subscription Successful')
        
#         # where to redirect to after sending mail
#         return redirect ('success/')
    
#     return render(request, 'pages/index.html')

   
def about(request):
    return render(request, 'pages/aboutus.html')


def thanks(request):
    return render(request, 'pages/thankyou.html')
   
   
def mailer(request):
    return render(request, 'pages/contact_form.html')
   
   