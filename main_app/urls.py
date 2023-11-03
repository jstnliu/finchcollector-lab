from django.urls import path
from . import views

urlpatterns = [
    # FINCH FUNCTIONS
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
    # EGG FUNCTIONS
    path('finches/<int:finch_id>/assoc_egg/<int:egg_id>/', views.assoc_egg, name = 'assoc_egg'),
    path('finches/<int:finch_id>/unassoc_egg/<int:egg_id>/', views.unassoc_egg, name = 'unassoc_egg'),
    path('eggs/', views.EggList.as_view(), name = 'eggs_index'),
    path('eggs/<int:pk>/', views.EggDetail.as_view(), name = 'eggs_detail'),
    path('eggs/create/', views.EggCreate.as_view(), name = 'eggs_create'),
    path('eggs/<int:pk>/update/', views.EggUpdate.as_view(), name = 'eggs_update'),
    path('eggs/<int:pk>/delete/', views.EggDelete.as_view(), name = 'eggs_delete'),
]