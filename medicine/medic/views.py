from django.shortcuts import redirect,render,get_object_or_404
from django.contrib.auth.decorators import login_required


def base(request):
    return render(request,'base.html')


@login_required
def news(request):
    return render(request,'news_medic.html')