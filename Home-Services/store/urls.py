from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views
from .views.home import Index, store
from .views.signup import Signup
# from .views.signup1 import Signup1
from .views.login import Login, logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .middlewares.auth import auth_middleware
from .views.about import About
from .views import *
from .views.signup_service_provider import Signup1
from .views.feedback import Feedback
from .views.contact import contact_form
from .views.orders import edit_order, cancel_order, order_complete



urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store', store, name='store'),

    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('cart', auth_middleware(Cart.as_view()), name='cart'),
    path('check-out', CheckOut.as_view(), name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('about', About.as_view(), name='about'),
    path('signup1', Signup1.as_view(), name='signup1'),
    #path('feedback', Feedback.as_view(), name='feedback'),
    path('contact', contact_form, name='contact'),
    path('Feedback', Feedback, name='Feedback'),
    path('edit_order/<int:pk>', edit_order, name='edit_order'),
    path('order_complete/<int:pk>', order_complete, name='order_complete'),
    path('cancel_order/<int:pk>', cancel_order, name='cancel_order'),
    #path('signups', views.signups, name='signups'),
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="registration/password_reset_form.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"), 
        name="password_reset_complete"),

]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

