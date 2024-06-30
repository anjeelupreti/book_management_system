
from django.urls import path,include
# from .views import register_user,login_user
from django.contrib.auth import views as auth_views
from .views import register_user,login_user

urlpatterns = [
#     path(
#         "login/",
#         auth_views.LoginView.as_view(
#             template_name="user/login.html",
# ),
# ),
    path('login/',login_user,name='login_user'),
    path('register/',register_user,name='register_user'),

]