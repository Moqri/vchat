from django.shortcuts import render

from .models import User


def index(request):
    user_list = User.objects.all()
    context = {
        'user_list': user_list,
    }
    return render(request ,'main_app/index.html',context)