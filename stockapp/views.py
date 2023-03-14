from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from stockapp.forms import cust_form, user_reg, stock_form
from stockapp.models import Stock, Customer_Registration


# Create your views here.
def home(request):

    return render(request,'index.html')

def log(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin1')

            elif user is not None and user.is_cust:
                return redirect('customer')



        else:
            messages.info(request, 'invalid credentials')

    return render(request,'login.html')

def cust_reg(request):
    u_form = user_reg()
    c_form = cust_form()
    if request.method == 'POST':
        u_form = user_reg(request.POST)
        c_form = cust_form(request.POST,request.FILES)
        if u_form.is_valid() and c_form.is_valid():
            user = u_form.save(commit=False)
            user.is_cust = True
            user.save()
            customer = c_form.save(commit=False)
            customer.user = user
            customer.save()
            messages.info(request, 'student registered successfully')
            return redirect('log')

    return render(request, 'cust_reg.html', {'u_form': u_form, 'c_form': c_form})

@login_required(login_url='log')
def admin1(request):
    return render(request,'admin1.html')

@login_required(login_url='log')
def customer(request):
    return render(request,'customer.html')
@login_required(login_url='log')
def add_stock(request):
    form = stock_form()
    if request.method == "POST":
        form = stock_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_stock')
    return render(request, 'add_stock.html', {'form': form})
@login_required(login_url='log')
def view_stock(request):
    data = Stock.objects.all().order_by('-date_added')
    context = {'data': data}
    return render(request, 'view_stock.html', context)

@login_required(login_url='log')
def view_user_stock(request):
    data = Stock.objects.all().order_by('-date_added')
    context = {'data': data}
    return render(request, 'view_user_stock.html', context)

@login_required(login_url='log')
def stock_update(request,id):
    stock1 = Stock.objects.get(id=id)
    form = stock_form(instance=stock1)
    if request.method =='POST' :
        form=stock_form(request.POST,instance = stock1)
    if form.is_valid():
        form.save()
        return redirect('view_stock')
    return render(request,'add_stock.html',{'form':form})

@login_required(login_url='log')
def stock_delete(request,id):
    Stock.objects.get(id=id).delete()
    return redirect('view_stock')

@login_required(login_url='log')
def view_customer(request):
    data = Customer_Registration.objects.all()
    return render(request, 'view_customer.html', {'data': data})

@login_required(login_url='log')
def logout_customer(request):
    logout(request)
    return redirect('log')

@login_required(login_url='log')
def logout_admin(request):
    logout(request)
    return redirect('log')