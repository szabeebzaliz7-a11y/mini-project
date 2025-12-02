from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from django.contrib import messages
# Create your views here.
def index(request):
    paints=Uploadsave.objects.exclude(user=request.user)
    print(paints,'hiiiiiiiiiiiiiiiiiiii')
    # print(request.user)
    context={
        'paints':paints
    }


    return render(request,'index.html',context)
def about(request):
    return render(request,'about.html')
def blogdetails(request):
    return render(request,'blog_details.html')
def blog(request):
    return render(request,'blog.html')
def contact(request):
    return render(request,'contact.html')
def elements(request):
    return render(request,'elements.html')
def main(request):
    return render(request,'main.html')
def productdetails(request):
    return render(request,'product_details.html')
def imageview(request,im_id):
    print(im_id,'kkkkkkkkkkkk')
    art=Uploadsave.objects.get(id=im_id)
    context={
        'art':art
    }

    return render(request,'imageview.html',context)
def shop(request):
    return render(request,'shop.html')
def uploadimage(request):
    return render(request,'upload.html')
def profile(request):
    return render(request,'profile.html')
def cart(request):
    item=Mycart.objects.filter(user=request.user)
    context={
        'item':item
    }
    return render(request,'cart.html',context)
def wishlist(request):
    item=Whishlist.objects.filter(user=request.user)
    context={
        'item':item
    }
    return render(request,'wishlist.html',context)

def uploadsave(request):
    if request.method=='POST':
        imagename=request.POST.get('imagename')
        description=request.POST.get('description')
        price=request.POST.get('price')
        uploadimage=request.FILES.get('uploadimage')
        print(imagename,description,price,uploadimage)
        user=request.user
        Uploadsave.objects.create(imagename=imagename,description=description,price=price,uploadimage=uploadimage,user=user)
        return redirect('paintapp:index')
    
def viewprofile(request,user_id):
    artist=Customuser.objects.get(id=user_id)
    art=Uploadsave.objects.filter(user=artist)
    context={
        'art':art
    }
    return render(request,'viewmore.html',context)

def mycart(request,item_id):
    # print(item_id,'idddddddddddddddddddddddddddddddd')
    mycart=Uploadsave.objects.get(id=item_id)
    user=request.user
    cart_item=Mycart.objects.filter(art=mycart,user=user)
    # print(cart_item,'oooooooooooooooooooooooooooo')
    
    if cart_item:
        messages.error(request,'item already exists')
        return redirect('paintapp:cart')
    else:
        item=Mycart.objects.create(art=mycart,user=user)
        messages.success(request,'item added succesfully')
        return redirect('paintapp:cart')
    
def mywishlist(request,itm_id):
    mylist=Uploadsave.objects.get(id=itm_id)
    user=request.user
    wish_item=Whishlist.objects.filter(art=mylist,user=user)
    if wish_item:
        messages.error(request,'item already added to wishlist')
        return redirect('paintapp:wishlist')
    else:
        item=Whishlist.objects.create(art=mylist,user=user)
        messages.success(request,'item added to whishlist')
        return redirect('paintapp:wishlist')
    

    
def buynow(request, buy_id):
    buy_item = Uploadsave.objects.get(id=buy_id)
    try:
        citem = Mycart.objects.get(user=request.user, art=buy_item)
        quantity = citem.quantity
    except Mycart.DoesNotExist:
        citem = None
        quantity = 1

    total_price = buy_item.price * quantity

    context = {
        'buy_item': buy_item,
        'citem': citem,          # ✅ pass cart item
        'quantity': quantity,
        'total_price': total_price
    }
    return render(request, 'buy.html', context)

def updatequantity(request, qu_id, operator):
    buy_item = Uploadsave.objects.get(id=qu_id)
    print(qu_id, operator)

    if operator == 'minus':
        try:
            citem = Mycart.objects.get(art=buy_item, user=request.user)
            cquantity = citem.quantity
            if cquantity == 1:
                messages.error(request, 'cart quantity cannot be less than 1')
            else:
                citem.quantity = cquantity - 1
                citem.save()
        except:
            messages.error(request, 'cart quantity cannot be less than 1')

        # ✅ always return after minus
        return redirect('paintapp:buynow', qu_id)

    if operator == 'plus':
        try:
            citem = Mycart.objects.get(art=buy_item, user=request.user)
            cquantity = citem.quantity
            citem.quantity = cquantity + 1
            citem.save()
        except:
            Mycart.objects.create(art=buy_item, user=request.user, quantity=2)

        # ✅ always return after plus
        return redirect('paintapp:buynow', qu_id)
        
# def followings(request):

        



