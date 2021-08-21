from typing import Any
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class Auditable(models.Model):
    ip = models.GenericIPAddressField(null=True)
    user_agent = models.CharField(max_length=255, blank=True)
    remote_host = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name="%(app_label)s_%(class)s_created_by", null=True, blank=True)  # this is for web user
    modified_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name="%(app_label)s_%(class)s_modified_by", null=True, blank=True)  # this is for web user

    class Meta:
        abstract = True

    def get_fields(self):
        list_fields = ['ip', 'user_agent',
                       'remote_host', 'created_by', 'modified_by']
        return [(field.verbose_name, field._get_val_from_obj(self)) for field in self.__class__._meta.fields if field.name not in list_fields and not
                (field.get_internal_type() == "DateTimeField" and
                 (field.auto_now is True or field.auto_now_add is True)) and
                field.concrete and (not field.is_relation or field.one_to_one or
                (field.many_to_one and field.related_model))]


class EntityTypeMaster(Auditable):
    entity_id = models.BigAutoField(primary_key=True)
    name_en = models.CharField(max_length=200)
    name_ma = models.CharField(max_length=200)
    table_name = models.CharField(max_length=200)
    condition = models.CharField(max_length=200)
# Return??
    def __str__(self):
        return str(self.entity_id) + ' - ' + self.name_ma


class StateMaster(Auditable):
    state_id = models.BigAutoField(primary_key=True)
    name_en = models.CharField("Name (En)", max_length=200, unique=True)
    name_ma = models.CharField("Name (Ma)", max_length=200, unique=True)

    def __str__(self):
        return str(self.state_id) + ' - ' + self.name_ma

    class Meta:
        ordering = ['state_id']


class DistrictMaster(Auditable):
    district_id = models.BigAutoField(primary_key=True)
    name_en = models.CharField("Name in English", max_length=200, unique=True)
    name_ma = models.CharField("Name in Marathi", max_length=200, unique=True)
    state_id = models.ForeignKey(StateMaster, on_delete=models.DO_NOTHING, verbose_name='State Name')

    def __str__(self):
        return str(self.district_id) + ' - ' + self.name_ma

    class Meta:
        ordering = ['district_id']


class TalukaMaster(Auditable):
    taluka_id = models.BigAutoField(primary_key=True)
    name_en = models.CharField("Name in English", max_length=200, unique=True)
    name_ma = models.CharField("Name in Marathi", max_length=200, unique=True)
    district_id = models.ForeignKey(DistrictMaster, on_delete=models.DO_NOTHING, verbose_name='District Name')

    def __str__(self):
        return str(self.taluka_id) + ' - ' + self.name_ma

    class Meta:
        ordering = ['taluka_id']


class VillageMaster(Auditable):
    village_id = models.BigAutoField(primary_key=True)
    name_en = models.CharField("Name in English", max_length=200, unique=True)
    name_ma = models.CharField("Name in Marathi", max_length=200, unique=True)
    pin_code = models.IntegerField('Pin Code Number', null=True, blank=True)
    taluka = models.ForeignKey(TalukaMaster, on_delete=models.DO_NOTHING, verbose_name='Taluka Name')
    command_area_ind = models.CharField("command area index", max_length=1)

    def __str__(self):
        return str(self.village_id) + ' - ' + str(self.name_ma) + ' ता. ' + str(self.taluka.name_ma)

    class Meta:
        ordering = ['taluka']


class BankMaster(Auditable):
    bank_id = models.BigAutoField(primary_key=True)
    name_en = models.CharField("Name in English", max_length=200,  unique=True)
    name_ma = models.CharField("Name (Ma)", max_length=200, unique=True)

    def __str__(self):
        return str(self.bank_id) + ' - ' + self.name_ma

    class Meta:
        ordering = ['bank_id']


class BranchMaster(Auditable):
    branch_id = models.BigAutoField(primary_key=True)
    name_en = models.CharField("Name in English", max_length=200, unique=True)
    name_ma = models.CharField("Name in Marathi", max_length=200, unique=True)
    phone_no = models.CharField("Phone Number", max_length=20, blank=True)
    address_en = models.CharField("Address (En)", max_length=2000, blank=True)
    address_ma = models.CharField("Address (Ma)", max_length=2000, blank=True)
    bank = models.ForeignKey(BankMaster, on_delete=models.DO_NOTHING, verbose_name='Bank Name')
    village = models.ForeignKey(VillageMaster, on_delete=models.DO_NOTHING, verbose_name='Village Name')

    def __str__(self):
        return str(self.branch_id) + ' - ' + self.name_ma

    class Meta:
        ordering = ['branch_id']


class FactoryMaster(Auditable):
    factory_id = models.BigAutoField(primary_key=True)
    desc_en = models.CharField("Description in English", max_length=155, unique=True)
    desc_ma = models.CharField("Description in Marathi", max_length=255, unique=True)
    address_en = models.CharField("Address (En)", max_length=2000, blank=True)
    address_ma = models.CharField("Address (Ma)", max_length=2000, blank=True)
    short_desc_en = models.CharField("Short description in English", max_length=50,blank=True)
    short_desc_ma = models.CharField("Short description in Marathi", max_length=200,blank=True)

    def __str__(self):
        return str(self.factory_id) + ' - ' + self.desc_ma

    class Meta:
        ordering = ['factory_id']


class SetupMaster(Auditable):
    setup_id = models.BigAutoField(primary_key=True)
    code_level = models.CharField("Code Level", max_length=5)
    code_no = models.IntegerField('Code Number')
    description = models.CharField("Description", max_length=200)
    value = models.CharField("Value", max_length=200)
    data_type = models.CharField("Data Type", max_length=1)
    applicable_ind = models.CharField("Applicable Index", max_length=1)
    from_date = models.DateField(verbose_name="From Date")
    to_date = models.DateField(verbose_name="To Date")
    lov_query = models.CharField(max_length=2000, blank=True)

    def __unicode__(self):
        return str(self.setup_id)

    class Meta:
        ordering = ['setup_id']


# class SmsInOut(Auditable):
#     sms_id = models.BigAutoField(primary_key=True)
#     mobileno = models.IntegerField()
#     text = models.CharField(max_length=500)
#     smsdate = models.DateField()
#     status = models.CharField(max_length=1)
#     type = models.CharField(max_length=50)
#     responce = models.CharField(max_length=2000, blank=True, null=True)
#     template_id = models.IntegerField()

#     def __str__(self):
#         return str(self.sms_id) + ' - ' + self.mobileno

#     class Meta:
#         managed = True
#         db_table = 'COM_SMS_IN_OUT'


class MemTypeMaster(Auditable):
    mem_type_id = models.IntegerField(primary_key=True)
    desc_en = models.CharField('Description (En)', max_length=200, unique=True)
    desc_ma = models.CharField('Description (Ma)', max_length=200, unique=True)

    class Meta:
        ordering = ['mem_type_id']

    def __str__(self):
        return str(self.mem_type_id) + ' - ' + self.desc_ma


class ReligionMaster(Auditable):
    religion_id = models.BigAutoField(primary_key=True)
    religion_ma = models.CharField(max_length=30)
    religion_en = models.CharField(max_length=30)

    def __str__(self):
        return self.religion_ma


class OrganizationMaster(models.Model):
    organisation_id = models.BigAutoField(primary_key=True)
    organisation_name_ma = models.CharField(max_length=255, unique=True)
    organisation_name_en = models.CharField(max_length=255, unique=True)
    organisation_address = models.CharField(max_length=255)

    def __str__(self):
        return self.organisation_name_ma


class CasteMaster(Auditable):
    caste_id = models.BigAutoField(primary_key=True)
    religion = models.ForeignKey(ReligionMaster, on_delete=models.DO_NOTHING)
    caste_ma = models.CharField(max_length=30, unique=True)
    caste_en = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.caste_ma


class EducationMaster(Auditable):
    education_id = models.BigAutoField(primary_key=True)
    education_ma = models.CharField(max_length=255)
    education_en = models.CharField(max_length=255)

    def __str__(self):
        return self.education_ma


class RelationShipsMaster(Auditable):
    relation_id = models.BigAutoField(primary_key=True)
    relation_ma = models.CharField(max_length=255)
    relation_en = models.CharField(max_length=255)
    seq_no = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.relation_ma)


class PersonMaster(Auditable):
    GENDER = (('M', 'Male'), ('F', 'Female'))
    person_id = models.BigAutoField(primary_key=True)
    aadhaar_number = models.CharField(max_length=20, blank=True, unique=True)
    fname_en = models.CharField(max_length=255)
    mname_en = models.CharField(max_length=255)
    lname_en = models.CharField(max_length=255)
    alias_en = models.CharField(max_length=255, blank=True)
    fname_ma = models.CharField(max_length=255)
    mname_ma = models.CharField(max_length=255)
    lname_ma = models.CharField(max_length=255)
    alias_ma = models.CharField(max_length=255, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER)
    birth_date = models.DateField(blank=True, null=True)
    mobile_no = models.CharField("Mobile No.", max_length=12, blank=True)
    phone_no = models.CharField(max_length=20, blank=True)
    fax = models.CharField("Fax", max_length=15, blank=True)
    email_id = models.CharField(max_length=255, blank=True)
    village = models.ForeignKey(VillageMaster, on_delete=models.DO_NOTHING)
    pan_no = models.CharField(max_length=30, blank=True)
    passport_no = models.CharField(max_length=100, blank=True)
    status = models.CharField("Status", max_length=1, default='A')
    blood_group = models.CharField(max_length=50, blank=True)
    # Persons with offitials in Employee
    is_lock = models.BooleanField(default=False)
    caste = models.ForeignKey(CasteMaster, on_delete=models.DO_NOTHING, blank=True, null=True)
    education = models.ForeignKey(EducationMaster, on_delete=models.DO_NOTHING, blank=True, null=True)

    # TODO
    class Meta:
        unique_together = (('village', 'fname_en', 'mname_en', 'lname_en', 'alias_en'),
                           ('village', 'fname_ma', 'mname_ma', 'lname_ma', 'alias_ma'),)

    def __str__(self):
        return str(self.fname_en) + ' ' + str(self.mname_en) + ' ' + str(self.lname_en) + ' - ' + str(self.village) + ' - ' + str(self.mobile_no)

    @property
    def any_work_done(self):

        result = Any.objects.filter(
            person__person_id=self.person_id).exists()

        if result:
            return True
        else:
            return False

    def get_name_ma(self):
        "Returns Person's full name in Marathi"
        return '%s %s %s' % (self.fname_ma, self.mname_ma, self.lname_ma)

    name_ma = property(get_name_ma)

    def get_name_en(self):
        "Returns Person's full name in English"
        return '%s %s %s %s' % (self.fname_en, self.mname_en, self.lname_en, self.alias_en)

    name_en = property(get_name_en)
