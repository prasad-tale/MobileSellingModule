from django.shortcuts import render,redirect,HttpResponse
from .models import Selling
from .forms import SellingForm
from django.contrib import messages
# Create your views here.

##basic home view showing approved mobile phones for user

def home(request):
    posts = Selling.objects.all()

    context = {'posts': posts}
    return render(request,'selling/home.html', context)

def sellproduct(request):
    form = SellingForm()
   

    if request.method == 'POST':
        form = SellingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your order has been saved, We will contact you once it is approved')
            return redirect("home")
            
        

    context = {'form':form}
    return render(request,'selling/sell.html', context)

def get_post(request, pk_id):
    post = Selling.objects.get(id=pk_id)


    context = {'post': post}
    return render (request, 'selling/view.html', context)

def buy_phone(request):
    return HttpResponse("Customer will buy the Phone over here")