# import all basic rendering and redirecting modules...
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect

# datetime module is used for deal with dates..
from datetime import datetime as dt

# this are all our models which we used in this section..
from hotellist.models import Hotellist
from mainapp.models import Login

# we dont required this 2 models here ...
# from mainapp.models import Login
# from bookings.models import Bookinghotel
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required


@never_cache
def hotellist(request, hotelstate, id):
    if (
        'user_{}_uname'.format(id) not in request.session
        and 'user_{}_upass'.format(id) not in request.session
        and 'user_{}_uemail'.format(id) not in request.session
    ):
        return HttpResponseRedirect('/login/')

    elif (
        'user_{}_uname'.format(id) in request.session
        and 'user_{}_upass'.format(id) in request.session
        and 'user_{}_uemail'.format(id) in request.session
    ):
        user = Login.objects.get(
            username=request.session.get('user_{}_uname'.format(id)),
            email=request.session.get('user_{}_uemail'.format(id)),
            password=request.session.get('user_{}_upass'.format(id)),
        )
        username = user.username
        password = user.password
        if Login.objects.filter(username=username, password=password).exists():
            if hotelstate == 'all':
                data = Hotellist.objects.all().order_by('?')
            elif hotelstate == 'others':
                data = (Hotellist.objects.filter(state='gujrat' ) | Hotellist.objects.filter(state='laddakh')).order_by('?')
            else:
                data = Hotellist.objects.filter(state=hotelstate).order_by('?')
            url = '/dashboard/{}'.format(id)
            # this is for showing the user name in place of dashboard button after login ....
            dash_board_name = username[0:7]
            datamain = {
                'un': username,
                'pw': password,
                'url': url,
                'data': data,
                'id': id,
                'dn': dash_board_name,
                'hstate': hotelstate,
            }
            # print('-------------------------------------------------------------------------------------------')
            # for d in data:
            #     print(d.name )
            # print('-------------------------------------------------------------------------------------------')
            return render(request, 'hotellist.html', datamain)
        return render(request, 'hotellist.html', datamain)
