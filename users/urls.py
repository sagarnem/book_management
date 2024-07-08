from django.urls import path
from django.contrib.auth import views as auth_views
from users.views import list_user_balance, admin_add_balance

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="user/login.html")),
    path('userbalance',list_user_balance, name='user-balance'),
    path('userbalance/create',admin_add_balance, name='admin-user-balance'),

]