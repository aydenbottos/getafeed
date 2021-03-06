from django.contrib import admin
from django.urls import path, include
from foodtaskerapp import views, apis
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
    url(r'^restaurant/meals/edit/(?P<meal_id>\d+)/$', views.restaurant_edit_meals, name = 'restaurant-edit-meals'),
    url(r'^restaurant/orders/$', views.restaurant_orders, name = 'restaurant-orders'),
    url(r'^restaurant/report/$', views.restaurant_report, name = 'restaurant-report'),

    url(r'^api/restaurant/order/notification/(?P<last_request_time>.+)/$', apis.restaurant_order_notification),
    url(r'^api/customer/restaurants/$', apis.customer_get_restaurant),
    url(r'^api/customer/meals/(?P<restaurant_id>\d+)/$', apis.customer_get_meals),
    url(r'^api/customer/order/add/$', apis.customer_add_order),
    url(r'^api/customer/order/latest/$', apis.customer_get_latest_order),

    # APIs for DRIVERS
    url(r'^api/driver/orders/ready/$', apis.driver_get_ready_orders),
    url(r'^api/driver/order/pick/$', apis.driver_pick_order),
    url(r'^api/driver/order/latest/$', apis.driver_get_latest_order),
    url(r'^api/driver/order/complete/$', apis.driver_complete_order),
    url(r'^api/driver/revenue/$', apis.driver_get_revenue),
    url(r'^api/driver/location/update/$', apis.driver_update_location),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
