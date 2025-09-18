from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name=serializers.CharField()
    email=serializers.EmailField()
    contact=serializers.IntegerField()
    
    def create(self, validated_data):
        """
        Create and return a new `App` instance, given the validated data.
        """
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
            """
            Update and return an existing `App` instance, given the validated data.
            """
            instance.name = validated_data.get('name', instance.name)
            instance.email = validated_data.get('email', instance.email)
            instance.contact = validated_data.get('contact', instance.contact)
            instance.save()
            return instance