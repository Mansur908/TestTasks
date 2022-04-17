from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.dateparse import parse_date
from django.views import View
from django.shortcuts import redirect

from tableApp.models import Data


class MainPageView(View):

    def get(self, request):
        return render(request, 'page.html',{"result": Data.objects.filter()})

    def post(self, request):
        column = request.POST.get('column')
        condition = request.POST.get('condition')
        value = request.POST.get('value')
        sort = request.POST.get('sort')
        try:
            if column == 'date':
                date = parse_date(value)
                if not date:
                    result = Data.objects.filter()
                if condition in ['equals','contains'] :
                    result = Data.objects.filter(date=date)
                if condition == 'over':
                    result = Data.objects.all().order_by('date').filter(date__gt=date)
                if condition == 'less':
                    result = Data.objects.all().order_by('date').filter(date__lt=date)
            elif column == 'name':
                if condition == 'equals':
                    result = Data.objects.filter(name=value)
                if condition == 'contains':
                    result = Data.objects.filter(name__contains=value)
                if condition == 'over':
                    result = Data.objects.all().order_by('name').filter(name__gt=value)
                if condition == 'less':
                    result = Data.objects.all().order_by('name').filter(name__lt=value)
            elif column == 'quantity':
                if condition in ['equals','contains']:
                    result = Data.objects.filter(quantity=value)
                if condition == 'over':
                    result = Data.objects.filter(quantity__gt=value)
                if condition == 'less':
                    result = Data.objects.filter(quantity__lt=value)
            elif column == 'distance':
                if condition in ['equals', 'contains']:
                    result = Data.objects.filter(distance=value)
                if condition == 'over':
                    result = Data.objects.filter(distance__gt=value)
                if condition == 'less':
                    result = Data.objects.filter(distance__lt=value)
            else:
                result = Data.objects.all()

            result = list(result.order_by(sort).values())
        except:
            result = ""

        return JsonResponse(result, status=200, safe=False)


def view_404(request, exception=None):
    return redirect('/')