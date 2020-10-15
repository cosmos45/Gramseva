from django.shortcuts import render
from .models import UserInfo
from django.core.files.storage import FileSystemStorage


def Registration(request):
    return render(request, "registration.html")


def Add_data(request):
    print("form is submitted")
    if request.method == "POST":
        aadharcard = request.FILES['img']
        fs = FileSystemStorage()
        filename = fs.save(aadharcard.name, aadharcard)

    if request.method == "POST":
        pancard = request.FILES['img1']
        fs = FileSystemStorage()
        filename = fs.save(pancard.name, pancard)

        fname = request.POST.get("fname")
        mname = request.POST.get("mname")
        lname = request.POST.get("lname")
        cname = request.POST.get("cname")
        pnumber = request.POST.get("pnumber")
        email = request.POST.get("email")
        dob = request.POST.get("dob")
        pin = request.POST.get("pin")
        district = request.POST.get("district")
        state = request.POST.get("state")
        city = request.POST.get("city")
        address = request.POST.get("address")

        userinfo = UserInfo(fname=fname, mname=mname, lname=lname, cname=cname, pnumber=pnumber, email=email, dob=dob,
                            pin=pin, district=district, state=state, city=city, address=address, aadharcard=aadharcard, pancard=pancard)

        userinfo.save()

        return render(request, "registration.html")
