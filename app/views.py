from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from django.views.generic import ListView, DetailView
from django.views.generic import TemplateView, FormView

from app.form import RegisterForm, EmailLoginForm, ContactForm
from app.models import Portfolio, Product


class IndexView(ListView):
    template_name = 'index.html'

    model = Product
    paginate_by = 3
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["star_range"] = range(1, 6)
        context["top_products"] = Product.objects.order_by('-review')[:4]
        return context


class MahsulotListView(ListView):
    template_name = 'mahsulotlar.html'
    model = Product
    paginate_by = 3
    context_object_name = 'products'

    def get_queryset(self):
        queryset = Product.objects.all()
        q = self.request.GET.get('q')

        sort = self.request.GET.get('sort')
        if sort == 'title_asc':
            queryset = queryset.order_by('title')
        elif sort == 'price_asc':
            queryset = queryset.order_by('price')
        elif sort == 'price_desc':
            queryset = queryset.order_by('-price')
        elif sort == 'rating_desc':
            queryset = queryset.order_by('-review')

        if q:
            queryset = queryset.filter(
                Q(title__icontains=q))


        return queryset

class MahsulotDetailView(DetailView):
    template_name = 'mahsulot-detail.html'
    model = Product
    context_object_name = 'product'

class BizHaqimizdaView(TemplateView):
    template_name = 'biz-haqimizda.html'

class BlogListView(ListView):
    model = Portfolio
    paginate_by = 3
    template_name = 'blog.html'
    context_object_name = 'portfolio'

class BlogDetailView(DetailView):
    template_name = 'blog-detail.html'

    model = Portfolio
    context_object_name = 'portfolio'

class CheckoutView(TemplateView):
    template_name = 'checkout.html'

class ConfirmPasswordView(TemplateView):
    template_name = 'confirm-password.html'

class ForgotPasswordView(TemplateView):
    template_name = 'forgot-password.html'


class ResetPasswordView(TemplateView):
    template_name = 'reset-password.html'

class SavatchaView(TemplateView):
    template_name = 'savatcha.html'

class AloqaView(FormView):
    template_name = 'aloqa.html'
    form_class = ContactForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


# -------------------- Auth



class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "register.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        super().form_valid(form)
        logout(self.request)
        return redirect("login")



class UserLoginView(LoginView):
    authentication_form = EmailLoginForm
    template_name = "login.html"
    redirect_authenticated_user = True




class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")

    def post(self, request):
        logout(request)
        return redirect("login")
