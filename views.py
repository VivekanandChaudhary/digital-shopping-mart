from django.shortcuts import render,redirect
from django.contrib import messages
from app.models import productModel
from django.core.paginator import Paginator


def showIndex(request):
    #result=productModel.objects.all()
    #return render(request,"index.html",{"data":result})

    result = productModel.objects.all()
    pa = Paginator(result, 2)
    page_number = request.GET.get("page_no", 1)
    page = pa.page(page_number)
    return render(request, "index.html", {"page": page})


def admin_login(request):
    return render(request,"admin_login.html")


def admin_login_check(request):
    un=request.POST.get("t1")
    pa=request.POST.get("t2")

    if un=="vivek" and pa=="vivek12":
        return render(request,"admin_home.html")
    else:
        messages.error(request,"Invalid Users")
        return redirect('admin_login')


def admin_home(request):
    return render(request,"admin_home.html")


def admin_view_users(request):
    return render(request,"admin_view_users.html")


def admin_view_products(request):
    #result=productModel.objects.all()
    #return render(request,"admin_view_products.html",{"data":result})


    result=productModel.objects.all()
    pa=Paginator(result,2)
    page_number=request.GET.get("page_no",1)
    page=pa.page(page_number)
    return render(request,"admin_view_products.html",{"page":page})


def save_product(request):
    na=request.POST.get("p1")
    pr=request.POST.get("p2")
    qty=request.POST.get("p3")
    img=request.FILES["p4"]
    status="active"
    productModel(name=na,price=pr,quantity=qty,photo=img,status=status).save()
    return redirect('admin_view_products')








def delete_product_info(request):
    no=request.GET.get("no")
    productModel.objects.filter(no=no).delete()
    return redirect('admin_view_products')


def add_to_cart(request):
    k=request.GET.get("c1")
    v=request.GET.get("c2")
    response=redirect('in_cart')
    response.set_cookie(k,v)
    return response


def in_cart(request):
    return render(request,"in_cart.html",{"data":request.COOKIES})



