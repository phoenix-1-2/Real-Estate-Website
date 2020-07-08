from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
# Create your views here.
def contact(request):

    if request.method == "POST":
        user_id=request.POST['user_id']
        realtor_email=request.POST['realtor_email']
        listing_id=request.POST['listing_id']
        listing=request.POST.get('listing',"")
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']

        user_id=request.user.id
        has_contacted = Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
        if has_contacted:
            messages.error(request,'You have already submitted an inquiry for this property')
            return redirect('/listings/' + listing_id )


        contact = Contact(listing_id=listing_id,listing=listing,name=name,email=email,phone=phone,message=message,user_id=user_id)
        contact.save()

        send_mail(

            'Property Inquiry',
            'Hello ' + name + ', Your inquiry for ' + listing + ' has been sent to our realtor and will get back to you ASAP.For more info Please Login',
             'nikhil.bhasin124@gmail.com',
             [
                 realtor_email,
                 email,
                 'geekycoder.12@gmail.com'
             ],
             fail_silently=False


        )




        messages.success(request,"You have successfully made an inquiry , Realtor will get back to you soon")
        return redirect('/listings/' + listing_id)
        