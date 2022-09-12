from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Div, Fieldset, HTML
from crispy_forms.bootstrap import (
    PrependedText, AppendedText, PrependedAppendedText, FormActions)
from equipment.models import Equipment
from inspections.models import Inspection


class Project(forms.ModelForm):
    # department = forms.ModelChoiceField(queryset=department.objects.all())
    class Meta:
        model = Inspection
        fields = ['department',
                  'project_type',
                  'province',
                  'title',
                  'project_number',
                  'client',
                  'owner',
                  'project_supervisor',
                  'client_contact',
                  'start_date',
                  'end_date',
                  'project_terms',
                  'purchase_order',
                  'status',
                  'equipment']

    def __init__(self, *args, **kwargs):
        super(Project, self).__init__(*args, **kwargs)

    # Uni-form
    helper = FormHelper()
    helper.form_method = 'POST'
    # helper.form_id = 'id-project'
    # action = "{% url 'home' %}"
    helper.form_action = 'create'
    # helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Div(
            Div('department', css_class='col-md-6'),
            Div('project_type', css_class='col-md-6'), css_class='row'),
        'province',
        Div(Div('project_number', css_class='col-md-6'),
            Div('title', css_class='col-md-6'), css_class='row'), \
        'client', \
        'owner', \
        'project_supervisor', \
        'client_contact', \
        'start_date', \
        'end_date', \
        'project_terms', \
        'purchase_order', \
        'status', \
        'equipment', \
        Submit('submit', 'Create Project', css_class="btn-primary"), \
        Submit('cancel', 'Cancel'),
    )


class BookInspection(forms.ModelForm):
    # department = forms.ModelChoiceField(queryset=department.objects.all())
    class Meta:
        model = Inspection
        fields = ['project_type',
                  'client',
                  'owner',
                  'client_contact',
                  'start_date',
                  'end_date',
                  'purchase_order',
                  'equipment']

    def __init__(self, *args, **kwargs):
        super(Project, self).__init__(*args, **kwargs)

    # Uni-form
    helper = FormHelper()
    helper.form_method = 'POST'
    # helper.form_id = 'id-project'
    # action = "{% url 'home' %}"
    helper.form_action = 'create'
    # helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Div(
            Div('project_type', css_class='col-md-6'), css_class='row'),
        Div(css_class='row'), \
        'client', \
        'owner', \
        'client_contact', \
        'start_date', \
        'purchase_order', \
        'equipment', \
        Submit('submit', 'Create Project', css_class="btn-primary"), \
        Submit('cancel', 'Cancel'),
    )


class InspectionForm(forms.Form):
    item = forms.CharField()
    quantity = forms.IntegerField(label="Qty")
    price = forms.DecimalField()


class InspectionFilterFormHelper(FormHelper):
    model = Inspection
    form_method = 'GET'
    form_tag = False
    form_show_labels = False
    layout = Layout(
        Div(
            Div('project_number__contains', css_class='col-md-5'),
            Div('client', css_class='col-md-5'),
            Div(Submit('submit', 'Apply Filter'), css_class='col-md-2'), css_class='row'), )


class ProjectLookupFormHelper(FormHelper):
    model = Inspection
    form_method = 'GET'
    form_tag = False
    form_show_labels = False
    layout = Layout(
        Div(
            Div('project_number__contains', css_class='col-md-5'),
            Div(Submit('submit', 'Look Up Project'), css_class='col-md-2'), css_class='row'), )


class Address(forms.Form):
    # Wrapping the fields "housenumber and addition". Assign extra class to the fields

    Project_Number = forms.CharField()

    description = forms.CharField(
        widget=forms.Textarea(),
    )

    radio_buttons = forms.ChoiceField(
        choices=(
            ('option_one', "Option one is this and that be sure to include why it's great"),
            ('option_two', "Option two can is something else and selecting it will deselect option one")
        ),
        widget=forms.RadioSelect,
        initial='option_two',
    )

    checkboxes = forms.MultipleChoiceField(
        choices=(
            ('option_one', "Option one is this and that be sure to include why it's great"),
            ('option_two', 'Option two can also be checked and included in form results'),
            ('option_three', 'Option three can yes, you guessed it also be checked and included in form results')
        ),
        initial='option_one',
        widget=forms.CheckboxSelectMultiple,
        help_text="<strong>Note:</strong> Labels surround all the options for much larger click areas and a more usable form.",
    )

    appended_text = forms.CharField(
        help_text="Here's more help text"
    )

    prepended_text = forms.CharField()

    prepended_text_two = forms.CharField()

    multicolon_select = forms.MultipleChoiceField(
        choices=(('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')),
    )

    # Uni-form
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('Project_Number', css_class='input-xlarge'),
        Field('description', rows="3", css_class='input-xlarge'),
        'radio_buttons',

        AppendedText('appended_text', '.00'),
        PrependedText('prepended_text', '<input type="checkbox" checked="checked" value="" id="" name="">',
                      active=True),
        PrependedText('prepended_text_two', '@'),
        'multicolon_select',
        FormActions(
            Submit('submit', 'Create Project', css_class="btn-primary"),
            Submit('cancel', 'Cancel'),
        )
    )


class CartForm(forms.Form):
    item = forms.CharField()
    quantity = forms.IntegerField(label="Qty")
    price = forms.DecimalField()

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.layout = Layout(
        'item',
        PrependedText('quantity', '#'),
        PrependedAppendedText('price', '$', '.00'),
        FormActions(Submit('login', 'login', css_class='btn-primary'))
    )


class CreditCardForm(forms.Form):
    fullname = forms.CharField(label="Full Name", required=True)
    card_number = forms.CharField(label="Card", required=True, max_length=16)
    expire = forms.DateField(label="Expire Date", input_formats=['%m/%y'])
    ccv = forms.IntegerField(label="ccv")
    notes = forms.CharField(label="Order Notes", widget=forms.Textarea())

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-sm-2'
    helper.field_class = 'col-sm-4'
    helper.layout = Layout(
        Field('fullname', css_class='input-sm'),
        Field('card_number', css_class='input-sm'),
        Field('expire', css_class='input-sm'),
        Field('ccv', css_class='input-sm'),
        Field('notes', rows=3),
        FormActions(Submit('purchase', 'purchase', css_class='btn-primary'))
    )
