from django.contrib import admin
from django.urls import path, include
from foodtaskerapp import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls import url

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^restaurant/sign-in/$', LoginView.as_view(template_name='restaurant/sign_in.html'), name = "restaurant-sign-in"),
    url(r'^restaurant/sign-out', LogoutView.as_view(next_page="/"), name = 'restaurant-sign-out'),
    url(r'^restaurant/sign-up', views.restaurant_sign_up, name = 'restaurant-sign-up'),
    url(r'^restaurant/$', views.restaurant_home, name = 'restaurant-home'),

    url(r'^api/social/', include('rest_framework_social_oauth2.urls')),

    url(r'^restaurant/account/$', views.restaurant_account, name = 'restaurant-account'),
    url(r'^restaurant/meals/$', views.restaurant_meals, name = 'restaurant-meals'),
    url(r'^restaurant/meals/add/$', views.restaurant_add_meals, name = 'restaurant-add-meals'),
    url(r'^restaurant/orders/$', views.restaurant_orders, name = 'restaurant-orders'),
    url(r'^restaurant/report/$', views.restaurant_report, name = 'restaurant-report'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
