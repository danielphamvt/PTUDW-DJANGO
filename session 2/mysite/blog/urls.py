
from django.urls import path
from .views import IndexView, SignUpDoneView, SignUp, noidung_baiviet, noidung_comment, timkiem_baiviet
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
app_name = 'blog'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('signup/', SignUp.as_view(success_url=reverse_lazy('blog:signup_done')), name='signup'),
    path('signup/done/', SignUpDoneView.as_view(), name='signup_done'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),


    path('', IndexView.as_view(), name='home'),
    path('<int:pk>/', noidung_baiviet, name='noidung_baiviet'),
    path('new_comment/', noidung_comment, name='noidung_comment'),
    path('search/', timkiem_baiviet, name='search'),

]
