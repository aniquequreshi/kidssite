from django.shortcuts import get_object_or_404, get_list_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django_filters.views import FilterView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin

from kidsapp.models import Denial
from kidsapp.forms import DenialForm
from kidsapp.filters import DenialFilter

import csv, io
from django.contrib import messages


# Create your views here.
def index_view(request):
    return render(request, 'kidsapp/index.html')

@login_required
@permission_required('kidsapp.delete_denial')
def denial_delete_archive(request):
    Denial.objects.filter(status='Archive').delete()
    template = "kidsapp/denial_upload.html"
    success_url = reverse_lazy('denial-list')  # was denial-list
    context = {}
    return render(request, template, context)

@login_required
@permission_required('kidsapp.create_denial')
def denial_upload(request):
    # declaring template
    template = "kidsapp/denial_upload.html"
    data = Denial.objects.all()
    # prompt is a context variable that can have different values      depending on their context
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.txt'):
        messages.error(request, 'THIS IS NOT A TXT FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter='\t', quotechar="|"):
        _, created = Denial.objects.update_or_create(
            visit_id=column[0],
            reason_code=column[1],
            reason=column[2].split(': ', 1)[1],
            carrier_code=column[3].split(' - ', 1)[0],
            carrier=column[3].split(' - ', 1)[1],
            date_of_service=column[4],
            procedure = column[5],
            date_of_denial = column[6],
            amount = column[7]
        )
    context = {}
    return render(request, template, context)


# class DenialListView(ListView):
class DenialListView(PermissionRequiredMixin, FilterView):
    model = Denial
    permission_required = ('kidsapp.view_denial')

    def get_queryset(self):
        query_set = self.model.objects.all()
        denial_filtered_list = DenialFilter(self.request.GET, queryset=query_set)
        return denial_filtered_list.qs


# class DenialDetailView(DetailView):
#     model = Denial

class DenialCreateView(PermissionRequiredMixin, CreateView):
    model = Denial
    form_class = DenialForm
    permission_required = ('kidsapp.add_denial')
    # permission_denied_message = "You are not allowed here."


class DenialUpdateView(PermissionRequiredMixin, UpdateView):
    model = Denial
    form_class = DenialForm
    permission_required = ('kidsapp.change_denial')
    # fields = '__all__'
    success_url = reverse_lazy('denial-list')  # was denial-list


class DenialDeleteView(PermissionRequiredMixin, DeleteView):
    model = Denial
    success_url = reverse_lazy('denial-list')  # was denial-list
    permission_required = ('kidsapp.delete_denial')