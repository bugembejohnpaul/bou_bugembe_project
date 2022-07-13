from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User, auth


# Create your views here.
def home(request):
    # return HttpResponse("Hello Uganda, Am John Paul")
    return render(request, "home.html")


def login(request):
    if request.method == 'post':
        username = request.post['username']
        password = request.post['password']
        return render(request, 'home.html')
    return render(request, "login.html")


def register(request):
    if request.method == 'post':
        fname = request.post['fname']
        lname = request.post['lname']
        organisation = request.post['organisation']
        department = request.post['department']
        telphone = request.post['telphone']
        email = request.post['email']
        created_by = request.post['created_by']
        create_date = request.post['create_date']
        updated_by = request.post['updated_by']
        user = User.objects.create_user(fname=fname, lname=lname, organisation=organisation,
                                        department=department, telphone=telphone, email=email, created_by=created_by,
                                        create_date=create_date, updated_by=updated_by)
        user.save()
        print("Great User Created")

    else:
        return render(request, 'register.html')


def items_register(request):
    return render(request, 'items_register.html')
