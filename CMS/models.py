"""CMS App's Model file."""
from django.contrib.auth.models import User
from django.db import models
from COM.models import Auditable
from django.conf import settings

class CaneClassMaster(Auditable):
    """Store Cane Class Master."""
    cane_class_id = models.IntegerField(primary_key=True)
    sequence = models.IntegerField()
    desc_en = models.CharField("Name (En)", max_length=200, unique=True)
    desc_ma = models.CharField("Name (Ma)", max_length=200, unique=True)

    class Meta:
        ordering = ['cane_class_id']

    def __str__(self):
        return str(self.cane_class_id) + ' - ' + self.desc_ma

class CaneQualityMaster(Auditable):
    """Cane Quality Master."""
    cquality_id = models.IntegerField(primary_key=True)
    desc_en = models.CharField("Description (En)", max_length=200, unique=True)
    desc_ma = models.CharField("Description (Ma)", max_length=200, unique=True)

    class Meta:
        ordering = ['cquality_id']

    def __str__(self):
        return str(self.cquality_id) + ' - ' + self.desc_ma

class PlantTypeMaster(Auditable):
    plant_type_id = models.IntegerField(primary_key=True, db_index=True)
    desc_en = models.CharField('Description (En)', max_length=200, unique=True)
    desc_ma = models.CharField('Description (Ma)', max_length=200, unique=True)

    class Meta:
        ordering = ['plant_type_id']

    def __str__(self):
        return str(self.plant_type_id) + ' - ' + self.desc_ma

class RegTypeMaster(Auditable):
    reg_type_id = models.IntegerField(primary_key=True)
    desc_en = models.CharField('Description (En)', max_length=200, unique=True)
    desc_ma = models.CharField('Description (Ma)', max_length=200, unique=True)

    class Meta:
        ordering = ['reg_type_id']

    def __str__(self):
        return str(self.reg_type_id) + ' - ' + self.desc_ma

class LaganTypeMaster(Auditable):
    lagan_type_id = models.IntegerField(primary_key=True)
    desc_en = models.CharField("Description in English", max_length=200, unique=True)
    desc_ma = models.CharField("Description in Marathi", max_length=200, unique=True)

    class Meta:
        ordering = ['lagan_type_id']

    def __str__(self):
        return str(self.lagan_type_id) + ' - ' + self.desc_ma

class GatTypeMaster(Auditable):
    gat_type_id = models.IntegerField(primary_key=True)
    desc_en = models.CharField("Description in English", max_length=200, unique=True)
    desc_ma = models.CharField("Description in Marathi", max_length=200, unique=True)

    class Meta:
        ordering = ['gat_type_id']

    def __str__(self):
        return str(self.gat_type_id) + ' - ' + self.desc_ma


class GatMaster(Auditable):
    gat_id = models.IntegerField(primary_key=True)
    name_en = models.CharField("Name in English", max_length=200, unique=True,)
    name_ma = models.CharField("Name in Marathi", max_length=200, unique=True)
    gat_type_id = models.ForeignKey(GatTypeMaster, on_delete=models.DO_NOTHING, verbose_name='Gat Type Name')
    
    class Meta:
        ordering = ['gat_id']

    def __str__(self):
        return str(self.gat_id) + ' - ' + self.name_ma

class VillageGats(Auditable):
    vlggat_id = models.IntegerField(primary_key=True)
    from_date = models.DateField(verbose_name="From Date")
    to_date = models.DateField(verbose_name="From Date")
    gat = models.ForeignKey(GatMaster, on_delete=models.DO_NOTHING, verbose_name='Gat Name')
    Village = models.ForeignKey('COM.VillageMaster', on_delete=models.DO_NOTHING, verbose_name='Village Name')
    
    class Meta:
        ordering = ['vlggat_id']

    def __str__(self):
        return str(self.vlggat_id) + ' - ' + self.Village

class HangamMaster(Auditable):
    hangam_id = models.IntegerField(primary_key=True)
    desc_en = models.CharField("Description in English", max_length=200, unique=True)
    desc_ma = models.CharField("Description in Marathi", max_length=200, unique=True)
    approx_yeild_gunthe = models.IntegerField()
    from_date = models.DateField(verbose_name="From Date")
    to_date = models.DateField(verbose_name="To Date")
    lagan_type = models.ForeignKey(LaganTypeMaster, on_delete=models.DO_NOTHING, verbose_name='Lagan Type')

    class Meta:
        ordering = ['hangam_id']

    def __str__(self):
        return str(self.hangam_id) + ' - ' + self.desc_ma


class SubVillageMaster(Auditable):
    """ subvilages are shivars """
    subvlg_id = models.IntegerField(primary_key=True)
    name_en = models.CharField("Name in English", max_length=200, unique=True,)
    name_ma = models.CharField("Name in Marathi", max_length=200, unique=True)
    village = models.ForeignKey('COM.VillageMaster', on_delete=models.DO_NOTHING, verbose_name='Village Name')

    class Meta:
        ordering = ['subvlg_id']

    def __str__(self):
        return str(self.subvlg_id) + ' - ' + self.name_ma + ' - ' + str(self.village.name_ma)

class SubVillageRoutes(Auditable):
    """ subvilage Routes """
    route_id = models.IntegerField(primary_key=True)
    name_en = models.CharField("Name in English", max_length=200, unique=True,)
    name_ma = models.CharField("Name in Marathi", max_length=200, unique=True)
    distance = models.IntegerField("Distance in KM")
    subvlg = models.ForeignKey(SubVillageMaster, on_delete=models.DO_NOTHING, verbose_name='Sub Village Name')

    class Meta:
        ordering = ['route_id']

    def __str__(self):
        return str(self.route_id) + ' - ' + self.name_ma + ' - ' + str(self.subvlg.name_ma)
 
class SpPermissionMaster(Auditable):
    permission_id = models.IntegerField(primary_key=True)
    desc_en = models.CharField("Description in English", max_length=200, unique=True)
    desc_ma = models.CharField("Description in Marathi", max_length=200, unique=True)

    class Meta:
        ordering = ['permission_id']

    def __str__(self):
        return self.desc_ma


class WaterSupplyMaster(Auditable):
    water_supp_id = models.IntegerField(primary_key=True)
    desc_en = models.CharField("Description in English", max_length=200, unique=True)
    desc_ma = models.CharField("Description in Marathi", max_length=200, unique=True)
    class Meta:
        ordering = ['water_supp_id']

    def __str__(self):
        return str(self.water_supp_id) + ' - ' + self.desc_ma

class WaterSchemeMaster(Auditable):
    wscheme_id = models.IntegerField(primary_key=True)
    name_ma = models.CharField(max_length=120)
    name_en = models.CharField(max_length=120)
    note = models.CharField(max_length=1000)
    sanstha_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name_ma

class SeasonYearMaster(Auditable):
    season_yr_id = models.IntegerField(primary_key=True)
    start_date = models.DateField(verbose_name='Start Date')
    end_date = models.DateField(verbose_name='End Date')
    desc_en = models.CharField('Description in English', max_length=200, unique=True)
    desc_ma = models.CharField('Description in Marathi', max_length=200, unique=True)
    status = models.CharField('Status', max_length=1, blank=True)
    current_season = models.CharField('Current Season', max_length=1, blank=True)
    reg_start_date = models.DateField(verbose_name='Reg. Start Date')
    reg_end_date = models.DateField(verbose_name="Reg. End Date")
    crushing_start_date  = models.DateField(verbose_name='Crusing Start Date')
    crushing_end_date = models.DateField(verbose_name='Crusing End Date')
    
    class Meta:
        ordering = ['season_yr_id']

    def __str__(self):
        return str(self.season_yr_id) + ' - ' + self.desc_ma

class OtherUse(models.Model):
    other_use_id = models.IntegerField(primary_key=True)
    name_en = models.CharField(max_length=155, unique=True)
    name_ma = models.CharField(max_length=155, unique=True)

    def __str__(self):
        return self.name_ma



class CaneRegistration(Auditable):
    """Cane Registration Master."""
    STATUS = (("A", "Approved"), ("P", "Pending"),)
    PHOTO_REMARK = (("1", "फोटो अपलोड नाही"), ("2", "फोटो चुकीचा आहे"),("3", "लागण फॉर्म फोटो"), ("4", "फोटो बरोबर आहे"),)
    LAT_LONG_REMARK = (("1", "लॅट-लॉन्ग बरोबर आहे"), ("2", "लॅट-लॉन्ग चुकीचे आहे"),("3", "चारी बाजू फिरलेल्या नाहीत"), ("4", "चुकीच्या ठिकाणी नोंद घेतलेली आहे"),)
    ANUDAN_IND = (("Y","Yes"),("N","No"),)
    HAMIPATRA = (("Y","Yes"),("N","No"),)

    reg_id = models.AutoField(primary_key=True)
    reg_no = models.IntegerField(blank=True, null=True)
    reg_date = models.DateField('Registration Date')
    form_number = models.CharField('Form Number' , max_length=30, blank=True)
    form_fill_date = models.DateField(verbose_name="Form Fill Date", null=True, blank=True)
    mobile_number = models.CharField(max_length=13, blank=True)
    lagan_type = models.ForeignKey(LaganTypeMaster, on_delete=models.DO_NOTHING, verbose_name="Lagan Type", blank=True, null=True)
    survey_no = models.CharField("Survey No", max_length=30, blank=True)
    total_area = models.DecimalField('Total Area', max_digits=8, decimal_places=2, null=True, blank=True)
    cane_area = models.DecimalField('Cane Area', max_digits=8, decimal_places=2, null=True, blank=True)
    on_street_ind = models.BooleanField('On Street', default=False)
    extra_area_form_no = models.CharField('Extra Area Form No', max_length=15, blank=True)
    plantation_date = models.DateField('Plantation Date')
    # TODO calculate maturity date in models according to crop
    maturity_date = models.DateField('Maturity Date', null=True, blank=True)
    approx_maturity_date = models.DateField(verbose_name='Approximate Maturity Date', null=True, blank=True)
    sample_prg_no = models.IntegerField('Sample PRG Number', null=True, blank=True)
    harvest_prg_no = models.IntegerField('Harvest PRG Number', null=True, blank=True)
    forcasted_tonnage = models.DecimalField('Forcast Tonnage', max_digits=10, decimal_places=3, null=True, blank=True)
    anudan_ind = models.CharField("Anudan Ind", max_length=1,choices=ANUDAN_IND,default="N")
    recovery = models.DecimalField('Recovery', max_digits=8, decimal_places=3, null=True, blank=True)
    status = models.CharField("Status", max_length=1, choices=STATUS, default="P")
    reg_type = models.ForeignKey(RegTypeMaster, on_delete=models.DO_NOTHING, verbose_name='Registration Type')
    hangam = models.ForeignKey(HangamMaster, on_delete=models.DO_NOTHING, verbose_name='Hangam Name')
    water_supp = models.ForeignKey(WaterSupplyMaster, on_delete=models.DO_NOTHING, verbose_name='Water Supply')
    wscheme = models.ForeignKey(WaterSchemeMaster, on_delete=models.DO_NOTHING, verbose_name='Water Supply Scheme')   
    cane_class = models.ForeignKey(CaneClassMaster, on_delete=models.DO_NOTHING, verbose_name='Cane Class Name')
    season_yr = models.ForeignKey(SeasonYearMaster, on_delete=models.DO_NOTHING, verbose_name='Season Year')
    sub_village = models.ForeignKey(SubVillageMaster, on_delete=models.DO_NOTHING, verbose_name='Sub Village Name')
    fact = models.ForeignKey('COM.FactoryMaster', on_delete=models.DO_NOTHING, verbose_name='Factory Name')
    permission = models.ForeignKey(SpPermissionMaster, on_delete=models.DO_NOTHING, verbose_name='Permission', blank=True, null=True)
    oth_use_no = models.IntegerField('OTH User Number', null=True, blank=True)
    plant_type = models.ForeignKey(PlantTypeMaster, on_delete=models.DO_NOTHING, verbose_name='Plant Type')
    gat = models.ForeignKey(GatMaster, on_delete=models.DO_NOTHING, verbose_name='Gat Name')
    hamipatra = models.CharField("Hamipatra",max_length=1,choices=HAMIPATRA,default ="N")
    hamipatra_no = models.IntegerField('Hamipatra No', null=True, blank=True)
    file_no = models.IntegerField('File Number', null=True, blank=True)
    farmer_id = models.IntegerField(blank=True, null=True)
    farm_photo = models.ImageField(upload_to="farm_photos/", blank=True, null=True)
    photo_lat = models.DecimalField(max_digits=18, decimal_places=14, blank=True, null=True) # To store latitude from where photo is clicked
    photo_long = models.DecimalField(max_digits=18, decimal_places=14, blank=True, null=True) # To store longitude from where photo is clicked
    emp_id = models.IntegerField(blank=True, null=True)
    photo_remark = models.CharField("PHOTO_REMARK", max_length=100, choices=PHOTO_REMARK, blank=True)
    lat_long_remark = models.CharField("LAT_LONG_REMARK", max_length=100, choices=LAT_LONG_REMARK, blank=True)
    approved_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING,related_name="%(app_label)s_%(class)s_approved_by", null=True, blank=True)
    
    class Meta:
        #ordering = [ 'reg_id', 'gat', 'sub_village', 'kacchi_tarikh', 'hangam', 'farmer__farmer_code']
        unique_together = (('sub_village', 'farmer_id', 'plantation_date', 'survey_no', 'season_yr'),)
 
    # LOGIC for creating reg_no - LAGAN_ID + CREATED_BY + SEASON_YR + (COUNT + 1) WITH SAME SEASON_YR
    def save(self, * args, ** kwargs):

        if not self.reg_no:
            LAGAN_ID = str(self.lagan_type.lagan_type_id)
            CREATED_BY = str(self.created_by_id).zfill(3)
            SEASON_YR = str(self.season_yr.season_yr_id)
            TOP = CaneRegistration.objects.filter(season_yr=self.season_yr).count()
            TOP = TOP + 1
            TOP = str(TOP).zfill(5)
            self.reg_no = LAGAN_ID + CREATED_BY + SEASON_YR + TOP
        super(CaneRegistration, self).save(* args, ** kwargs)

    def __str__(self):
        return str(self.reg_id) +  ' - ' + str(self.season_yr.desc_ma) + ' - ' + self.farmer.fname_ma + ' ' \
         + self.farmer.mname_ma + ' ' + self.farmer.lname_ma + ' - ' \
         + str(self.survey_no) + ' - ' + str(self.cane_area) 

    @property
    def is_photo_uploaded(self):

        result = CaneRegistrationPhotos.objects.filter(reg_id=self.reg_id).exclude(farm_photo_base64__isnull=True).exclude(farm_photo_base64="").exists()

        if result:
            return True
        else:
            return False

    def get_coordinates(self):
        
        return CaneRegistrationCoOrdinate.objects.filter(reg_id=self.reg_id)


class CaneRegistrationPhotos(Auditable):
    reg_id = models.ForeignKey(CaneRegistration, related_name="canephotos",on_delete=models.DO_NOTHING, verbose_name="Cane Registration Photos")
    farm_photo_base64 = models.ImageField(upload_to='canephotos/')


class CaneRegistrationCoOrdinate(Auditable):
    reg_id = models.ForeignKey(CaneRegistration, related_name='coords',on_delete=models.DO_NOTHING, verbose_name="CanRegistratio Id")
    seq_id = models.IntegerField()
    longitude = models.DecimalField(max_digits=18, decimal_places=14)
    latitude = models.DecimalField(max_digits=18, decimal_places=14)

    class Meta:
        unique_together = (('reg_id', 'seq_id'),)
        ordering = ['-reg_id']

    def __str__(self):
        return '%s: %s' % (self.reg_id.reg_no, self.seq_id)


class HamipatraMaster(Auditable):
    STATUS = (('A', 'Approved'), ('P', 'Pending'))
    hamipatra_id = models.AutoField(primary_key=True)
    farmer_id = models.IntegerField(blank=True, null=True)
    bank_name = models.CharField(max_length=255)
    branch_name = models.CharField(max_length=255)
    taluka = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    total_area = models.DecimalField('Cane Area', max_digits=8, decimal_places=2)
    #hami_type = models.CharField(max_length=20, blank=True)
    issued_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="%(app_label)s_%(class)s_issued_by",on_delete=models.DO_NOTHING,  null=True, blank=True)
    #issued_status = models.CharField(max_length=1, choices=STATUS, default='A')
    approved_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="%(app_label)s_%(class)s_approved_by", on_delete=models.DO_NOTHING,null=True, blank=True)
    approved_status = models.CharField(max_length=1, choices=STATUS, default='P')
    is_printed = models.BooleanField(default=False)
    printed_date =  models.DateField(blank=True, null=True)
    printed_by = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="%(app_label)s_%(class)s_printed_by",on_delete=models.DO_NOTHING,  null=True, blank=True)

    class Meta:
        #ordering = [ 'reg_id', 'gat', 'sub_village', 'kacchi_tarikh', 'hangam', 'farmer__farmer_code']
        
        permissions = ( 
                        ("issue_hamipatra", "can issue Hamipatra"),
                        ("approve_hamipatra", "can approve Hamipatra"),
                        ("view_hamipatra", "can view hamipatra"),
        )


class HamipatraDetails(models.Model):
    hamipatra = models.ForeignKey(HamipatraMaster,on_delete=models.DO_NOTHING)
    reg_id = models.ForeignKey(CaneRegistration,on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=1)
    survey_no = models.CharField("Survey No", max_length=30, blank=True)
    plantation_date = models.DateField('Plantation Date')
    cane_area = models.DecimalField('Cane Area', max_digits=8, decimal_places=2, null=True, blank=True)
    forcasted_tonnage = models.DecimalField('Forcast Tonnage', max_digits=10, decimal_places=3, null=True, blank=True)
    note = models.CharField(max_length=1000,blank=True)


class CaneCertificate(Auditable):
    STATUS = (('A', 'Approved'), ('P', 'Pending'))

    certificate_id = models.AutoField(primary_key=True)
    certificate_no = models.CharField(max_length=30, blank=True)
    farmer_id = models.IntegerField(blank=True, null=True)
    #issued_status = models.CharField(max_length=1, choices=STATUS)
    #approved_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="%(app_label)s_%(class)s_approved_by", null=True, blank=True)
    #approved_status = models.CharField(max_length=1, choices=STATUS, default='P')
    #ded_acc =  models.ForeignKey("cac.DedAccountMaster")
    society_name = models.CharField(max_length=255)
    society_village = models.CharField(max_length=255)
    total_area = models.DecimalField('Cane Area', max_digits=8, decimal_places=2, null=True, blank=True)
    issued_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="%(app_label)s_%(class)s_issued_by",on_delete=models.DO_NOTHING, null=True, blank=True)

    class Meta:
        ordering = ['certificate_id']
        
class CaneCertificateDetails(Auditable):
    certificate = models.ForeignKey(CaneCertificate,on_delete=models.DO_NOTHING)
    reg_id = models.ForeignKey(CaneRegistration,on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=1)
    survey_no = models.CharField("Survey No", max_length=30, blank=True)
    plantation_date = models.DateField('Plantation Date')
    cane_area = models.DecimalField('Cane Area', max_digits=8, decimal_places=2, null=True, blank=True)
    #village = models.CharField(max_length=255)
    note = models.CharField(max_length=1000)
    
     
class CaneSampling(Auditable):
    sample_id = models.IntegerField(primary_key=True)
    season_yr = models.ForeignKey(SeasonYearMaster, on_delete=models.DO_NOTHING, verbose_name='Season Year')
    reg = models.ForeignKey(CaneRegistration, on_delete=models.DO_NOTHING, verbose_name='Cane Registration No')
    sample_no = models.IntegerField('Sample No')
    recovery = models.DecimalField('Recovery', max_digits=14, decimal_places=3, null=True, blank=True)
    sample_date = models.DateField(verbose_name="Sample Date")
    bricks = models.DecimalField(verbose_name="Bricks", max_digits=14, decimal_places=3, null=True, blank=True)
    latitude = models.DecimalField(max_digits=12, decimal_places=8, blank=True, null=True)
    longitude = models.DecimalField(max_digits=12, decimal_places=8, blank=True, null=True)
    photo = models.ImageField(upload_to="canesample_photos/", blank=True, null=True)

    class Meta:
        ordering = ['-sample_id']

    def __unicode__(self):
        return str(self.sample_id)


class TransporterTypeMaster(Auditable):
    """Cane Transport Type Master."""
    tran_type_id = models.IntegerField(primary_key=True)
    desc_en = models.CharField("Description in English", max_length=200, unique=True)
    desc_ma = models.CharField("Description in Marathi", max_length=200, unique=True)
    max_tonnage = models.DecimalField('Maximum Tonnage', max_digits=10, decimal_places=3, null=True, blank=True)
    vehical_type_ind = models.BooleanField('Vehical Type', default=False)
    binding_wt = models.DecimalField('Binding weight', max_digits=10, decimal_places=3, null=True, blank=True)
    adj_wt = models.DecimalField('Adjuting weight', max_digits=10, decimal_places=3, null=True, blank=True)

    class Meta:
        ordering = ['tran_type_id']
    

class TransporterMaster(Auditable):
    """ Transporter Master """
    transporter_id = models.IntegerField(primary_key=True)
    transporter_code = models.CharField(unique=True,max_length=10)
    status = models.CharField(max_length=1)
    self_tran_ind = models.CharField(max_length=1)
    photo = models.ImageField(upload_to='transporter', blank=True)
    mobile_no = models.CharField(max_length=10)
    person_id = models.IntegerField("SubLedger")
    main_cont_ind = models.CharField(max_length=1)
    main_cont_id = models.IntegerField()


    class Meta:
        ordering = ['transporter_id']

    def __str__(self):
      return  str(self.tran_id) 

class TranVehicleMaster(Auditable):
    AGREEMENT_IND = (('Y', 'Yes'), ('N', 'No'))
    """ Transporter Vehicle Master """
    vehicle_id = models.IntegerField(primary_key=True)
    vehicle_no = models.CharField(unique=True,max_length=20)
    agreement_ind = models.CharField(max_length=1,choices=AGREEMENT_IND,default='Y')
    agreement_no = models.IntegerField()
    season_yr = models.ForeignKey(SeasonYearMaster,verbose_name='Season Year',on_delete=models.DO_NOTHING,blank=False,null=False)   
    transporter = models.ForeignKey(TransporterMaster,verbose_name='Transporter',on_delete=models.DO_NOTHING,blank=False,null=False)
    tran_type = models.ForeignKey(TransporterTypeMaster, verbose_name="Transporter Type",on_delete=models.DO_NOTHING,blank=False,null=False)
    tyre_no = models.CharField(max_length=10)
    status = models.CharField(max_length=1)
    smartcard = models.CharField(verbose_name='Smart Card No',unique=True,max_length=10)
    rfid = models.CharField(verbose_name='Smart Card No',unique=True,max_length=10) 
    barcode = models.CharField(verbose_name='Smart Card No',unique=True,max_length=10) 
    trollytag1 = models.CharField(verbose_name='Smart Card No',unique=True,max_length=10)
    trollytag2 = models.CharField(verbose_name='Smart Card No',unique=True,max_length=10)
    GPStracking = models.BooleanField(max_length=1,default='Y')
    GPSIMEI_No = models.CharField(verbose_name='IMEI',unique=True,max_length=30)
    driver_name=models.CharField(verbose_name='Driver Name',max_length=200)
    driver_mobile=models.CharField(verbose_name='Driver Mobile',max_length=10)
 

    class Meta:
        ordering = ['vehicle_id']

    def __str__(self):
      return  str(self.vehicle_id) 

class HarvesterMaster(models.Model):
    harvester_id = models.IntegerField(primary_key=True)
    harvester_code = models.CharField(unique=True,max_length=10)
    harv_type_id = models.IntegerField()
    status = models.CharField("Status", max_length=1, blank=True)
    self_harv_ind = models.BooleanField('Self Harvester Ind', default=False)
    photo = models.ImageField(upload_to='transporter', blank=True)
    no_of_harvesters = models.IntegerField()
    mobile_no = models.CharField(max_length=13)
    person_id = models.IntegerField("SubLedger")
    main_cont_id = models.IntegerField()   

 
    def __str__(self):
      return str(self.harvester_id) + ' - ' + self.harvester_code
        
    class Meta:
        ordering = ['harvester_id']


class WeightSlips(Auditable):
    UPDOWN = ((1, "वरचा"), (2, "खालचा"), (3, "संपूर्ण"))

    token_id = models.BigIntegerField(primary_key=True)
    vtrip_id = models.BigIntegerField(blank=False,null=False)
    token_no = models.IntegerField(blank=False,null=False)
    season_yr = models.ForeignKey(SeasonYearMaster, on_delete=models.DO_NOTHING, verbose_name='Season Year')
    status = models.CharField(max_length=1, blank=True, null=True)
    wait_no = models.IntegerField(blank=True, null=True)
    wait_shift_date = models.DateField(blank=True,null=True)
    wait_shift_id = models.IntegerField(blank=True, null=True)
    in_time = models.DateTimeField(blank=True, null=True)
    out_time = models.DateTimeField(blank=True, null=True)
    rfid = models.CharField(max_length=50, blank=True, null=True)
    smartcard = models.CharField(max_length=8, blank=True, null=True)
    tag1 = models.CharField(max_length=8, blank=True, null=True)
    tag2 = models.CharField(max_length=8, blank=True, null=True)
    fieldslip_no = models.CharField(max_length=10) #
    weight_bridge_no = models.IntegerField(blank=True, null=True) #
    mill_no = models.IntegerField(blank=True, null=True)
    tran_binding_material_ind = models.CharField(max_length=1,blank=True, null=True)   
    loaded_weight = models.DecimalField(max_digits=14, decimal_places=3, blank=True, null=True)
    empty_weight = models.DecimalField(max_digits=14, decimal_places=3, blank=True, null=True)
    gross_weight = models.DecimalField(max_digits=14, decimal_places=3, blank=True, null=True)
    bind_weight = models.DecimalField(max_digits=14, decimal_places=3, blank=True, null=True)
    net_weight = models.DecimalField(max_digits=14, decimal_places=3, blank=True, null=True)
    updown_1 = models.IntegerField(choices=UPDOWN) # updown1
    updown_2 = models.IntegerField(choices=UPDOWN) # upddown 2
    through_pass_ind = models.CharField(max_length=255, blank=True, null=True)
    cane_loaded_date = models.DateTimeField(blank=True, null=True) #
    loaded_vehicle_weight_date = models.DateTimeField(blank=True, null=True)
    loaded_wt_shift = models.IntegerField()
    loaded_wt_user = models.CharField(max_length=20, blank=True)
    empty_vehicle_weight_date = models.DateTimeField(blank=True, null=True)
    empty_wt_shift = models.IntegerField()
    empty_wt_user = models.CharField(max_length=20, blank=True)
    weight_slip_date = models.DateField(blank=True, null=True) #
    canequality = models.ForeignKey(CaneQualityMaster, on_delete=models.DO_NOTHING, blank=True, null=True) #
    reg = models.ForeignKey(CaneRegistration, on_delete=models.DO_NOTHING) #
    vehicle = models.ForeignKey(TranVehicleMaster,on_delete=models.DO_NOTHING)
    tran = models.ForeignKey(TransporterMaster,on_delete=models.DO_NOTHING)
    harv  = models.ForeignKey(HarvesterMaster, on_delete=models.DO_NOTHING)
    agent_id = models.IntegerField(blank=True, null=True)
    fieldslip_user=models.CharField(max_length=20, blank=True)
    numbertaker_user=models.CharField(max_length=20, blank=True)
    fact = models.ForeignKey('COM.FactoryMaster', on_delete=models.DO_NOTHING,blank=True, null=True)
    sms_send = models.CharField(max_length=1,blank=True, null=True)
    shiftsr_no = models.IntegerField(blank=True, null=True)
    entry_type = models.CharField(max_length=1, blank=True, null=True)
    last_trip = models.BooleanField(default=False)
    distance=models.CharField(max_length=20, blank=True)
    diesel = models.IntegerField(null=True, blank=True)
    oil = models.IntegerField(null=True, blank=True)
    fpayment_no  = models.IntegerField(blank=True, null=True)
    tpayment_no  = models.IntegerField(blank=True, null=True)
    hpayment_no  = models.IntegerField(blank=True, null=True)
   

    def __str__(self):    
        return 'Field Slip Number - ' + str(self.fieldslip_no)

    class Meta:
         ordering = ['vtrip_id']


class WeightSlip_Mobile(Auditable):
    vtrip_id = models.BigIntegerField(primary_key=True)
    vtrip_date = models.DateField()
    through_pass_ind = models.IntegerField()
    status = models.CharField(max_length=1,blank=True)
    emp_id = models.IntegerField(blank=True, null=True)
    samrtcard_no = models.CharField(max_length=20)
    harv_id = models.IntegerField() #models.ForeignKey('CmsHarvesterMaster', on_delete=models.DO_NOTHING)
    season_year = models.ForeignKey(SeasonYearMaster, on_delete=models.DO_NOTHING)
    tran_id = models.IntegerField() #models.ForeignKey('CmsTransporterMaster', on_delete=models.DO_NOTHING)
    latitude = models.DecimalField(max_digits=14, decimal_places=8, blank=True, null=True) # To store latitude from where photo is clicked
    longitude = models.DecimalField(max_digits=14, decimal_places=8, blank=True, null=True) # To store longitude from where photo is clicked

    class Meta:
        ordering = ['vtrip_date' , 'vtrip_id']
        permissions = ( 
                        ("view_weightslipmobile" , "can view cane weightslip mobile"),
                    )


class WeightSlip_Mobile_Details(Auditable):
    CHOICES = ((1, "वरचा"), (2, "खालचा"), (3, "संपूर्ण"))
    vtrip = models.ForeignKey(WeightSlip_Mobile, on_delete=models.DO_NOTHING)
    serial_number = models.IntegerField() #
    field_slip_no = models.CharField(max_length=25)
    updown_1 = models.IntegerField(choices=CHOICES) # 1 - varacha , 2- khalcha , 3 - sumpurna
    updown_2 = models.IntegerField(choices=CHOICES) # 1 - varacha , 2 - khalacha , 3 - sumpurna
    reg = models.ForeignKey(CaneRegistration, on_delete=models.DO_NOTHING)
    cquality = models.ForeignKey(CaneQualityMaster, on_delete=models.DO_NOTHING)
    last_trip = models.BooleanField(default=False)

    class Meta:
        ordering = ['vtrip_id']


class HarvestingProgram(models.Model):
    STATUS = (('A', 'Active'), ('S', 'Started'), ('E', 'Ended'), ('H', 'Hold'), ('O', 'OtherUse'))
    season_yr_id = models.IntegerField()
    program_no = models.IntegerField()
    program_sr_no = models.IntegerField(primary_key=True)
    reg_id = models.IntegerField()
    reg_no = models.IntegerField()
    survey_no = models.CharField(max_length=25)
    farmer_code = models.IntegerField()
    farmer_name = models.CharField(max_length=255)
    cane_area = models.DecimalField('Cane Area', max_digits=8, decimal_places=2)
    lagan_date = models.DateField()
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=25, choices=STATUS, default='A')
    status_remark = models.CharField(max_length=155, blank=True)    
    hangam_id = models.IntegerField()
    other_use_id = models.IntegerField()
    village_id = models.IntegerField()
    class Meta:
        ordering = ['program_sr_no']
        unique_together = (('season_yr_id', 'program_sr_no'),)

