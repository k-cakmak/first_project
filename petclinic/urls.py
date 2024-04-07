from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index_page, name="home"),
    path('owners/', views.list_owner, name="owners"),
    path('owner/<int:pk>', views.detail_owner, name="detail-owner"),
    path('owner/', views.create_owner, name="owner"),
    path('owner/update/<int:pk>', views.update_owner, name="updateowner"),
    path('owner/delete/<int:pk>', views.delete_owner, name="delete-owner"),
]
