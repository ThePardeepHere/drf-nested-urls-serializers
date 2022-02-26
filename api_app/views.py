from functools import partial
from rest_framework.response import Response
from rest_framework import viewsets,status,mixins
from .models import *
from rest_framework.generics import RetrieveUpdateAPIView,RetrieveAPIView
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from .serializers import *

class SchoolViewSet(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,
                    mixins.ListModelMixin,GenericViewSet,mixins.CreateModelMixin):

        serializer_class=SchoolSerializer
        queryset=School.objects.all()
        
        @action(methods=["get","post"],detail=True,
                url_name="school_class",url_path="school-class",
                serializer_class=ClassSerializer)
        def SchoolClassListView(self,request,pk):
            if request.method=="POST":
                serializer=ClassSerializer(data=request.data)
                if serializer.is_valid():
                     serializer.save(school_id=pk)
                     return Response(serializer.data)
                else:
                    return Response(serializer.errors)

            if request.method=="GET":             
                queryset=School_Class.objects.filter(school=pk)
                serializer=ClassSerializer(queryset,many=True)
                return Response(serializer.data)


        @action(methods=["get","patch"],detail=True,
                url_name="school_class_details",url_path="school-class/(?P<class_id>\d+)",
                serializer_class=ClassSerializer)
        def SchoolClassDetailView(self,request,pk,class_id):
            if request.method=="PATCH":
                instance=School_Class.objects.filter(pk=class_id,school=pk).first()
                serializer=ClassSerializer(instance,request.data,partial=True)
                if serializer.is_valid():
                     serializer.save()
                     return Response(serializer.data)
                else:
                    return Response(serializer.errors)

            if request.method=="GET":             
                queryset=School_Class.objects.filter(pk=class_id,school=pk).first()
                serializer=ClassSerializer(queryset)
                return Response(serializer.data)         

        @action(methods=["get","post"],detail=True,
                url_name="school_class_section",url_path="school-class/(?P<class_id>\d+)/sections",
                serializer_class=SectionSerializer)
        def SchoolClassSectionListView(self,request,pk,class_id):
            if request.method=="POST":
                serializer=SectionSerializer(data=request.data)
                if serializer.is_valid():
                     serializer.save(school_class_id=class_id)
                     return Response(serializer.data)
                else:
                    return Response(serializer.errors)

            if request.method=="GET":             
                queryset=Class_Section.objects.filter(school_class=class_id,school_class__school=pk)
                serializer=SectionSerializer(queryset,many=True)
                return Response(serializer.data)


        @action(methods=["get","patch"],detail=True,
                url_name="school_class_section_details",url_path="school-class/(?P<class_id>\d+)/sections/(?P<section_id>\d+)",
                serializer_class=SectionSerializer)
        def SchoolClassSectionDetailView(self,request,pk,class_id,section_id):
            if request.method=="PATCH":
                instance=Class_Section.objects.filter(school_class=class_id,school_class__school=pk,pk=section_id).first()
                serializer=SectionSerializer(instance,request.data,partial=True)
                if serializer.is_valid():
                     serializer.save()
                     return Response(serializer.data)
                else:
                    return Response(serializer.errors)

            if request.method=="GET":             
                queryset=Class_Section.objects.filter(school_class=class_id,school_class__school=pk,pk=section_id).first()
                serializer=SectionSerializer(queryset)
                return Response(serializer.data)      
      