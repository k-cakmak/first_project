from django.shortcuts import render
# from django.template import loader
# from django.http import HttpResponse

# Create your views here.
# def index_page(request):
#     template = loader.get_template('index.html')
#     return HttpResponse(template.render())

def index_page(request):
    return render(request, template_name="index.html", context={})
