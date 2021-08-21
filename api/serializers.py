from rest_framework import serializers
from COM.models import *
from CMS.models import *

# COM
class EntityTypeMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntityTypeMaster
        fields = '__all__'

class StateMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateMaster
        fields = '__all__'

class DistrictMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = DistrictMaster
        fields = '__all__'

class TalukaMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = TalukaMaster
        fields = '__all__'

class VillageMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = VillageMaster
        fields = '__all__'

class BankMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankMaster
        fields = '__all__'

class BranchMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchMaster
        fields = '__all__'

class FactoryMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactoryMaster
        fields = '__all__'

class SetupMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SetupMaster
        fields = '__all__'

# class SmsInOutSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SmsInOut
#         fields = '__all__'

class MemTypeMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemTypeMaster
        fields = '__all__'

class ReligionMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReligionMaster
        fields = '__all__'

class OrganizationMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationMaster
        fields = '__all__'

class CasteMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CasteMaster
        fields = '__all__'
    
class EducationMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationMaster
        fields = '__all__'

class RelationShipsMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelationShipsMaster
        fields = '__all__'

class PersonMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonMaster
        fields = '__all__'

# CMS
class CaneClassMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaneClassMaster
        fields = '__all__'

class CaneQualityMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaneQualityMaster
        fields = '__all__'

class PlantTypeMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantTypeMaster
        fields = '__all__'

class RegTypeMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegTypeMaster
        fields = '__all__'

class LaganTypeMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaganTypeMaster
        fields = '__all__'

class GatTypeMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = GatTypeMaster
        fields = '__all__'

class GatMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = GatMaster
        fields = '__all__'

class VillageGatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VillageGats
        fields = '__all__'

class HangamMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = HangamMaster
        fields = '__all__'

class SubVillageMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubVillageMaster
        fields = '__all__'

class SubVillageRoutesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubVillageRoutes
        fields = '__all__'

class SpPermissionMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpPermissionMaster
        fields = '__all__'

class WaterSupplyMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterSupplyMaster
        fields = '__all__'

class WaterSchemeMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterSchemeMaster
        fields = '__all__'

class SeasonYearMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeasonYearMaster
        fields = '__all__'

class OtherUseSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherUse
        fields = '__all__'

class CaneRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaneRegistration
        fields = '__all__'

class CaneRegistrationPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaneRegistrationPhotos
        fields = '__all__'

class CaneRegistrationCoOrdinateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaneRegistrationCoOrdinate
        fields = '__all__'

class HamipatraMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = HamipatraMaster
        fields = '__all__'

class HamipatraDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HamipatraDetails
        fields = '__all__'

class CaneCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaneCertificate
        fields = '__all__'

class CaneCertificateDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaneCertificateDetails
        fields = '__all__'

class CaneSamplingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaneSampling
        fields = '__all__'

class TransporterTypeMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransporterTypeMaster
        fields = '__all__'

class TransporterMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransporterMaster
        fields = '__all__'

class TranVehicleMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranVehicleMaster
        fields = '__all__'

class HarvesterMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = HarvesterMaster
        fields = '__all__'

class WeightSlipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeightSlips
        fields = '__all__'

class WeightSlip_MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeightSlip_Mobile
        fields = '__all__'

class WeightSlip_Mobile_DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeightSlip_Mobile_Details
        fields = '__all__'

class HarvestingProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = HarvestingProgram
        fields = '__all__'

