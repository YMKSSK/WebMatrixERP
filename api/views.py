from django.shortcuts import render
from COM.models import *
from CMS.models import *
from rest_framework.views import APIView
from django.core import serializers
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from rest_framework import generics

import random
# Create your views here.

# COM
class EntityTypeAPI(APIView):
    def get(self, request, format=None):
        entity_type = EntityTypeMaster.objects.all()
        serializer = EntityTypeMasterSerializer(entity_type, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = EntityTypeMasterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StateMasterAPI(APIView):
    def get_object(self, pk):
        try:
            return StateMaster.objects.get(state_id=pk)
        except StateMaster.DoesNotExist:
            return Response(status=404)

    def get(self, request, pk, format=None):
        state = StateMaster.objects.all()
        serializer = StateMasterSerializer(state, many=True)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        data = request.data
        serializer = StateMasterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        state_id = self.get_object(pk)
        serializer = StateMasterSerializer(state_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DistrictMasterAPI(APIView):
    def get(self, request, format=None):
        state = self.request.query_params.get('state_id', None)
        district = StateMaster.objects.all()
        serializer = DistrictMasterSerializer(district, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = DistrictMasterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TalukaMasterAPI(APIView):
    def get(self, request, format=None):
        district = self.request.query_params.get('district_id', None)
        taluka = TalukaMaster.objects.all()
        serializer = TalukaMasterSerializer(taluka, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = TalukaMasterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VillageMasterAPI(APIView):
    def get(self, request, format=None):
        taluka = self.request.query_params.get('taluka_id', None)
        village = VillageMaster.objects.all()
        serializer = VillageMasterSerializer(village, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = VillageMasterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BankMasterAPI(APIView):
    def get(self, request, format=None):
        bank = BankMaster.objects.all()
        serializer = BankMasterSerializer(bank, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = BankMasterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BranchMasterAPI(APIView):
    def get(self, request, format=None):
        bank = self.request.query_params.get('bank_id', None)
        village = self.request.query_params.get('village_id', None)
        branch = BranchMaster.objects.all()
        serializer = BranchMasterSerializer(branch, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = BranchMasterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FactoryMasterAPI(APIView):
    def get(self, request, format=None):
        factory = FactoryMaster.objects.all()
        serializer = FactoryMasterSerializer(factory, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = FactoryMasterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SetupMasterAPI(APIView):
    def get(self, request, format=None):
        setup = SetupMaster.objects.all()
        serializer = SetupMasterSerializer(setup, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = SetupMasterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class SmsInOutAPI(APIView):
#     def get(self, request, format=None):
#         sms = SmsInOut.objects.all()
#         serializer = SmsInOutSerializer(sms, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         data = request.data
#         serializer = SmsInOutSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MemTypeMasterAPI(APIView):
    def get(self, request, format=None):
        mem_type = MemTypeMaster.objects.all()
        serializer = MemTypeMasterSerializer(mem_type, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = MemTypeMasterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReligionMasterAPI(APIView):
    def get(self, request, format=None):
        religion = ReligionMaster.objects.all()
        serializer = ReligionMasterSerializer(religion, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = ReligionMasterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrganizationMasterAPI(APIView):
    def get(self, request, format=None):
        organization = OrganizationMaster.objects.all()
        serializer = OrganizationMasterSerializer(organization, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = OrganizationMasterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CasteMasterAPI(APIView):
    def get(self, request, format=None):
        caste = CasteMaster.objects.all()
        serializer = CasteMasterSerializer(caste, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = CasteMasterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EducationMasterAPI(APIView):
    def get(self, request, format=None):
        education = EducationMaster.objects.all()
        serializer = EducationMasterSerializer(education, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = EducationMasterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RelationShipsMasterAPI(APIView):
    def get(self, request, format=None):
        relation_ships = RelationShipsMaster.objects.all()
        serializer = RelationShipsMasterSerializer(relation_ships, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = RelationShipsMasterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonMasterAPI(APIView):
    def get(self, request, format=None):
        village = self.request.query_params.get('village_id', None)
        caste = self.request.query_params.get('caste_id', None)
        education = self.request.query_params.get('education_id', None)
        person = PersonMaster.objects.all()
        serializer = PersonMasterSerializer(person, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = PersonMasterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# CMS
class CaneClassMasterAPI(APIView):
    def get(self, request, format=None):
        cane_class = CaneClassMaster.objects.all()
        serializer = CaneClassMasterSerializer(cane_class, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = CaneClassMasterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CaneQualityMasterAPI(APIView):
    def get(self, request, format=None):
        cane_quality = CaneQualityMaster.objects.all()
        serializer = CaneQualityMasterSerializer(cane_quality, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = CaneQualityMasterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PlantTypeMasterAPI(APIView):
    def get(self, request, format=None):
        plant_type = PlantTypeMaster.objects.all()
        serializer = PlantTypeMasterSerializer(plant_type, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = PlantTypeMasterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegTypeMasterAPI(APIView):
    def get(self, request, format=None):
        reg_type = RegTypeMaster.objects.all()
        serializer = RegTypeMasterSerializer(reg_type, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = RegTypeMasterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LaganTypeMasterAPI(APIView):
    def get(self, request, format=None):
        lagan_type = LaganTypeMaster.objects.all()
        serializer = LaganTypeMasterSerializer(lagan_type, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = LaganTypeMasterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GatTypeMasterAPI(APIView):
    def get(self, request, format=None):
        gat_type = GatTypeMaster.objects.all()
        serializer = GatTypeMasterSerializer(gat_type, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = GatTypeMasterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GatMasterAPI(APIView):
    def get(self, request, format=None):
        gat_type = self.request.query_params.get('gat_type_id', None)
        gat = GatMaster.objects.all()
        serializer = GatMasterSerializer(gat, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = GatMasterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VillageGatsAPI(APIView):
    def get(self, request, format=None):
        gat = self.request.query_params.get('gat_id', None)
        village = self.request.query_params.get('village_id', None)
        vlg_gats = VillageGats.objects.all()
        serializer = VillageGatsSerializer(vlg_gats, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = VillageGatsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HangamMasterAPI(APIView):
    def get(self, request, format=None):
        lagan_type = self.request.query_params.get('lagan_type_id', None)
        hangam = HangamMaster.objects.all()
        serializer = HangamMasterSerializer(hangam, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = HangamMasterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubVillageMasterAPI(APIView):
    def get(self, request, format=None):
        village = self.request.query_params.get('village_id', None)
        sub_village = SubVillageMaster.objects.all()
        serializer = SubVillageMasterSerializer(sub_village, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = SubVillageMasterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubVillageRoutesAPI(APIView):
    def get(self, request, format=None):
        sub_vlg = self.request.query_params.get('subvlg_id', None)
        sub_vlg_routes = SubVillageRoutes.objects.all()
        serializer = SubVillageRoutesSerializer(sub_vlg_routes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = SubVillageRoutesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SpPermissionMasterAPI(APIView):
    def get(self, request, format=None):
        sp_permission = SpPermissionMaster.objects.all()
        serializer = SpPermissionMasterSerializer(sp_permission, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = SpPermissionMasterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WaterSupplyMasterAPI(APIView):
    def get(self, request, format=None):
        water_supply = WaterSupplyMaster.objects.all()
        serializer = WaterSupplyMasterSerializer(water_supply, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = WaterSupplyMasterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WaterSchemeMasterAPI(APIView):
    def get(self, request, format=None):
        water_scheme = WaterSchemeMaster.objects.all()
        serializer = WaterSchemeMasterSerializer(water_scheme, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = WaterSchemeMasterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SeasonYearMasterAPI(APIView):
    def get(self, request, format=None):
        season_year = SeasonYearMaster.objects.all()
        serializer = SeasonYearMasterSerializer(season_year, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = SeasonYearMasterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OtherUseAPI(APIView):
    def get(self, request, format=None):
        other_use = OtherUse.objects.all()
        serializer = OtherUseSerializer(other_use, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = OtherUseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CaneRegistrationAPI(APIView):
    def get(self, request, format=None):
        lagan_type = self.request.query_params.get('lagan_type_id', None)
        reg_type = self.request.query_params.get('reg_type_id', None)
        hangam = self.request.query_params.get('hangam_id', None)
        water_supply = self.request.query_params.get('water_supp_id', None)
        water_scheme = self.request.query_params.get('wscheme_id', None)
        cane_class = self.request.query_params.get('cane_class_id', None)
        season_yr = self.request.query_params.get('season_yr_id', None)
        factory = self.request.query_params.get('factory_id', None)
        sp_permission = self.request.query_params.get('permission_id', None)
        plant_type = self.request.query_params.get('plant_type_id', None)
        gat = self.request.query_params.get('gat_id', None)
        approved_by = self.request.query_params.get()
        cane_reg = CaneRegistration.objects.all()
        serializer = CaneRegistrationSerializer(cane_reg, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = CaneRegistrationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CaneRegistrationPhotosAPI(APIView):
    def get(self, request, format=None):
        cane_photos = CaneRegistrationPhotos.objects.all()
        serializer = CaneRegistrationPhotosSerializer(cane_photos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = CaneRegistrationPhotosSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CaneRegistrationCoOrdinateAPI(APIView):
    def get(self, request, format=None):
        cane_reg = self.request.query_params.get('reg_id', None)
        cane_coordinates = CaneRegistrationCoOrdinate.objects.all()
        serializer = CaneRegistrationCoOrdinateSerializer(cane_coordinates, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = CaneRegistrationCoOrdinateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HamipatraMasterAPI(APIView):
    def get(self, request, format=None):
        issued_by = self.request.query_params.get()
        approved_by = self.request.query_params.get()
        printed_by = self.request.query_params.get()
        hami_patra = HamipatraMaster.objects.all()
        serializer = HamipatraMasterSerializer(hami_patra, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = HamipatraMasterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HamipatraDetailsAPI(APIView):
    def get(self, request, format=None):
        hami_patra = self.request.query_params.get('hamipatra_id', None)
        cane_reg = self.request.query_params.get('reg_id', None)
        hami_patra_details = HamipatraDetails.objects.all()
        serializer = HamipatraDetailsSerializer(hami_patra_details, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = HamipatraDetailsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CaneCertificateAPI(APIView):
    def get(self, request, format=None):
        approved_by = self.request.query_params.get()
        # ded_acc = self.request.query_params.get()
        issued_by = self.request.query_params.get()
        cane_certificate = CaneCertificate.objects.all()
        serializer = CaneCertificateSerializer(cane_certificate, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = CaneCertificateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CaneCertificateDetailsAPI(APIView):
    def get(self, request, format=None):
        certificate = self.request.query_params.get('certificate_id', None)
        cane_reg = self.request.query_params.get('reg_id', None)
        cane_certificate_details = CaneCertificateDetails.objects.all()
        serializer = CaneCertificateDetailsSerializer(cane_certificate_details, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = CaneCertificateDetailsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CaneSamplingAPI(APIView):
    def get(self, request, format=None):
        season_year = self.request.query_params.get('season_yr_id', None)
        cane_reg = self.request.query_params.get('reg_id', None)
        cane_sampling = CaneSampling.objects.all()
        serializer = CaneSamplingSerializer(cane_sampling, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = CaneSamplingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TransporterTypeMasterAPI(APIView):
    def get(self, request, format=None):
        trans_type = TransporterTypeMaster.objects.all()
        serializer = TransporterTypeMasterSerializer(trans_type, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = TransporterTypeMasterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TransporterMasterAPI(APIView):
    def get(self, request, format=None):
        trans = TransporterMaster.objects.all()
        serializer = TransporterMasterSerializer(trans, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = TransporterMasterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TranVehicleMasterAPI(APIView):
    def get(self, request, format=None):
        season_year = self.request.query_params.get('season_yr_id', None)
        transporter = self.request.query_params.get('transporter_id', None)
        tran_type = self.request.query_params.get('tran_type_id', None)
        tran_vehicle = TranVehicleMaster.objects.all()
        serializer = TranVehicleMasterSerializer(tran_vehicle, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = TranVehicleMasterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HarvesterMasterAPI(APIView):
    def get(self, request, format=None):
        harvester = HarvesterMaster.objects.all()
        serializer = HarvesterMasterSerializer(harvester, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = HarvesterMasterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WeightSlipsAPI(APIView):
    def get(self, request, format=None):
        season_year = self.request.query_params.get('season_yr_id', None)
        canequality = self.request.query_params.get('transporter_id', None)
        cane_reg = self.request.query_params.get('reg_id', None)
        vehicle = self.request.query_params.get('vehicle_id', None)
        tran = self.request.query_params.get('transporter_id', None)
        harv = self.request.query_params.get('harvester_id', None)
        fact = self.request.query_params.get('factory_id', None)
        weight_slips = WeightSlips.objects.all()
        serializer = WeightSlipsSerializer(weight_slips, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = WeightSlipsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WeightSlip_MobileAPI(APIView):
    def get(self, request, format=None):
        season_year = self.request.query_params.get('season_yr_id', None)
        weight_slip_mob = WeightSlip_Mobile.objects.all()
        serializer = WeightSlip_MobileSerializer(weight_slip_mob, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = WeightSlip_MobileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WeightSlip_Mobile_DetailsAPI(APIView):
    def get(self, request, format=None):
        vtrip = self.request.query_params.get('vtrip_id', None)
        cane_class = self.request.query_params.get('season_yr_id', None)
        cquality = self.request.query_params.get('cquality_id', None)
        weight_slip_mob_det = WeightSlip_Mobile_Details.objects.all()
        serializer = WeightSlip_Mobile_DetailsSerializer(weight_slip_mob_det, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = WeightSlip_Mobile_DetailsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HarvestingProgramAPI(APIView):
    def get(self, request, format=None):
        harvest_prog = HarvestingProgram.objects.all()
        serializer = HarvestingProgramSerializer(harvest_prog, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = HarvestingProgramSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)