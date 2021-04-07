from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
def login_func3(request):
    return render(request, 'login_page3.html')

def profile_page(request):
    # return render(request, 'profile_page1.html')
    return render(request, 'profile2.html')

@csrf_exempt
def user_login(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged in')
            return render(request, 'welcome_page.html')
        else:
            messages.error(request, 'invalid credentials')
            return redirect('login3')

    return HttpResponse('404 Not Found')


def user_logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return HttpResponse("Successfully logged out")


def sign_up_func1(request):
    # return render(request, 'signup_page.html')
    return render(request, 'signup2.html')

def User_signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['password']
        pass2 = request.POST['password2']

        if len(username) < 6:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('signup')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('signup')

        if (pass1 != pass2):
            messages.error(request, " Passwords do not match")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('signup')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        return render(request,'login_page3.html')


    else:
        return HttpResponse("404 - Not found")


from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import update_last_login

# def update_first_login(sender, user, **kwargs):
#     if user.last_login is None:
#         # First time this user has logged in
#         kwargs['request'].session['first_login'] = True
#     # Update the last_login value as normal
#     update_last_login(sender, user, **kwargs)
#
# user_logged_in.disconnect(update_last_login)
# user_logged_in.connect(update_first_login)

# def index(request):
#     print(request.user.last_login)
#     if request.user:
#         if request.session.get('first_login'):
# return redirect('profile')
#     return HttpResponse('first_login')
# else:
#     return HttpResponse('second login')
# return redirect('home')
# else:
#     return HttpResponse('else')
# return redirect('/login')

# def get_user(self, user_id):
#     try:
#         return CustomUser.objects.get(pk=user_id)
#     except CustomUser.DoesNotExist:
#         return None

from django.contrib.auth.decorators import login_required


@csrf_exempt
def index(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged in')
            return redirect('login2')
        else:
            messages.error(request, 'invalid credentials')
            return redirect('login2')

    return HttpResponse('404 Not Found')







import folium

from django.views.generic import TemplateView


class FoliumView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        figure = folium.Figure()
        m = folium.Map(
            location=[45.372, -121.6972],
            zoom_start=12,
            tiles='Stamen Terrain'
        )
        m.add_to(figure)

        folium.Marker(
            location=[45.3288, -121.6625],
            popup='Mt. Hood Meadows',
            icon=folium.Icon(icon='cloud')
        ).add_to(m)

        folium.Marker(
            location=[45.3311, -121.7113],
            popup='Timberline Lodge',
            icon=folium.Icon(color='green')
        ).add_to(m)

        folium.Marker(
            location=[45.3300, -121.6823],
            popup='Some Other Location',
            icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(m)
        figure.render()
        return {"map": figure}


def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'sk.eyJ1IjoidHVzaGFyODg4OSIsImEiOiJja24wNTdlOTkwazh4MnVvMzJ0OGFtcTc2In0.7Htmd3GIHDX7lCfk5KpZzQ'
    return render(request, 'default.html',
                  { 'mapbox_access_token': mapbox_access_token })
