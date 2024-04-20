from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#from django.views.generic.detail import DetailView
from .models import Owner, Pet
#from .forms import OwnerForm

# from django.template import loader
# from django.http import HttpResponse

# Create your views here.
# def index_page(request):
#     template = loader.get_template('index.html')
#     return HttpResponse(template.render())

def index_page(request):
    return render(request, template_name="index.html", context={})

# def list_owner(request):
#     all_objects = Owner.objects.all()
#     data = {"object_list":all_objects}
#     return render(request, template_name="petclinic/owner_list.html", context=data)

class OwnerListView(ListView):
    model = Owner
    #ordering = ("name", "last_name")
    ordering = "-name"

# def detail_owner(request, pk):
#     obj = Owner.objects.get(pk=pk)
#     pets = obj.pet_set.all()
#     return render(request, "petclinic/owner.html", context={"owner":obj, "pets":pets})

class OwnerDetailView(DetailView):
    model = Owner
    template_name = "petclinic/owner.html"

# def create_owner(request):
#     if request.method == 'POST':
#         form = OwnerForm(request.POST)
#         if form.is_valid():
#             # obj = Owner()
#             # obj.name = form.cleaned_data["name"]
#             # obj.last_name = form.cleaned_data["last_name"]
#             # obj.email = form.cleaned_data["email"]
#             # obj.phone = form.cleaned_data["phone"]
#             # obj.save()
#             # alternatif yöntem
#             #Owner.objects.create(**form.cleaned_data)
#             # eğer model form kullanıldıysa 
#             form.save()
#             return HttpResponseRedirect("/owners")
#     form = OwnerForm()
#     return render(request, "petclinic/owner_form.html", context={"form":form})

class OwnerCreateView(CreateView):
    model = Owner
    #fields = ["name", "last_name", "email"]
    fields = "__all__"
    success_url = "/owners"

# def update_owner(request, pk):
#     obj = Owner.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = OwnerForm(request.POST, instance=obj)
#         if form.is_valid():
#             form.save()
#             return redirect("/owners")
#     form = OwnerForm(instance=obj)
#     return render(request, "petclinic/owner_form.html", context={"form":form})

class OwnerUpdateView(UpdateView):
    model = Owner
    fields = "__all__"
    template_name_suffix = "_update_form"
    success_url = "/owners"

# def delete_owner(request, pk):
#     obj = Owner.objects.get(pk=pk)
#     if request.method == 'POST':
#         obj.delete()
#         return redirect("/owners")
#     return render(request, "petclinic/owner_delete.html", context={"owner":obj})

class OwnerDeleteView(DeleteView):
    model = Owner
    success_url = "/owners"
    template_name = "petclinic/owner_delete.html"

class PetCreateView(CreateView):
    model = Pet
    fields = "__all__"
    success_url = "/owners"

class PetDetailView(DetailView):
    model = Pet
