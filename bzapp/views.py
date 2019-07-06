from django.shortcuts import render,HttpResponse,redirect
from bzapp.models import User,info,ip_info
from django.core.paginator import Paginator
import time


def regist(request):
    return render(request,'register.html')

def registlogic(request):
    name=request.POST.get('userid')
    phone=request.POST.get('usrtel')
    email=request.POST.get('email')
    pwd=request.POST.get('psw')
    print(name,phone,pwd,email)

    User.objects.create(name=name,phone=phone,email=email,password=pwd)
    return redirect('/login/')

def checkname(request):
    name = request.POST.get('username')
    usr = User.objects.filter(name=name)
    if usr:
        return HttpResponse('k')
    print(name)
    if name=='':
        return HttpResponse('a')
    elif len(name)>128:
        return HttpResponse('b')
    elif name[0].isdigit():
        return HttpResponse('c')
    else:
        return HttpResponse('d')

def checkphone(request):
    phone = request.POST.get('phone')

    print(phone)
    if phone=='':
        return HttpResponse('a')
    elif len(phone)==11 and  phone.isdigit():
        return HttpResponse('c')
    else:
        return HttpResponse('b')

def checkpwd(request):
    pwd = request.POST.get('pwd')
    print(pwd)
    if pwd=='':
        return HttpResponse('a')
    else:
        dd=0
        ff=0
        gg=0
        for i in pwd:
            if i.isupper():
                dd+=1
            elif i.islower():
                ff+=1
            elif i=='@':
                gg+=1
        if dd!=0 and ff!=0 or dd!=0 and gg!=0 or ff!=0 and gg!=0 or dd!=0 and gg!=0 and ff!=0:
             return HttpResponse('b')
        else:
            return HttpResponse('c')




def login(request):
    return render(request,'login.html')

def loginlogic(request):
    name = request.POST.get('userid')
    pwd = request.POST.get('psw')
    print(name,pwd)
    usr=User.objects.filter(name=name,password=pwd)
    if usr:
        request.session['login']='ok'
        return redirect('/mains/')


def checkuser(request):
    name=request.POST.get('username')
    pwd=request.POST.get('pwd')
    print(name,222,pwd)
    usr = User.objects.filter(name=name, password=pwd)
    if usr:
        return HttpResponse('a')
    else:
        return HttpResponse('b')


def mains(request):
    status=request.session.get('login')
    if status:
        return render(request,'main.html')
    return redirect('login')


def introduce(request):

    return render(request, 'introduce.html')




def menu(request):
    ip=request.META.get('REMOTE_ADDR')
    ip1=ip_info.objects.filter(ip=ip)
    app_time = time.time()
    if ip1:
        flag=ip1[0].flag
        if flag=='0':
            t1=ip1[0].apply_time
            cz=app_time-t1
            if cz>0.2:
                ip1[0].apply_time = app_time
                ip1[0].save()
                print(44444,cz)
            else:
                ip1[0].flag = '1'
                ip1[0].forbid_time = time.time()
                ip1[0].save()
                return HttpResponse('访问过于频繁！！')
        else:
            t1=ip1[0].forbid_time
            cz1=app_time-t1
            if cz1>10000:
                ip1[0].apply_time=app_time
                ip1[0].forbid_time=0
                ip1[0].flag='0'
                ip1[0].save()
            else:
                return HttpResponse('访问过于频繁！！')
    else:
        ip_info.objects.create(ip=ip,apply_time=app_time,flag='0')
        print(22222222222222222222)
    number = request.GET.get('num')
    c_p=request.GET.get('c_p')
    choice=request.GET.get('choice')
    city=request.GET.get('city')
    position2=request.GET.get('position')
    cityid=request.GET.get('parentID')
    position=request.GET.get('resourceName')
    if position2=='None' or position2 is None:
        position2=''
    if position is not None:
        print(122,type(position))
        if int(cityid) == 3 :
            city='北京'
        elif int(cityid) == 4:
            city='上海'
        elif int(cityid) == 5:
            city='广州'
        elif int(cityid) == 6:
            city='深圳'
        user=info.objects.filter(city__icontains=city,position__icontains=position)
    elif c_p=='城市':
        print(116)
        user=info.objects.filter(city__contains=choice)
    elif c_p=='职位':
        print(119)
        user = info.objects.filter(position__contains=choice)
    elif position2 :
        print(type(position2), 132)
        print(city)
        position = position2
        user = info.objects.filter(city__icontains=city, position__icontains=position2)
        print(user, 6666)

    else:
        user = info.objects.all()
        print(user, 222222222222222222)
    if not number or not number.isdigit() or int(number)<=0:
        number=1
    pagtor = Paginator(user, per_page=3)
    page = pagtor.page(number)
    count=pagtor.num_pages
    obj_num=pagtor.count
    status = request.session.get('login')
    if status:
        return render(request,'menu.html',{
            'page':page,
            'count':count,
            'obj':obj_num,
            'cp':c_p,
            'choice':choice,
            'city':city,
            'position':position,

                })
    return redirect('login')






# Create your views here.
