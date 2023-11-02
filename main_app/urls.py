from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('finches/', views.finches_idx, name = 'index'),
    path('finches/<int:finch_id>/', views.finches_detail, name = 'detail'),
    # route to show form and create finch
    path('finches/create/', views.FinchCreate.as_view(), name = 'finches_create'),
    # edit made finches 
    path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name = 'finches_update'),
    # delete a finch
    path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name = 'finches_delete'),
    path('finches/<int:finch_id>/add_feeding/', views.add_feeding, name = 'add_feeding'),
]