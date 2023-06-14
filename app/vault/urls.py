from django.urls import path
from vault import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('user/', views.user_all, name='all_users'),
    path('user/<int:id>/', views.user_detail, name='individual_user'),
    path('password/', views.passwords_one_user, name='passwords_one_user'),
    # path('password/<int:user_id>/', views.passwords_one_user, name='one_user_passwords'),
    # path('password/<int:user>/<str:url>/', views.unique_password_one_user, name='unique_passwords')
] 