from django.shortcuts import render, redirect,HttpResponseRedirect
from .models import crtinfo, usrinfo, criminfo
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from .forms import CrtReg, CrimReg, UserReg
from django.views.generic import CreateView
from .decorators import user_required, crim_required, crt_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from .models import User as mu
from django.core.mail import send_mail
from .models import Contact, Contact2
from datetime import datetime
from django.utils import timezone
from .models import Todo

# Create your views here....................................................................................


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def services(request):
    return render(request, 'services.html')


def features(request):
    return render(request, 'features.html')


def info(request):
    return render(request, 'info.html')


def indexo(request):
    return render(request, 'indexo.html')

#........................................................................................

def uploadImage(request):
    print("request handling .....")
    print("add image here")
    print(request.FILES)
    return render(request, 'indexo.html')

def indexTO(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    return render(request, "indexTO.html", {"todo_items": todo_items})


def to_do(request):
    current_date = timezone.now()
    content = request.POST.get("content")
    Todo.objects.create(added_date=current_date, text=content)
    return HttpResponseRedirect("/TO")


def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/TO")

#....................................................................................................................

def contactSS(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        usr_eml = request.POST.get('email')
        phone = request.POST.get('phnum')
        message = request.POST['message']
        send_mail(fname,
                  "User Phone:-  "+phone+"\n"+"User Email:- "+usr_eml+"\n"+message,
                  usr_eml,
                  ['ss.blognchat@gmail.com'],
                  fail_silently=True)
        messages.success(
            request, 'Thank you for your feedbacks,we will definitely try to improve !!')
    return render(request, 'contactSS.html')

#.....................................................................................................................

def sgin_user(request):
    if request.method == "POST":
        # check if user has entered correct credientials
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_user == True:
                login(request, user)
                # backend authenticated the credentials
                return redirect("sginpg_user")
            else:
                messages.error(
                    request, 'You are not authorized to access this page!')
        else:
            # No backend authenticated the credentials
            messages.error(request, 'Invalid Credentials!,plz try again')
            return render(request, 'sgin_user.html')
    return render(request, 'sgin_user.html')


@login_required
@user_required
def sginpg_user(request):
    crim_data = criminfo.objects.all()
    crim = {
        "crim_info": crim_data
    }
    return render(request, 'sginpg_user.html', crim)


@login_required
@user_required
def search(request):
    qur = request.GET.get('search')
    ct = criminfo.objects.filter(city__contains=qur)
    return render(request, 'search.html', {'ct': ct})


@login_required
@user_required
def update_usr_data(request):
    this_usr = usrinfo.objects.get(user=request.user)
    usr_inf = mu.objects.get(email=request.user.email)
    if request.method == "POST":
        fname = request.POST.get('fname')
        phnum = request.POST.get('phnum')
        email = request.POST.get('email')
        city = request.POST.get('city')
        addres = request.POST.get('addres')

        this_usr.full_Name = fname
        this_usr.phone = phnum
        this_usr.email = email
        this_usr.city = city
        this_usr.address = addres
        this_usr.save()

        usr_inf.email = email
        usr_inf.save()
        form=UserReg()
        messages.success(request, '...your data has been updated Successfully!')

    usr_dat = {
        "usr_info": this_usr,
        "my_usr_inf": usr_inf
    }
    return render(request, 'user_edit_x.html', usr_dat)


@login_required
@user_required
def change_pass_usr(request):
    if request.method == 'POST':
        fm = PasswordChangeForm(user=request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Password changed successfully!')
            update_session_auth_hash(request, fm.user)
            return redirect("sginpg_user")
    else:
        fm = PasswordChangeForm(user=request.user)
    return render(request, 'change_pass.html', {'form': fm})


def sgin_crim(request):
    if request.method == "POST":
        # check if user has entered correct credientials or not 
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            if user.is_crim == True:
                login(request, user)
                return redirect("sginpg_crim")
            else:
                messages.error(
                    request, 'You are not allowed to access this page!')
        else:
            # No backend authenticated the credentials
            messages.error(request, 'Invalid username or password!')
            return render(request, 'sgin_crim.html')
    return render(request, 'sgin_crim.html')


@login_required
@crim_required
def sginpg_crim(request):
    crim_data = criminfo.objects.filter(user=request.user.id)
    crim = {
        "crim_info": crim_data
    }
    return render(request, 'sginpg_crim.html', crim)


@login_required
@crim_required
def update_data(request):
    this_hsp = criminfo.objects.get(user=request.user.id)
    usr_inf = mu.objects.get(email=request.user.email)  
    if request.method == "POST":
        hosname = request.POST.get('hosname')
        phnum = request.POST.get('phnum')
        email = request.POST.get('email')
        city = request.POST.get('city')
        addres = request.POST.get('addres')
        nbd = request.POST.get('nbd')
        nvnt = request.POST.get('nvnt')
        nvc = request.POST.get('nvc')

        this_hsp.hospital_Name = hosname
        this_hsp.phone = phnum
        this_hsp.email = email
        this_hsp.city = city
        this_hsp.address = addres
        this_hsp.no_of_cases = nbd
        this_hsp.desc1 = nvnt
        this_hsp.desc2 = nvc
        this_hsp.save()

        usr_inf.email = email
        usr_inf.save()
        messages.success(request, 'Data has been Updated Successfully!')

    crim = {
        "crim_info": this_hsp,
        "my_usr_inf": usr_inf
    }
    return render(request, 'crim_edit_x.html', crim)


@login_required
@crim_required
def change_pass_crim(request):
    if request.method == 'POST':
        fm = PasswordChangeForm(user=request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Password changed successfully!')
            update_session_auth_hash(request, fm.user)
            return redirect("sginpg_crim")
    else:
        fm = PasswordChangeForm(user=request.user)
    return render(request, 'change_pass.html', {'form': fm})


def letsout(request):
    logout(request)
    return render(request, 'index.html')


class CrimView(CreateView):
    model = User
    form_class = CrimReg
    template_name = 'register_crim.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'criminal'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, 'User has been Created successfully!')
        login(self.request, user)
        return redirect("sgin_crim")


class UsrView(CreateView):
    model = User
    form_class = UserReg
    template_name = 'register_user.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'user'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, 'User has been created successfully!')
        login(self.request, user)
        return redirect("sgin_user")


class CrtView(CreateView):
    model = User
    form_class = CrtReg
    template_name = 'register_crt.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'court'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, 'User has been created successfully!')
        login(self.request, user)
        return redirect("sgin_crt")


def sgin_crt(request):
    if request.method == "POST":
        # check if user has entered correct credientials
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            if user.is_crt == True:
                login(request, user)
                return redirect("sginpg_crt")
            else:
                messages.error(
                    request, 'You are not authorized to access this page!')
        else:
            # No backend authenticated the credentials
            messages.error(request, 'Invalid username or password!')
            return render(request, 'sgin_crt.html')
    return render(request, 'sgin_crt.html')


@login_required
@crt_required
def sginpg_crt(request):
    return render(request, 'sginpg_crt.html')


def contact2(request):
    if 'q' in request.GET:
        q = request.GET['q']
        all_Contact2 = Contact2.objects.filter(name__icontains=q)
    else:
        all_Contact2 = Contact2.objects.all().order_by("id")
        if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            desc = request.POST.get('desc')
            desc = request.POST.get('desc')
            contact2 = Contact2(name=name, email=email,phone=phone,desc=desc,date=datetime.today())
            contact2.save()
            messages.error(request, 'THE MESSAGE HAS BEEN SENT...')
    return render(request, 'contact2.html', {"messagess": all_Contact2})


def contact(request):
    if 'q' in request.GET:
        q = request.GET['q']
        all_Contact = Contact.objects.filter(name__icontains=q)
    else:
        all_Contact = Contact.objects.all()
        if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            desc = request.POST.get('desc')
            desc = request.POST.get('desc')
            contact = Contact(name=name, email=email,phone=phone, desc=desc, date=datetime.today())
            contact.save()
            messages.error(request, 'THE MESSAGE HAS BEEN SENT...')
    return render(request, 'contact.html', {"messages": all_Contact})



















