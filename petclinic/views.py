from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Owner
from .forms import OwnerForm

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
    return render(request, template_name="petclinic/owner_list.html", context=data)

def detail_owner(request, pk):
    obj = Owner.objects.get(pk=pk)
    pets = obj.pet_set.all()
    return render(request, "petclinic/owner.html", context={"owner":obj, "pets":pets})

def create_owner(request):
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            # obj = Owner()
            # obj.name = form.cleaned_data["name"]
            # obj.last_name = form.cleaned_data["last_name"]
            # obj.email = form.cleaned_data["email"]
            # obj.phone = form.cleaned_data["phone"]
            # obj.save()
            # alternatif yöntem
            #Owner.objects.create(**form.cleaned_data)
            # eğer model form kullanıldıysa 
            form.save()
            return HttpResponseRedirect("/owners")
    form = OwnerForm()
    return render(request, "petclinic/owner_form.html", context={"form":form})

