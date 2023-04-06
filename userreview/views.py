from django.shortcuts import render
from userreview.models import Review
from django.http import HttpResponseRedirect


# this is the feedback form page for users...
from django.views.decorators.cache import never_cache
from django.contrib import messages


@never_cache
def review(request, id):
    if 'user_{}_uname'.format(id) not in request.session and 'user_{}_upass'.format(id) not in request.session:
        return HttpResponseRedirect('/login/')
    elif 'user_{}_uname'.format(id) in request.session and 'user_{}_upass'.format(id) in request.session:
        username = request.session['user_{}_uname'.format(id)]
        password = request.session['user_{}_upass'.format(id)]
        url = "/dashboard/{}".format(id)
        data = {'un': username, 'url': url, 'id': id}

        if request.method == "POST":
            name = request.POST.get('username')
            review = request.POST.get('review')
            ratings = request.POST.get('ratings')
            data = Review(username=name, user_review=review, ratings=ratings)
            data.save()
            url = "/dashboard/{}".format(id)
            messages.success(request, 'your review is added successfully !')
            data = {'un': username,
                    'url': url, 'id': id}
        return render(request, 'reviewform.html', data)


@never_cache
def blog(request, id=None):
    if id == None:
        data = Review.objects.all()
        datamain = {'data': data}
        return render(request, 'blogs.html', datamain)
    else:
        if 'user_{}_uname'.format(id) in request.session and 'user_{}_uemail'.format(id) in request.session and 'user_{}_upass'.format(id) in request.session:
            data = Review.objects.all()
            url = "/dashboard/{}".format(id)
            datamain = {'data': data, 'id': id, 'url': url}
            return render(request, 'blogs2.html', datamain)
        else:
            return HttpResponseRedirect('/blogs/')

