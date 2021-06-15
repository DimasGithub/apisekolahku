from django.shortcuts import render
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser, FileUploadParser
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from visimisi.serializer import SerializerVisimisi, SerializerPengajarstaff, SerializerPengumuman, SerializerJadwal, SerializerPengaturan
from visimisi.models import Visimisi, Pengajarstaff, Pengumuman, Jadwal, Pengaturan
from django.http import JsonResponse
from rest_framework import generics
from rest_framework import views

@api_view(['GET', 'PUT'])
def TampilData(request, id):
    try:
        query = Visimisi.objects.filter(id = id)
        snippet = Visimisi.objects.get(id = id)
    except snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = SerializerVisimisi(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print('data tidak valid')
    elif request.method == 'GET':
        serializer = SerializerVisimisi(query, many=True)
        return JsonResponse(serializer.data, safe=False)
    return JsonResponse(serializer.errors)

@api_view(['GET','POST'])
def Datapengajarstaff(request):
    try:
        query = Pengajarstaff.objects.all()
    except Pengajarstaff.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = SerializerPengajarstaff(query, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        pengajar_serializer = SerializerPengajarstaff(data=request.data)
        if pengajar_serializer.is_valid():
            pengajar_serializer.save()
            return JsonResponse(pengajar_serializer.data)
        else:
            print('input tidak valid')
        return JsonResponse(pengajar_serializer.errors)

@api_view(['GET', 'PUT','DELETE'])
def Detailpengajarstaff(request, id):
    try:
        query = Pengajarstaff.objects.filter(id=id)
        snippet = Pengajarstaff.objects.get(id=id)
    except Pengajarstaff.DoesNotExist:
        return JsonResponse(query.data)
    if request.method  == 'GET':
        serializer = SerializerPengajarstaff(query, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        pengajar_serializer = SerializerPengajarstaff(snippet, data=request.data)
        if pengajar_serializer.is_valid():
            pengajar_serializer.save()
            return Response(pengajar_serializer.data)
        else:
            print('data tidak valid')
            return Response(pengajar_serializer.data)
    elif request.method == 'DELETE':
        serializer = SerializerPengajarstaff(query, many=True)
        serial = Pengajarstaff.objects.filter(id=id).first()
        serial.delete()
        return Response(serializer.data)      

@api_view(['GET','POST'])
def Datapengumuman(request):
    if request.method == 'GET':
        query = Pengumuman.objects.order_by('-date_created')
        serializer = SerializerPengumuman(query, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        pengumuman_serializer = SerializerPengumuman(data=request.data)
        if pengumuman_serializer.is_valid():
            pengumuman_serializer.save()
            return JsonResponse(pengumuman_serializer.data)
        else:
            print('data tidak valid')
        return JsonResponse(query.data, safe=False)

@api_view(['GET', 'PUT', 'DELETE'])
def Detaildatapengumuman(request, id):
    try:
        query = Pengumuman.objects.filter(id=id)
        snippet = Pengumuman.objects.get(id=id)
    except Pengumuman.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = SerializerPengumuman(query, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        pengumuman_serializer = SerializerPengumuman(snippet, data=request.data)
        if pengumuman_serializer.is_valid():
            pengumuman_serializer.save()
            return Response(pengumuman_serializer.data)
    elif request.method == 'DELETE':
        serializer=SerializerPengumuman(query, many=True)
        serial = Pengumuman.objects.filter(id=id).first()
        serial.delete()
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def Datajadwal(request):
    query = Jadwal.objects.order_by('-date_schedule')
    if request.method == 'GET':
        serializer = SerializerJadwal(query, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        jadwal_serializer = SerializerJadwal(data=request.data)
        if jadwal_serializer.is_valid():
            jadwal_serializer.save()
            return JsonResponse(jadwal_serializer.data)
        else:
            print('data tidak betul')
            return Response(query.data)

@api_view(['GET', 'PUT', 'DELETE'])
def Detaildatajadwal(request, id):
    try:
        query = Jadwal.objects.filter(id=id)
        snippet = Jadwal.objects.get(id=id)
    except Jadwal.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = SerializerJadwal(query, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        jadwal_serializer = SerializerJadwal(snippet, data=request.data)
        print(jadwal_serializer)
        if jadwal_serializer.is_valid():
            jadwal_serializer.save()
            return JsonResponse(jadwal_serializer.data, safe=False)
    elif request.method == 'DELETE':
        serializer = SerializerJadwal(query, many=True)
        serial = query.first()
        serial.delete()
        return Response(serializer.data)

class FileUploadView(generics.ListAPIView):
    parser_classes = [FileUploadParser]
    def get_queryset(self):
        queryset= Pengaturan.objects.all()
        return queryset
    def put(self, request, filename, format=None):
        imageid = self.request.POST.get('id')
        f_obj = Pengaturan.objects.filter(id=imageid)
        fileserializer = SerializerPengaturan(f_obj, data=request.data)
        if fileserializer.is_valid():
            fileserializer.save()
            return Response(status=204)
        else:
            print('gagal')
            return Response(status=201)

@api_view(['GET', 'PATCH'])
def Datapengaturan(request, id):
    snippet = Pengaturan.objects.get(id=id)
    query = Pengaturan.objects.filter(id = id)
    if request.method == 'PATCH':
        serializer = SerializerPengaturan(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print('data tidak valid')
            return Response(serializer.data)
    elif request.method == 'GET':
        serializer = SerializerPengaturan(query, many=True)
        return JsonResponse(serializer.data, safe=False)