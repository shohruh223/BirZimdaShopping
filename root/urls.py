from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from app.views import IndexView, MahsulotListView, MahsulotDetailView, AloqaView, BizHaqimizdaView, BlogListView, \
    BlogDetailView, CheckoutView, SavatchaView, LoginView, RegisterView, ForgotPasswordView, ResetPasswordView, \
    ConfirmPasswordView, UserLoginView, UserLogoutView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', IndexView.as_view(), name='index'),

    path('mahsulotlar.html', MahsulotListView.as_view(), name='mahsulotlar'),

    path("product/<int:pk>/", MahsulotDetailView.as_view(), name="mahsulot-detail"),

    path('aloqa.html', AloqaView.as_view(), name='aloqa'),
    path('biz-haqimizda.html', BizHaqimizdaView.as_view(), name='biz-haqimizda'),

    path('blog.html', BlogListView.as_view(), name='blog'),

    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),

    path('checkout.html', CheckoutView.as_view(), name='checkout'),
    path('savatcha.html', SavatchaView.as_view(), name='savatcha'),

    path('login.html', UserLoginView.as_view(), name='login'),
    path('register.html', RegisterView.as_view(), name='register'),
    path('logout/', UserLogoutView.as_view(), name='logout'),


    path('forgot-password.html', ForgotPasswordView.as_view(), name='forgot-password'),
    path('reset-password.html', ResetPasswordView.as_view(), name='reset-password'),
    path('confirm-password.html', ConfirmPasswordView.as_view(), name='confirm-password'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)