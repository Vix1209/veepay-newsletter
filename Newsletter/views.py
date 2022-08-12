from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives
from django.template import loader
from django.contrib import messages
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
            'Veepay Telecommunications', message,
            'VEEPAY', [email]  
        )
        
        #converting the text file to html
        
        email.content_subtype = 'html'
        
        #sending the email
        email.send()
        
        # message to show at the admin page
        messages.success(request, 'subscription successful')
      
        # message to be printed out on the terminal       
        print( 'Subscription Successful')
        
        # where to redirect to after sending mail
        return redirect ('success/')
    
    return render(request, 'pages/index.html')
    
   
def about(request):
    return render(request, 'pages/aboutus.html')


def thanks(request):
    return render(request, 'pages/thankyou.html')
   
   
def mailer(request):
    return render(request, 'pages/contact_form.html')
   
   
   
    
## simple mail

# def index(request):
#     if request.method == 'POST':
    
#         mail = request.POST['user_email']
    
#         subscribe = Newsletter(email = mail)
#         subscribe.save()
        
#         mail_list = [mail]
        
#         send_mail(
#             'WELCOME TO VEEPAY 💙',
#             '''
#             Thank you for your interest in our product! We are super pumped to have you here.
            
#             Veepay is currently working to give you the avenue to connect with your favorite services
#             by providing Bulk SMS, SME data, Recharge platforms(Cable Tv and airtime etc).8
#             Stayed tuned as we bring you the best.
            
#             To help you get started, follow and like our social media pages
            
            
            
            
            
            
            
            
#             Cheers 
#             Veepay (Feed your network, Live better)''',
            
#             '',
#             mail_list, 
#             fail_silently=False,
#         )
        
#         return redirect('success/')
    
#     return render(request, 'pages/index.html')
      

    


    


