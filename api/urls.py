from django.urls import path, include
from rest_framework import routers
from api.views import *


urlpatterns = [
    # COM
    path('entity_type/', EntityTypeAPI.as_view(), name='entity_type'),

    path('state/', StateMasterAPI.as_view(), name='state'),   
    # path('state_update/<int:pk>/', StateMasterAPI.as_view(), name='state_update'),
    path('district/', DistrictMasterAPI.as_view(), name='district'),
    path('taluka/', TalukaMasterAPI.as_view(), name='taluka'), 
    path('village/', VillageMasterAPI.as_view(), name='village'),

    path('bank/', BankMasterAPI.as_view(), name='bank'),
    path('branch/', BranchMasterAPI.as_view(), name='branch'),

    path('factory/', FactoryMasterAPI.as_view(), name='factory'),
    path('setup/', SetupMasterAPI.as_view(), name='setup'),
    # path('sms/', SmsInOutAPI.as_view(), name='sms'),
    path('mem_type/', MemTypeMasterAPI.as_view(), name='mem_type'),

    path('religion/', ReligionMasterAPI.as_view(), name='religion'),
    path('organization/', OrganizationMasterAPI.as_view(), name='organization'),
    path('caste/', CasteMasterAPI.as_view(), name='caste'),
    path('education/', EducationMasterAPI.as_view(), name='education'),

    path('relation_ships/', RelationShipsMasterAPI.as_view(), name='relation_ships'),
    path('person/', PersonMasterAPI.as_view(), name='person'),

    # CMS
    path('cane_class/', CaneClassMasterAPI.as_view(), name='cane_class'),
    path('cane_quality/', CaneQualityMasterAPI.as_view(), name='cane_quality'),
    path('reg_type/', RegTypeMasterAPI.as_view(), name='reg_type'),
    path('lagan_type/', LaganTypeMasterAPI.as_view(), name='lagan_type'),
    path('gat_type/', GatTypeMasterAPI.as_view(), name='gat_type'),
    path('gat/', GatMasterAPI.as_view(), name='gat'),
    path('vlg_gats/', VillageGatsAPI.as_view(), name='vlg_gats'),
    path('hangam/', HangamMasterAPI.as_view(), name='hangam'),
    path('sub_vlg/', SubVillageMasterAPI.as_view(), name='sub_vlg'),
    path('sub_vlg_routes/', SubVillageRoutesAPI.as_view(), name='sub_vlg_routes'),
    path('sp_permission/', SpPermissionMasterAPI.as_view(), name='sp_permission'),
    path('water_supply/', WaterSupplyMasterAPI.as_view(), name='water_supply'),
    path('water_scheme/', WaterSchemeMasterAPI.as_view(), name='water_scheme'),
    path('season_year/', SeasonYearMasterAPI.as_view(), name='season_year'),
    path('other_use/', OtherUseAPI.as_view(), name='other_use'),
    path('cane_registration/', CaneRegistrationAPI.as_view(), name='cane_registration'),
    path('cane_photos/', CaneRegistrationPhotosAPI.as_view(), name='cane_photos'),
    path('cane_coordinates/', CaneRegistrationCoOrdinateAPI.as_view(), name='cane_coordinates'),
    path('hami_patra/', HamipatraMasterAPI.as_view(), name='hami_patra'),
    path('hami_patra_details/', HamipatraDetailsAPI.as_view(), name='hami_patra_details'),
    path('cane_certificate/', CaneCertificateAPI.as_view(), name='cane_certificate'),
    path('cane_certificate_details/', CaneCertificateDetailsAPI.as_view(), name='cane_certificate_details'),
    path('cane_sampling/', CaneSamplingAPI.as_view(), name='cane_sampling'),
    path('trans_type/', TransporterTypeMasterAPI.as_view(), name='trans_type'),
    path('transporter/', TransporterMasterAPI.as_view(), name='transporter'),
    path('tran_vehicle/', TranVehicleMasterAPI.as_view(), name='tran_vehicle'),
    path('harvester/', HarvesterMasterAPI.as_view(), name='harvester'),
    path('weight_slips/', WeightSlipsAPI.as_view(), name='weight_slips'),
    path('weight_slip_mob/', WeightSlip_MobileAPI.as_view(), name='weight_slip_mob'),
    path('weight_slip_mob_det/', WeightSlip_Mobile_DetailsAPI.as_view(), name='weight_slip_mob_det'),
    path('harvest_prog/', HarvestingProgramAPI.as_view(), name='harvest_prog'),















]