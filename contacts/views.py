from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contact(request):
	if request.method == 'POST':
		listing_id = request.POST['listing_id']
		listing = request.POST['listing']
		user_id = request.POST['user_id']
		realtor_email = request.POST['realtor_email']
		name = request.POST['name']
		email = request.POST['email']
		phone = request.POST['phone']
		message = request.POST['message']

		# Check if there is already an inquiry for the current user

		if request.user.is_authenticated:
			user_id = request.user.id
			if Contact.objects.all().filter(listing_id=listing_id, user_id=user_id).exists():
				messages.error(request, 'You have already submitted an inquiry for this listing.')
				return redirect('/listings/' + listing_id)
		
		contact = Contact(listing_id=listing_id, listing=listing, name=name, user_id=user_id, email=email, phone=phone, message=message)
		contact.save()

		# Send mail

		send_mail(
			'There is a new inquiry for ' + listing,
			'Sign into the admin page to view the new inquiry.',
			'devbotalex@gmail.com',
			[realtor_email, 'devbotalex@gmail.com'],
			fail_silently=False
			)

		messages.success(request, 'You have successfully sent an inquiry. A realtor will get back to you soon.')

	return redirect('/listings/' + listing_id)