from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from .models import Ad
from django.core.paginator import Paginator

def index(request):
    context = {}
    if request.method == "POST":
        if request.POST['city'] is None:
            print("City is not provided")
        else:
            filter_city = request.POST['city']
        print(request.POST['keywordhidden'])
        ads = Ad.objects.filter(location__contains=filter_city).filter(is_rejected=False).filter(is_approved=True)
        print(ads)
        recent = Ad.objects.filter(is_rejected=False).filter(is_approved=True).order_by('-id')[:10]
        paginator = Paginator(ads,8)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
        context["AD"] = posts
        context["RECENT"] = recent
        context["city"] = filter_city
        return render(request,'home.html',context=context)
    else:
        ads = Ad.objects.filter(is_rejected=False).filter(is_approved=True)
        print(ads)
        recent = Ad.objects.filter(is_rejected=False).filter(is_approved=True).order_by('-id')[:10]
        paginator = Paginator(ads,8)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
        context["AD"] = posts
        context["RECENT"] = recent
        return render(request,'home.html',context=context)

def index_keyword(request):
    context = {}
    if request.method == "POST":
        filter_keyword = request.POST['keyword']
        ads = Ad.objects.filter(title__contains=filter_keyword).filter(is_rejected=False).filter(is_approved=True)
        print(ads)
        recent = Ad.objects.filter(is_rejected=False).filter(is_approved=True).order_by('-id')[:10]
        paginator = Paginator(ads,8)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
        context["AD"] = posts
        context["RECENT"] = recent
        context["keyword"] = filter_keyword
        return render(request,'home.html',context=context)
    else:
        ads = Ad.objects.filter(is_rejected=False).filter(is_approved=True)
        print(ads)
        recent = Ad.objects.filter(is_rejected=False).filter(is_approved=True).order_by('-id')[:10]
        paginator = Paginator(ads,8)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
        context["AD"] = posts
        context["RECENT"] = recent
        return render(request,'home.html',context=context)
def ad_details(request,id):
    ads = Ad.objects.get(id=id)  
    print(ads.users)  
    return render(request, 'ad-details.html',{"ad":ads})

@login_required
def admin_details(request,id):
    ads = Ad.objects.get(id=id)
    return render(request, 'ad-details-admin.html',{"AD":ads})

@login_required
def sell(request):
    return render(request, 'sell.html')

@login_required
def admin_view(request):
    ads = Ad.objects.filter(is_approved=False)
    dictt = {}
    dictt["AD"]=ads
    return render(request, 'admin-profile.html',dictt)

@login_required
def approved(request,id):
    ads = Ad.objects.get(id=id)
    ads.is_approved= True
    ads.is_rejected= False
    print(ads.users.id)
    ads.save()
    ads = Ad.objects.filter(is_approved=False).filter(is_rejected=False)
    dictt = {}
    dictt["AD"]=ads
    return render(request, 'admin-profile.html',dictt)

@login_required
def rejected(request,id):
    ads = Ad.objects.get(id=id)
    ads.is_approved= False
    ads.is_rejected= True
    ads.save()
    ads = Ad.objects.filter(is_approved=False).filter(is_rejected=False)
    dictt = {}
    dictt["AD"]=ads
    return render(request, 'admin-profile.html',dictt)

@login_required
def save_item(request):
    mytitle = request.POST['title']
    print(request.POST['category'])
    print(request.FILES['image'])
    obj = Ad.objects.create(title=mytitle,category=request.POST['category'],location=request.POST['state'],price=request.POST['price'],image=request.FILES['image'],description=request.POST['description'],users=request.user)
    return render(request, 'sell.html')

@login_required
def log_out(request):
    logout(request)      
    return render(request, 'home.html')