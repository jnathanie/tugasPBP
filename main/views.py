from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from main.forms import ItemForm
from django.urls import reverse
from main.models import Item
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout 
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotFound


@login_required(login_url='/login')
def show_main(request):
    items = Item.objects.filter(user=request.user)
    
    items_count = items.filter(amount__gt=0).count()
    
    context = {
        'name': request.user.username,
        'class': 'PBP D',
        'items': items,
        'item_count': items_count,  # Menambah item_count ke dalam konteks
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)

def delete_item(request, id):
    # Get data berdasarkan ID
    item = Item.objects.get(pk = id)
    # Hapus data
    item.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
            
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/login')
def add_amount(request, id):
    item = Item.objects.get(pk = id)
    item.amount += 1
    item.save()
    return HttpResponseRedirect(reverse('main:show_main'))

@login_required(login_url='/login')
def min_amount(request, id):
    item = Item.objects.get(pk = id)
    if item.amount > 0:
        item.amount -= 1
        item.save()
    if item.amount == 0:
        item.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@login_required(login_url='/login')
def remove_item(request, id):
    if request.method == 'POST':
        item = Item.objects.filter(user=request.user, pk=id).first()
        if item:
            item.delete()
    return redirect('main:show_main')

def get_item_json(request):
    product_items = Item.objects.filter(user=request.user)
    data = serializers.serialize('json', product_items)
    return HttpResponse(data, content_type='application/json')

@csrf_exempt
def add_item_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        user = request.user

        new_product = Item(name=name, amount=amount, description=description, user=user)
        new_product.save()
        
        response_data = {
            'id': new_product.id,
            'name': new_product.name,
            'amount': new_product.amount,
            'description': new_product.description,
            'date_added': new_product.date_added.strftime("%Y-%m-%d %H:%M:%S")
        }


        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def delete_item_ajax(request, item_id):
    if request.method == 'DELETE':
        item = Item.objects.get(id=item_id)
        item.delete()
        return HttpResponse({'status': 'DELETED'}, status=200)