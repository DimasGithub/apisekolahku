from rest_framework import serializers
from visimisi.models import Visimisi, Pengajarstaff, Pengumuman, Jadwal, Pengaturan

class SerializerVisimisi(serializers.ModelSerializer):
    class Meta:
        model = Visimisi
        fields = '__all__'

class SerializerPengajarstaff(serializers.ModelSerializer):
    class Meta:
        model = Pengajarstaff
        fields = '__all__'

class SerializerPengumuman(serializers.ModelSerializer):
    class Meta:
        model = Pengumuman
        fields = '__all__'

class SerializerJadwal(serializers.ModelSerializer):
    class Meta:
        model = Jadwal
        fields = '__all__'

class SerializerPengaturan(serializers.ModelSerializer):
    class Meta:
        model = Pengaturan
        fields = '__all__'