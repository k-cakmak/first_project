from django.shortcuts import render
from .models import Owner

# from django.template import loader
# from django.http import HttpResponse

# Create your views here.
# def index_page(request):
#     template = loader.get_template('index.html')
#     return HttpResponse(template.render())

def index_page(request):
    return render(request, template_name="index.html", context={})

def list_owner(request):
    all_objects = Owner.objects.all()
    data = {"objects":all_objects}
    return render(request, template_name="owner_list.html", context=data)