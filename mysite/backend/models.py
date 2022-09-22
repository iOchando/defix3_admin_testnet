from cgi import test
#from tkinter import CASCADE
from django.db import models
from django.forms import DateField, DateTimeField
from django.db.models.signals import post_save
from django.contrib.auth.models import *

# Create your models here.

class Perfil(models.Model):
    TIPO=(('S','Super'),('A','Admin'),('U','Usuario'),('B','Banco'))
    usuario=models.OneToOneField(User,on_delete=models.CASCADE,help_text="usuario asociado")
    activo=models.BooleanField(default=True,help_text="esta el usuario activo?")
    #avatar=models.ImageField(upload_to='avatars',null=True,help_text="avatar para el usuario")
    tipo=models.CharField(max_length=1,null=True,choices=TIPO,default='U',help_text="Tipo de usuario")
    def __str__(self):
        return '%s - %s'%(self.usuario.username, self.tipo)

class Modulo(models.Model):
    nombre=models.CharField(max_length=255, null=False, blank=False, primary_key=True)
    #mayor=models.ForeignKey('self',default=None,null=True, on_delete=models.SET_DEFAULT)
    def __str__(self):
        return '%s'%(self.nombre)

class Permiso(models.Model):
    modulo=models.ForeignKey(Modulo,null=False,blank=False,on_delete=models.CASCADE,help_text="Opcion de menu asociada")
    perfil=models.ForeignKey(Perfil,null=False,blank=False,on_delete=models.CASCADE,help_text="Usuario asociado")
    # Metodos
    leer=models.BooleanField(default=False,help_text="Tiene opcion de leer?")
    escribir=models.BooleanField(default=False,help_text="Tiene opcion de escribir?")
    borrar=models.BooleanField(default=False,help_text="Tiene opcion de borrar?")
    actualizar=models.BooleanField(default=False,help_text="Tiene opcion de actualizar?")
 
    # def save(self):
    #     if not Permiso.objects.filter(perfil=self.perfil_id,da=self.menuinstancia_id):
    #         super().save()
    def __str__(self):
        return '%s (Permiso: %s - Leer:%s Borrar:%s Actualizar:%s Escribir:%s)'%(self.perfil.usuario.username,self.modulo.nombre,self.leer,self.borrar,self.actualizar,self.escribir)

class Comision(models.Model):
    coin=models.CharField(max_length=32, null=False, blank=False, primary_key=True)
    nombre=models.CharField(max_length=255, null=False, blank=False)
    blockchain=models.CharField(max_length=255, null=False, blank=False)
    transfer=models.FloatField(null=False, blank=False)
    swap=models.FloatField(null=False, blank=False)
    fiat=models.FloatField(null=False, blank=False)
    #mayor=models.ForeignKey('self',default=None,null=True, on_delete=models.SET_DEFAULT)
    def __str__(self):
        return '%s'%(self.coin)