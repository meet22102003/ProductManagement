from django.contrib import messages
from django.shortcuts import render, redirect
from .models import producttable,registertable,carttable



# Create your views here.

def showproductpage(request):
    alldata = producttable.objects.all()
    print(alldata)
    context = {
        "data": alldata
    }
    return render(request, "showproduct.html", context)


def addproductpage(request):
    return render(request, "addproduct.html")


def insertproductdata(request):
    pname = request.POST.get("pname")
    pprice = request.POST.get("pprice")
    pdesc = request.POST.get("pdesc")
    pimage = request.FILES["pimage"]

    storedata = producttable(name=pname, price=pprice, description=pdesc, proimage=pimage)
    storedata.save()

    return redirect("/")

def manageproduct(request):
    alldata = producttable.objects.all()
    print(alldata)
    context = {
        "data":alldata
    }
    return render(request,"manageproduct.html",context)

def singleproduct(request,pid):
    getdata = producttable.objects.get(id=pid)
    print(getdata)
    context = {
        "singledata":getdata
    }
    return render(request,"singleproduct.html",context)

def delete(request,id):
    getdeldata = producttable.objects.get(id=id)
    getdeldata.delete()
    return redirect("/manageproduct")


def registerpage(request):
    return render(request,"Registration.html")

def loginpage(request):
    return render(request,"Login.html")

def fetchregdata(request):
    uname = request.POST.get("name")
    uemail = request.POST.get("email")
    upassword = request.POST.get("password")
    ugender = request.POST.get("gender")
    uphone = request.POST.get("phone")
    uadd = request.POST.get("address")
    urole = request.POST.get("role")
    udp = request.FILES["dp"]

    insertdata = registertable(name=uname,email=uemail,password=upassword, gender=ugender,role=urole,phone=uphone,address=uadd,profilepicture=udp)
    insertdata.save()
    return render(request,"Login.html")

def checklogindata(request):
    uemail = request.POST.get("uemail")
    upassword = request.POST.get("upassword")

    try:
        checkdata = registertable.objects.get(email=uemail,password=upassword)
        request.session["logid"] = checkdata.id
        request.session["logname"] = checkdata.name
        request.session["logemail"] = checkdata.email
        request.session.save()
        return redirect("/showproduct")

    except registertable.DoesNotExist:
        messages.error(request, "Incorrect email or password. Please try again.")
        return render(request, "login.html")

    if checkdata is not None:
        return redirect("/showproduct")
    else:
        messages.error(request,"incorrect email or password.please try again")
        return render(request,"login.html")

def logout(request):
    try:
        del request.session["logid"]
        del request.session["logname"]
        del request.session["logemail"]

    except:
        pass
    return render(request,"login.html")

def addtocart(request):
    uid = request.session["logid"]
    proid = request.POST.get("pid")
    proprice = request.POST.get("pprice")
    proquantity = request.POST.get("quantity")
    totalamount = float(proprice) * float(proquantity)
    print(totalamount)

    try:
        checkitemincart = carttable.objects.get(userid=uid,productid=proid,cartstatus=1)
    except:
        checkitemincart = None

    if checkitemincart is None:
        storedata = carttable(userid=registertable(id=uid),productid=producttable(id=proid),quantity=proquantity,totalamount=totalamount,cartstatus=1,orderid=0)
        storedata.save()
    else:
        checkitemincart.quantity = checkitemincart.quantity + float(proquantity)
        checkitemincart.totalamount = float(checkitemincart.quantity) * float(proprice)
        checkitemincart.save()
    return redirect("/showproduct")


