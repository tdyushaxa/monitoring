import math
from django.db.models import Avg
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.decorators import login_required

from django.views import View

from .models import Device, DeviceInformation
from .forms import UpdateForm


# Create your views here.


def ComputerPageView(request):
    model = Device.objects.get(name__contains='Kompyuterlar')
    info = model.deviceinformation_set.all()
    today = timezone.now()
    week_start = today - timedelta(days=30)
    week_end = week_start + timedelta(days=30)
    weekly_updates = info.filter(timestamp__range=[week_start, week_end])
    month5 = [x.percentage for x in weekly_updates][:5]
    month10 = [x.percentage for x in weekly_updates][5:10]
    month15 = [x.percentage for x in weekly_updates][10:15]
    month20 = [x.percentage for x in weekly_updates][15:20]
    month25 = [x.percentage for x in weekly_updates][20:25]
    month30 = [x.percentage for x in weekly_updates][25:30]
    combined_lists = zip(month5, month10, month15, month20, month25, month30)
    data = [sum(values) / len(values) for values in combined_lists]
    ummumiy_son = info.aggregate(Avg('total'), Avg('percentage'))
    total = math.floor(ummumiy_son['total__avg'])
    percentage = math.floor(ummumiy_son['percentage__avg'])
    return render(request, 'index.html',
                  context={'info': info, 'weak': weekly_updates, 'total': total, 'percentage': percentage,
                           'data': data})


def ComputerHaftaPageView(request):
    model = Device.objects.get(name__contains='Kompyuterlar')
    info = model.deviceinformation_set.all()
    today = timezone.now()
    week_start = today - timedelta(days=7)
    week_end = week_start + timedelta(days=7)
    weekly_updates = info.filter(update_at__range=[week_start, week_end])
    data = [x.percentage for x in weekly_updates][:7]
    ummumiy_son = weekly_updates.aggregate(Avg('total'), Avg('percentage'))
    total = math.floor(ummumiy_son['total__avg'])
    percentage = math.floor(ummumiy_son['percentage__avg'])
    return render(request, 'computer-hafta.html',
                  context={'info': info, 'weak': weekly_updates, 'total': total, 'percentage': percentage,
                           'data': data})


def PrinterPageView(request):
    model = Device.objects.get(name__contains='Printerlar')
    info = model.deviceinformation_set.all()
    today = timezone.now()
    week_start = today - timedelta(days=30)
    week_end = week_start + timedelta(days=30)
    weekly_updates = info.filter(timestamp__range=[week_start, week_end])
    month5 = [x.percentage for x in weekly_updates][:5]
    month10 = [x.percentage for x in weekly_updates][5:10]
    month15 = [x.percentage for x in weekly_updates][10:15]
    month20 = [x.percentage for x in weekly_updates][15:20]
    month25 = [x.percentage for x in weekly_updates][20:25]
    month30 = [x.percentage for x in weekly_updates][25:30]
    combined_lists = zip(month5, month10, month15, month20, month25, month30)
    data = [sum(values) / len(values) for values in combined_lists]
    ummumiy_son = info.aggregate(Avg('total'), Avg('percentage'))
    total = math.floor(ummumiy_son['total__avg'])
    percentage = math.floor(ummumiy_son['percentage__avg'])
    return render(request, 'printer.html',
                  context={'info': info, 'weak': weekly_updates, 'total': total, 'percentage': percentage,
                           'data': data})


def PrinterHaftaPageView(request):
    model = Device.objects.get(name__contains='Printerlar')
    info = model.deviceinformation_set.all()
    today = timezone.now()
    week_start = today - timedelta(days=7)
    week_end = week_start + timedelta(days=7)
    weekly_updates = info.filter(update_at__range=[week_start, week_end])
    data = [x.percentage for x in weekly_updates][:7]
    ummumiy_son = weekly_updates.aggregate(Avg('total'), Avg('percentage'))
    total = math.floor(ummumiy_son['total__avg'])
    percentage = math.floor(ummumiy_son['percentage__avg'])
    return render(request, 'printer-hafta.html',
                  context={'info': info, 'weak': weekly_updates, 'total': total, 'percentage': percentage,
                           'data': data})


def ProektorPageView(request):
    model = Device.objects.get(name__contains='Proyektorlar')
    info = model.deviceinformation_set.all()
    today = timezone.now()
    week_start = today - timedelta(days=30)
    week_end = week_start + timedelta(days=30)
    weekly_updates = info.filter(update_at__range=[week_start, week_end])
    month5 = [x.percentage for x in weekly_updates][:5]
    month10 = [x.percentage for x in weekly_updates][5:10]
    month15 = [x.percentage for x in weekly_updates][10:15]
    month20 = [x.percentage for x in weekly_updates][15:20]
    month25 = [x.percentage for x in weekly_updates][20:25]
    month30 = [x.percentage for x in weekly_updates][25:30]
    combined_lists = zip(month5, month10, month15, month20, month25, month30)
    data = [sum(values) / len(values) for values in combined_lists]
    ummumiy_son = info.aggregate(Avg('total'), Avg('percentage'))
    total = math.floor(ummumiy_son['total__avg'])
    percentage = math.floor(ummumiy_son['percentage__avg'])
    return render(request, 'proektor.html',
                  context={'info': info, 'weak': weekly_updates, 'total': total, 'percentage': percentage,
                           'data': data})


def ProyektorHaftaPageView(request):
    model = Device.objects.get(name__contains='Proyektorlar')
    info = model.deviceinformation_set.all()
    today = timezone.now()
    week_start = today - timedelta(days=7)
    week_end = week_start + timedelta(days=7)
    weekly_updates = info.filter(update_at__range=[week_start, week_end])
    data = [x.percentage for x in weekly_updates][:7]
    ummumiy_son = weekly_updates.aggregate(Avg('total'), Avg('percentage'))
    total = math.floor(ummumiy_son['total__avg'])
    percentage = math.floor(ummumiy_son['percentage__avg'])
    return render(request, 'proyektor-hafta.html',
                  context={'info': info, 'weak': weekly_updates, 'total': total, 'percentage': percentage,
                           'data': data})


def WifiPageView(request):
    model = Device.objects.get(name__contains='Wifi router')
    info = model.deviceinformation_set.all()
    today = timezone.now()
    week_start = today - timedelta(days=30)
    week_end = week_start + timedelta(days=30)
    weekly_updates = info.filter(update_at__range=[week_start, week_end])
    month5 = [x.percentage for x in weekly_updates][:5]
    month10 = [x.percentage for x in weekly_updates][5:10]
    month15 = [x.percentage for x in weekly_updates][10:15]
    month20 = [x.percentage for x in weekly_updates][15:20]
    month25 = [x.percentage for x in weekly_updates][20:25]
    month30 = [x.percentage for x in weekly_updates][25:30]
    combined_lists = zip(month5, month10, month15, month20, month25, month30)
    data = [sum(values) / len(values) for values in combined_lists]
    ummumiy_son = info.aggregate(Avg('total'), Avg('percentage'))
    total = math.floor(ummumiy_son['total__avg'])
    percentage = math.floor(ummumiy_son['percentage__avg'])
    return render(request, 'wifi.html',
                  context={'info': info, 'weak': weekly_updates, 'total': total, 'percentage': percentage,
                           'data': data})


def WifiHaftaPageView(request):
    model = Device.objects.get(name__contains='Wifi router')
    info = model.deviceinformation_set.all()
    today = timezone.now()
    week_start = today - timedelta(days=7)
    week_end = week_start + timedelta(days=7)
    weekly_updates = info.filter(update_at__range=[week_start, week_end])
    data = [x.percentage for x in weekly_updates][:7]
    ummumiy_son = weekly_updates.aggregate(Avg('total'), Avg('percentage'))
    total = math.floor(ummumiy_son['total__avg'])
    percentage = math.floor(ummumiy_son['percentage__avg'])
    return render(request, 'wifi_hafta.html',
                  context={'info': info, 'weak': weekly_updates, 'total': total, 'percentage': percentage,
                           'data': data})


def CameraPageView(request):
    model = Device.objects.get(name__contains='Kameralar')
    info = model.deviceinformation_set.all()
    today = timezone.now()
    week_start = today - timedelta(days=30)
    week_end = week_start + timedelta(days=30)
    weekly_updates = info.filter(update_at__range=[week_start, week_end])
    month5 = [x.percentage for x in weekly_updates][:5]
    month10 = [x.percentage for x in weekly_updates][5:10]
    month15 = [x.percentage for x in weekly_updates][10:15]
    month20 = [x.percentage for x in weekly_updates][15:20]
    month25 = [x.percentage for x in weekly_updates][20:25]
    month30 = [x.percentage for x in weekly_updates][25:30]
    combined_lists = zip(month5, month10, month15, month20, month25, month30)
    data = [sum(values) / len(values) for values in combined_lists]
    ummumiy_son = info.aggregate(Avg('total'), Avg('percentage'))
    total = math.floor(ummumiy_son['total__avg'])
    percentage = math.floor(ummumiy_son['percentage__avg'])
    return render(request, 'camera.html',
                  context={'info': info, 'weak': weekly_updates, 'total': total, 'percentage': percentage,
                           'data': data})


def CameraHaftaPageView(request):
    model = Device.objects.get(name__contains='Kameralar')
    info = model.deviceinformation_set.all()
    today = timezone.now()
    week_start = today - timedelta(days=7)
    week_end = week_start + timedelta(days=7)
    weekly_updates = info.filter(update_at__range=[week_start, week_end])
    data = [x.percentage for x in weekly_updates][:7]
    ummumiy_son = weekly_updates.aggregate(Avg('total'), Avg('percentage'))
    total = math.floor(ummumiy_son['total__avg'])
    percentage = math.floor(ummumiy_son['percentage__avg'])
    return render(request, 'camera-hafta.html',
                  context={'info': info, 'weak': weekly_updates, 'total': total, 'percentage': percentage,
                           'data': data})



@login_required
def UPdateView(request):
    selected = request.GET.get('select')
    natija = str(selected) if selected else 'Kameralar'
    model = Device.objects.get(name__contains=natija)
    info = model.deviceinformation_set.all().last()
    form = UpdateForm(instance=info)
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=info)
        yangi = int(request.POST.get('new'))
        tamir = int(request.POST.get('tamir'))
        broken = int(request.POST.get('broken'))
        if form.is_valid():
            update = form.save(commit=False)
            if yangi:
                update.total +=yangi
                update.save()
            if tamir:
                update.total += tamir
                update.save()
            if broken:
                update.total -= broken
                update.save()
            update.save()
            return redirect('main:update')
    return render(request, 'update.html', {'form': form,'natija':natija})
