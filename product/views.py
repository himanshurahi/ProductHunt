from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import product
from .models import votecount
from django.contrib import messages
from django.utils.translation import get_language

# Create your views here.


#Error Pages
def handler404(request, exception):
    return render(request, '404.html')

def home(request):
	products = product.objects
	votes = votecount.objects
	# return HttpResponse('sd')
	return render(request,'home.html',{'products':products})

@login_required
def create(request):
	if request.method == 'POST':
		if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
			Product = product()
			try:
				product.objects.get(title = request.POST['title'])
				return render(request,'create.html',{'error':'title already exist..'})
			except product.DoesNotExist:
				Product.title = request.POST['title']

			Product.body = request.POST['body']
			if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):

				Product.url = request.POST['url']
			else:
				Product.url = "http://" + request.POST['url']
			Product.icon = request.FILES['icon']
			Product.image = request.FILES['image']
			Product.pub_date = timezone.datetime.now()
			Product.votes_total = 1
			Product.hunter = request.user
			Product.save()
			return redirect('home')

		else:
			return render(request,'create.html',{'error':'Please Fill All Fields..'})

	else:
		return render(request,'create.html')

@login_required
def upvote(request, product_id):
	if request.method == 'POST':
		# c = votecount.objects.filter(product_id = product_id) & votecount.objects.filter(user_id = request.user.id) 
		# if c:
		# 	messages.success(request, 'You already upvoted')
		# 	return redirect('home')
		# else:
		# 	votes = votecount()
		# 	Product = product()
		# 	votes.product_id = product_id
		# 	votes.user_id = request.user.id
		# 	votes.save()
		# 	p = get_object_or_404(product ,pk = product_id)
		# 	p.votes_total += 1
		# 	p.save()	
		# 	return redirect('home')
		obj, created = votecount.objects.get_or_create(user_id = request.user.id, product_id = product_id)
		if created:
			p = get_object_or_404(product, pk = product_id)
			p.votes_total += 1
			p.save()
			return redirect('home')
		else:
			messages.success(request, 'You already upvoted')
			return redirect('home')

	else:
		return redirect('home')




	# if request.method == 'POST':
	# 	products = get_object_or_404(product,pk = product_id)
	# 	products.votes_total += 1;
	# 	products.save()
	# 	return redirect('home')
	# else:
	# 	return redirect('home')
	# if request.method == 'POST':
	# 	votes = votecount()
		# Product = product()
		# votes = votecount()
		# try:
		# 	votes.objects.get(user_id = request.user)
		# 	return render(request,'home.html',{'error':'no bro'})
		# except votes.DoesNotExist:
		# 	votes.product_id = product_id
		# 	votes.user_id = request.user.id
		# 	votes.save()
		# 	return redirect('home')
		# try:
		# 	votecount.objects.get(user_id = request.user.id)
		# 	votecount.objects.get(product_id = product_id)
		# 	messages.success(request, 'You already upvoted')
		# 	return redirect('home')
		# except:
		# 	votes.user_id = request.user.id
		# votes.product_id = product_id
		# votes.save()
		# return redirect('home')
		
	# 	return HttpResponse(product_id)


	# else:
	# 	return redirect('home')
