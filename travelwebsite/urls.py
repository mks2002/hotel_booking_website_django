from django.conf.urls.static import static
from django.conf import settings
# this 2 import is for using the media...


from django.contrib import admin
from django.urls import path


# here we import all the different views of our project...
# travelwebsite is the main project level application of this project which django by default create inside any project...
from mainapp import views as v1
from bookings import views as v2
from hotellist import views as v3
from travelwebsite import views as v4
from userreview import views as v5
from payments import views as v6


admin.site.site_header = 'Hotel administration and managment'
admin.site.site_title = 'Hotel administration and managment'
admin.site.index_title = 'Hotel administration and managment'


# for error page we dont create any url we just render it when any of the requested url is not match with this below defined error.....


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', v4.homepage, name='home'),
    path('<id>', v4.homepage, name='home'),

    path('about/', v4.about, name='about'),
    path('about/<id>', v4.about, name='about'),
    path('services/', v4.services, name='service'),
    path('services/<id>', v4.services, name='service'),
    path('pricings/', v4.price, name='price'),

    path('staffs/', v4.staffs, name='staffs'),
    path('staffs/<id>', v4.staffs, name='staffs'),
    path('travel_details/', v4.travel, name='travel'),
    path('travel_details/<id>', v4.travel, name='travel'),


    path('blogs/', v5.blog, name='blog'),
    path('blogs/<id>', v5.blog, name='blog'),

    path('review/<id>', v5.review, name='review'),
    path('memories/<id>', v5.memory, name='memory'),

    path('dashboard/<id>', v2.dashboard, name='dashboard'),
    path('bookings/<id>/', v2.bookings, name='booking'),
    path('dashboard/deleteConfirmation/', v2.delete_confirmation, name='delete'),
    path('dashboard/deleteConfirmation/delete/', v2.delete, name='delete'),

    path('quaries/<id>', v2.query, name='query'),
    path('details/', v2.details, name='order_details'),


    path('login/', v1.login, name='login'),
    path('login/<id>', v1.login, name='login'),
    # this is for update the password before login..
    path('update/', v1.update, name='update'),
    path('signup/', v1.signup, name='signup'),
    



    path('hotellist/<hotelstate>/<id>', v3.hotellist, name='hotellist'),


    path('payments/', v6.paymentpage, name='payment'),
    path('logout/<id>/', v1.logout_user, name='logout'),



]


# in all the urls which id we used that is basically the id for getting the session key ...

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


# this are the pages which comes after login ...

# booking.html
# dashboard.html
# hotellist.html
# reviewform.html
# order_detail.html

    # path('<id>', v4.homepageid, name='homeid'),
    # path('pricings/<id>', v4.priceid, name='priceid'),
    # path('error/',v2.errorpage,name='errorpage'),
