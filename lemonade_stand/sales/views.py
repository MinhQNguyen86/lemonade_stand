from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import Staff, Product, Report


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'sales/index.html'
    context_object_name = 'staff_list'

    def get_queryset(self):
        """
        Return a list of staff names in descending order
        """
        return Staff.objects.order_by('-name')


def form(request):
    return render(request, 'sales/form.html', {
        'Product': Product.objects.all(),
        'Staff': Staff.objects.all(),
    })


def submission(request):
    try:
        prod = request.POST['products']
        quant = request.POST['quantity']
        date = request.POST['sale_date']
        staff = request.POST['staffs']
    except:
        return render(request, 'sales/form.html', {
            'error_message': "Please fill in all input fields",
            'Product': Product.objects.all(),
            'Staff': Staff.objects.all(),
        })
    else:
        p = quant * prod.price
        c = staff.commission * p
        try:
            r = Report.objects.get(staff=staff, date=date)
            r.items.add(prod)
        except (KeyError, Report.DoesNotExist):
            Report.objects.create(staff=staff, date=date, items=prod, price=p, commission=c)
        return HttpResponseRedirect(reverse('sales:form'))
        #return HttpResponseRedirect(reverse('sales:'))

def report(request):
    try:
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        staff = request.POST['staffs']

        od = Report.objects.filter(date__gte=start_date).filter(date__lte=end_date).order_by(-start_date)
        os = od.filter()
        return render(request, 'sales/report.html', {
            'Staff': Staff.objects.all(),
            'obj': od,
        })
    except KeyError:
