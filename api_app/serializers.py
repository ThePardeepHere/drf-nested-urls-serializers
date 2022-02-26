from rest_framework import serializers
from .models import *

class SectionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Class_Section
        fields=('id', 'section_name', 'school_class',)

    def to_representation(self, instance):
        """Removing School object while get/return class method"""
        ret = super().to_representation(instance)
        ret.pop('school_class')
        return ret

class ClassSerializer(serializers.ModelSerializer):
    class_section=SectionSerializer(many=True,required=False)
    class Meta:
        model=School_Class
        fields=('id', 'class_name','class_section','school', )
    
    def to_representation(self, instance):
        """Removing School object while get/return class method"""
        ret = super().to_representation(instance)
        ret.pop('school')
        return ret
    
    def create(self, validated_data):
        if 'class_section' in validated_data:
            validated_data.pop('class_section')
        school_class =School_Class.objects.create(**validated_data)
        return school_class

    def update(self, instance, validated_data):
        if 'class_section' in validated_data:
            validated_data = validated_data.pop('class_section')

        return super(ClassSerializer, self).update(instance, validated_data)


class SchoolSerializer(serializers.ModelSerializer):
   
    school_class=ClassSerializer(many=True,required=False)
   
    class Meta:
        model=School
        fields=('id','school_name', 'city', 'country','school_class', )

    

    def create(self, validated_data):
        if 'school_class' in validated_data:
            validated_data.pop('school_class')
        school =School.objects.create(**validated_data)
        return school

    def update(self, instance, validated_data):
        if 'school_class' in validated_data:
            validated_data = validated_data.pop('school_class')

        return super(SchoolSerializer, self).update(instance, validated_data)
