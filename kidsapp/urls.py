from django.urls import path
from . import views

from kidsapp.views import DenialListView, DenialCreateView, DenialUpdateView, DenialDeleteView, index_view, denial_upload, denial_delete_archive

from django_filters.views import FilterView
from kidsapp.filters import DenialFilter

urlpatterns = [
path('', views.index_view, name='index'),
path('denial/create/', DenialCreateView.as_view(), name ='denial-create'),
# path('denial/<int:pk>/', DenialDetailView.as_view(), name ='denial-detail'),
path('denial/delete/<int:pk>/', DenialDeleteView.as_view(), name ='denial-delete'),
path('denial/update/<int:pk>/', DenialUpdateView.as_view(), name='denial-update'),
path('denial/list/', DenialListView.as_view(filterset_class=DenialFilter), name='denial-list'),
# path('denial/list/<str:search_parameter>/', DenialListView.as_view(), name='denial-list'),
# path('search/', FilterView.as_view(filterset_class=DenialFilter, template_name='search/denial_list.html'), name='search'),
path('denial/upload/', denial_upload, name="denial-upload"),
path('denial/delete-archive/', denial_delete_archive, name="denial-delete-archive"),
# path('up/', simple_upload, name="simple_upload"),
]