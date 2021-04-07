from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('map/', views.default_map),
    path('signin/', views.login_func3, name='login3'),
    path('login/', views.user_login),
    path('logout/', views.user_logout),
    path('signup/', views.sign_up_func1, name='signup'),
    path('user_signup/', views.User_signup),
    path('profile/', views.profile_page),
    # path('login1/', views.login_func),
    # path('login2/', views.login_func2, name='login2'),
    # path('login_main/', views.login_main_func),
    # path('index1/', views.index_page),
    # path('index2/', views.FoliumView.as_view()),
]