from django.urls import path
from .views import DoctorListView, DoctorDetailView, DoctorCreateView, DoctorUpdateView, DPListView
from . import views

urlpatterns = [
    path('', DoctorListView.as_view(), name='d_list'),
    path('<int:pk>/', DoctorDetailView.as_view(), name='d_detail'),
    path('new/', DoctorCreateView.as_view(), name='d_new'),
    path('<int:pk>/edit/', DoctorUpdateView.as_view(), name='d_edit'),
    path('sdlist/', DPListView.as_view(), name='dp_list'),
    path('query1/', views.query1, name='query1'),
    path('query2/', views.query2, name='query2'),
]