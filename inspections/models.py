from django.db import models
from django.contrib.auth.models import User, Group
from equipment.models import Equipment
from accounts.models import Company
from accounts.models import Person


class Inspection(models.Model):
    server_bt_id = models.IntegerField(default=None, blank=True, null=True)
    department = models.CharField(max_length=255, default="Inspection",
                                  choices=[('Inspection', 'Inspection'), ('Engineering', 'Engineering')])
    project_type = models.CharField(max_length=255, default="Inspection",
                                    choices=[('Equipment Inspection', 'Equipment Inspection'),
                                             ('Engineering Design', 'Engineering Design')])
    province = models.CharField(max_length=255, default="Alberta",
                                choices=[('Alberta', 'Alberta'), ('British Columbia', 'British Columbia'),
                                         ('Manitoba', 'Manitoba')])
    title = models.CharField(max_length=255, default="Inspection of")
    project_number = models.CharField(max_length=255, default="AE218")
    client = models.ForeignKey(Company, related_name="client", on_delete=models.CASCADE)
    owner = models.ForeignKey(Company, related_name="owner", on_delete=models.CASCADE)
    project_supervisor = models.ForeignKey(Person, related_name="supervisor", on_delete=models.CASCADE)
    client_contact = models.ForeignKey(Person, related_name="client_contact", on_delete=models.CASCADE)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    project_terms = models.CharField(max_length=255, default="Lump Sum",
                                     choices=[('Lump Sum', 'Lump Sum'), ('Monthly', 'Monthly')])
    purchase_order = models.CharField(max_length=255, default="PO")
    status = models.CharField(max_length=255, default="Active",
                              choices=[('Active', 'Active'), ('Not Started', 'Not Started'),
                                       ('Completed', 'Completed')])
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)

    def __str__(self):
        return self.project_number + " " + self.title

    class Meta:
        verbose_name = 'Inspection'
        verbose_name_plural = 'Inspections'
        ordering = ['-id']


class lstRoles(models.Model):
    role = models.CharField(max_length=255)


class lstPhase(models.Model):
    Phase = models.CharField(max_length=255)


class lstDocumentTypes(models.Model):
    DocumentType = models.CharField(max_length=255)


class InspectionImage(models.Model):
    inspection_image = models.ForeignKey(Inspection, related_name="image", on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')


class lsttaskcategory(models.Model):
    Name_id = models.IntegerField()
    Name = models.IntegerField()
    NameText = models.CharField(max_length=255)
    Abbr = models.CharField(max_length=255)


class lsttaskrelation(models.Model):
    Server_id = models.IntegerField()
    Name = models.IntegerField()
    NameText = models.CharField(max_length=255)


class lsttaskdescription(models.Model):
    Server_id = models.IntegerField()
    Name = models.IntegerField()
    NameText = models.CharField(max_length=255)
    Abbr = models.CharField(max_length=255)


class lsttaskdetail(models.Model):
    Server_id = models.IntegerField()
    Name = models.IntegerField()
    NameText = models.CharField(max_length=255)
    Abbr = models.CharField(max_length=255)


class lstunittype(models.Model):
    Server_id = models.IntegerField()
    Name = models.IntegerField()
    NameText = models.CharField(max_length=255)


class lstunit(models.Model):
    Server_id = models.IntegerField()
    Name = models.IntegerField()
    Type_id = models.ForeignKey(lstunittype, related_name="unittype", on_delete=models.CASCADE)
    NameText = models.CharField(max_length=255)


class ProjectTasks(models.Model):
    Server_id = models.IntegerField()
    ParentTask = models.IntegerField()
    Title = models.CharField(max_length=255)
    Level = models.IntegerField()
    Phase = models.ForeignKey(lstPhase, related_name="phase", on_delete=models.CASCADE)
    Category = models.ForeignKey(lsttaskcategory, related_name="category", on_delete=models.CASCADE)
    Description = models.ForeignKey(lsttaskdescription, related_name="description", on_delete=models.CASCADE)
    Detail = models.ForeignKey(lsttaskdetail, related_name="detail", on_delete=models.CASCADE)
    Resource = models.ForeignKey(Person, related_name="Resource", on_delete=models.CASCADE)
    Rate = models.DecimalField(max_digits=4, decimal_places=2)
    RateUnits = models.ForeignKey(lstunit, related_name="rateunits", on_delete=models.CASCADE)
    EstHours = models.DecimalField(max_digits=4, decimal_places=2)
    ActHours = models.DecimalField(max_digits=4, decimal_places=2)
    Comments = models.CharField(max_length=255)


class InspectionDocument(models.Model):
    inspection_document = models.ForeignKey(Inspection, related_name="document", on_delete=models.CASCADE)
    documenttype = models.ForeignKey(lstDocumentTypes, related_name="documenttype", on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    document = models.FileField(upload_to='images/')


class DocumentPermissions(models.Model):
    server_bt_id = models.IntegerField(default=None, blank=True, null=True)
    document = models.ForeignKey(InspectionDocument, on_delete=models.CASCADE)
    doc_request_company = models.ForeignKey(Company, related_name="doc_request_company", on_delete=models.CASCADE)
    doc_request_person = models.ForeignKey(Person, related_name="doc_request_person", on_delete=models.CASCADE)
    doc_authority_company = models.ForeignKey(Company, related_name="doc_authority_company", on_delete=models.CASCADE)
    doc_authority_person = models.ForeignKey(Person, related_name="doc_authority_person", on_delete=models.CASCADE)
    default_status = models.IntegerField()
    status = models.IntegerField()


class InspectionPermissions(models.Model):
    server_bt_id = models.IntegerField(default=None, blank=True, null=True)
    project = models.ForeignKey(Inspection, on_delete=models.CASCADE)
    proj_request_company = models.ForeignKey(Company, related_name="proj_request_company", on_delete=models.CASCADE)
    proj_request_person = models.ForeignKey(Person, related_name="proj_request_person", on_delete=models.CASCADE)
    proj_authority_company = models.ForeignKey(Company, related_name="proj_authority_company", on_delete=models.CASCADE)
    proj_authority_person = models.ForeignKey(Person, related_name="proj_authority_person", on_delete=models.CASCADE)
    default_status = models.IntegerField()
    status = models.IntegerField()
