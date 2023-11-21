# from django.views import View
from django.shortcuts import render,HttpResponseRedirect
from .models import dj_srk, Cart
from .forms import dj_form
from django.contrib import messages

# Create your views here.
def home(request):
    a = dj_srk.objects.all()
    return render(request, 'index.html', {'data':a})

def data(request):
    if request.method == "POST":
        fm = dj_form(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
            messages.success(request, "DATA Added Successfully")

            return HttpResponseRedirect("/main/home/")
    else:
        fm = dj_form()
    return render(request, 'data_enter.html', {'form':fm})

def update(request, id):
    if request.method == "POST":
        pi = dj_srk.objects.get(pk = id)
        fm = dj_form(request.POST, request.FILES, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request, "DATA Updated Successfully")
            return HttpResponseRedirect("/main/home/")
    else:
        pi = dj_srk.objects.get(pk = id)
        fm = dj_form(instance=pi)

    return render(request, "update.html", {"form1": fm})

def dele(request, id):
    if request.method =="POST":
        pi = dj_srk.objects.get(pk=id)
        pi.delete()
        messages.success(request, "DATA Deleted Successfully")
        return HttpResponseRedirect("/main/home/")

def cart(request):
    a= dj_srk.objects.all()
    return render(request, 'cart.html', {'data':a})

def add_to_cart(request):
    if request.method == "GET":
        cid = request.GET.get('cid')
        Store = Cart.objects.create(Cart_id = cid)
        Store.save()
        return HttpResponseRedirect("/main/home/")

def view_cart(request):
    cart1 = Cart.objects.all().values_list('dj_srk_id', flat=True)
    cartdata = dj_srk.objects.filter(id__in = cart1)
    print(cart1)
    return render(request, 'show cart.html', {'data':cartdata})