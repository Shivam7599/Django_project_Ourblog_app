from django.urls import path
# from . import views

from .views import UserRegisterView, UserEditView, PasswordsChangeView, show_user_profile_ViewDetailView, CreateProfilePageView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name = "register"),
    path("Edit/", UserEditView.as_view(), name="Edit_Profile"),
    # path("password/", auth_views.PasswordChangeView.as_view(template_name='registration/change_pass.html'), name="Change_pass"),
    path("password/", PasswordsChangeView.as_view(), name="Change_pass"),
    path("<int:pk>/profile/", show_user_profile_ViewDetailView.as_view(), name="show_user_profile"),
    path("Edit_user_profile/", CreateProfilePageView.as_view(), name="Edit_user_profile"),
]