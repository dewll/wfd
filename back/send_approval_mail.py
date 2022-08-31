from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import EmailMessage, BadHeaderError
from .  import models
def send_mail(email,name):
    try:
        user = models.User.objects.get(email = email)
        if user is not None:
            print("yes")
            subject = "Station Approved"
            template_name = "back/station_approved.txt"
            c = {
            "email":email,
            'domain':'127.0.0.1:8000',
            'site_name': 'wfd',
            'protocol': 'http',
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "name":name,
            "user": user,
            'token': default_token_generator.make_token(user),

            }
            email = render_to_string(template_name, c)
            try:
                email = EmailMessage(subject, email, 'balosod37@gmail.com' , [email])
                email.send(fail_silently=False)
            except BadHeaderError:
                pass
                #return Response("Invalid header found", status=status.HTTP_400_BAD_REQUEST)
            #return Response("Password Reset Form Sent to Your Email", status=status.HTTP_200_OK)
    except:
        pass
        #return Response("Wrong Email Address", status=status.HTTP_400_BAD_REQUEST)