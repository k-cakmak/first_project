from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index_page, name="home"),
    #path('owners/', views.list_owner, name="owners"),
    path('owners/', views.OwnerListView.as_view(), name="owner-list"),
    #path('owner/<int:pk>', views.detail_owner, name="detail-owner"),
    path('owner/<int:pk>', views.OwnerDetailView.as_view(), name="detail-owner"),
    #path('owner/', views.create_owner, name="owner"),
    path('owner/', views.OwnerCreateView.as_view(), name="owner-create"),
    # path('owner/update/<int:pk>', views.update_owner, name="updateowner"),
    path('owner/update/<int:pk>', views.OwnerUpdateView.as_view(), name="update-owner"),
    #path('owner/delete/<int:pk>', views.delete_owner, name="delete-owner"),
    path('owner/delete/<int:pk>', views.OwnerDeleteView.as_view(), name="delete-owner"),
    path('pet/', views.PetCreateView.as_view(), name="pet-create"),
    path('pet/<int:pk>', views.PetDetailView.as_view(), name="detail-pet"),
]
