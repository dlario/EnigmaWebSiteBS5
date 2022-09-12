from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Inspection
from .filters import InspectionFilter
from equipment.models import Equipment
from accounts.models import Company, Person
from inspections.forms import InspectionFilterFormHelper, InspectionForm, ProjectLookupFormHelper
from django.utils import timezone, html
from django.views.generic import FormView, TemplateView, ListView
from django_tables2 import RequestConfig, SingleTableView, Table, LinkColumn, Column, CheckBoxColumn, FileColumn, TemplateColumn
from django_tables2.utils import A
from django.utils.html import format_html

from sqlalchemy import update, Table, Column, DateTime, Integer, String, Text, Date, Boolean, Numeric, MetaData, ForeignKey, create_engine, exists
from sqlalchemy.orm import aliased, Query, joinedload, lazyload, subqueryload, join, outerjoin, sessionmaker
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

from inspections.forms import Project, CreditCardForm, CartForm, Address
#def home(request):
#    inspection = Inspection.objects
#    return render(request, 'inspections/home.html',{'inspections':inspection})

class MainView(FormView):
    template_name = 'inspections/create.html'
    form_class = Project

class BookView(FormView):
    template_name = 'inspections/bookinspection.html'
    form_class = Project


class InspectionTable(Table):
    def render_name(self, value, record):
        #url = record.get_absolute_url()
        url = "/aboutus/engineering"
        edit_entries = TemplateColumn('<a href="/inspection/detail/{{record.id}}">Edit</a>')


        return html.mark_safe('<a href="%s">%s</a>' % (url, record))


    class Meta:
        model = Inspection
        name = LinkColumn('project_number2',
                          text='static text',
                          attrs={'a': {'style': 'color: red;'}}
                          )
        fields = ['project_number', 'title', 'owner']
        #template_name = 'django_tables2/table.html'
        #template_name = 'django_tables2/bootstrap4.html'
        template_name = 'django_tables2/bootstrap-responsive.html'
        #template_name = 'django_tables2/semantic.html'
        row_attrs = {
            'data-href': lambda record: record.pk,
            'href': '/aboutus/engineering'
                }

class ImageColumn(Column):
        def render(self, value):
            return format_html('<img src="/media/img/{}.jpg" />', value)


class InspectionTableView(TemplateView):
    template_name = 'inspections/inspectionfiltertable.html'

    def get_queryset(self, **kwargs):
        return Inspection.objects.all()

    def get_context_data(self, **kwargs):
        context = super(InspectionTableView, self).get_context_data(**kwargs)
        filter = InspectionFilter(self.request.GET, queryset=self.get_queryset(**kwargs))
        filter.form.helper = InspectionFilterFormHelper()
        table = InspectionTable(filter.qs)
        RequestConfig(self.request).configure(table)
        context['filter'] = filter
        context['table'] = table
        return context

class InspectionListView(ListView):
    template_name = 'inspections/inspectionfiltertable.html'
    model = Inspection

    def get_queryset(self, **kwargs):
        return Inspection.objects.all()
        #return Inspection.objects.filter(taxon="Cheloniidae")

    def get_context_data(self, **kwargs):
        context = super(InspectionListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class PagedFilteredTableView(SingleTableView):
    filter_class = None
    formhelper_class = None
    context_filter_name = 'filter'

    def get_queryset(self, **kwargs):
        qs = super(PagedFilteredTableView, self).get_queryset()
        self.filter = self.filter_class(self.request.GET, queryset=qs)
        self.filter.form.helper = self.formhelper_class()
        return self.filter.qs

    def get_table(self, **kwargs):
        table = super(PagedFilteredTableView, self).get_table()
        RequestConfig(self.request, paginate={"per_page": self.paginate_by}).configure(table)
        return table

    def get_context_data(self, **kwargs):
        context = super(PagedFilteredTableView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        return context

def index(request):
    return render (request, 'inspections/index.html')

def projectlist(request):
    return render (request, 'inspections/projectlist.html')

def create(request):
    if request.method == 'POST':
        if request.POST['title']:
            inspection = Inspection()
            inspection.inspector = request.POST['title']
            inspection.department = request.POST['department']
            inspection.project_type = request.POST['project_type']
            inspection.province = request.POST['province']
            inspection.title = request.POST['title']
            inspection.project_number = request.POST['project_number']
            inspection.client = Company.objects.get(id = request.POST['client'])
            inspection.owner = Company.objects.get(id = request.POST['owner'])
            inspection.project_supervisor = Person.objects.get(id = request.POST['project_supervisor'])
            inspection.client_contact = Person.objects.get(id = request.POST['client_contact'])
            inspection.start_date = timezone.datetime.now()
            inspection.end_date = request.POST['end_date']
            inspection.project_terms = request.POST['project_terms']
            inspection.purchase_order = request.POST['purchase_order']
            inspection.status = request.POST['status']
            inspection.equipment =  Equipment.objects.get(id = request.POST['equipment'])
            inspection.createdby = request.user

            inspection.save()
            #return redirect('/inspections/' + str(inspection.id))
            return render(request, 'inspections/inspections.html')
        else:
            return render(request, 'inspections/inspections.html')
    else:
        return render(request, 'inspections/inspections.html')


def inspections(request):
    inspections = Inspection.objects
    return render(request, 'inspections/inspections.html',{'inspections':inspections})

def detail(request, inspection_id):
    inspection = get_object_or_404(Inspection, pk=inspection_id)
    if True:
        return render(request, 'inspections/detail.html', {'inspection':inspection})
    else:
        return render(request, 'inspections/inspections.html')


@login_required(login_url="/accounts/signup")
def bookinspection(request, equipment_id):
    if request.method == 'POST':
        product = get_object_or_404(Inspection, pk=equipment_id)
        product.save()
        return redirect('/equipment/' + str(equipment_id))


class FooTableView(PagedFilteredTableView):
    model = Inspection
    table_class = InspectionTable
    paginate_by = 5
    filter_class = InspectionFilter
    formhelper_class = InspectionFilterFormHelper
    search_class = CreditCardForm
    projecthelper_class = ProjectLookupFormHelper
    template_name = 'inspections/inspectionfiltertable.html'