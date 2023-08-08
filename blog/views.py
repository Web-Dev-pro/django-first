from django.shortcuts import render
from .models import *
from django.db.models import Q

def home(request):
    # category = request.GET.get('category')
    # if category == None:
    #     cards = Cards.objects.all()
    # else:
    #     cards = Cards.objects.filter(category__name = category)

    # search-start
    if 'q' in request.GET:
        search = request.GET['q']
        fulL_search = Q(Q(heading__icontains=search))
        cards = Cards.objects.filter(fulL_search)
    else:
        cards = Cards.objects.all()
    # search-end

    categories = Category.objects.all()
    context = {
        'cards': cards,
        'categories': categories
    }
    return render(request, 'index.html', context)





def andijon(request):
    return render(request, "andijon.html")

def fargona(request):
    fargona = Fargona.objects.all()
    context = {
        "fargona": fargona
    }
    return render(request, "fargona.html",context)

def foot(request):
    foot = Foot.objects.all()
    context = {
        'foots': foot
    }
    return render(request, 'foot.html',context)