from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = '__all__'  

class PermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permiso
        fields = '__all__'  

class ModuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modulo
        fields = '__all__'  

class ComisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comision
        fields = '__all__'  

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'