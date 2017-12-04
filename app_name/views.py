# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from app_name.models import IMG


def index(request):
    return HttpResponse(
        u'{"Category":[{"categoryId":1,"categoryName":"饮品","categoryImage":"/upload/yinpin.jpg"},{"categoryId":2,"categoryName":"食品","categoryImage":"/upload/shiping.jpg"},{"categoryId":3,"categoryName":"酒类","categoryImage":"/upload/jiullei.jpg"}],"recommend":{"id":11,"productName":"统一老坛泡椒牛肉袋面香辣味110g*24袋","filenameSmall":"/upload/ty_ltpj_small.jpg","productPrice":48.0,"productCost":47.5}}')


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))


def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))


def old_add2_redirect(request, a, b):
    return HttpResponseRedirect(
        reverse('add2', args=(a, b))
    )


def home(request):
    list = map(str, range(100))
    return render(request, 'home.html', {'List': list})


def test(request):
    return render(request, 'test.html')


def upload_avatar(request):
    file_obj = request.FILES.get('avatar')
    file_path = os.path.join('static/images', file_obj.name)
    with open(file_path, 'wb') as f:
        for chunk in file_obj.chunks():
            f.write(chunk)

    return HttpResponse(file_path)


@csrf_exempt
def uploadImg(request):
    if request.method == 'POST':
        new_img = IMG(
            img=request.FILES.get('img'),
            name=request.FILES.get('img').name
        )
        new_img.save()
    return render(request, 'img_tem/uploadimg.html')


@csrf_exempt
def showImg(request):
    imgs = IMG.objects.all()
    content = {
        'imgs': imgs,
    }
    for i in imgs:
        print (i.img.url)
    return render(request, 'img_tem/showimg.html', content)
