from django.urls import path, include
from .views import Datapengaturan, FileUploadView, TampilData, Datapengajarstaff, Detailpengajarstaff, Datapengumuman, Detaildatapengumuman,Datajadwal, Detaildatajadwal
urlpatterns = [
    path('visimisi/<int:id>', TampilData, name='TampilDataVisimisi'),
    path('pengajarstaff/',Datapengajarstaff, name='DataPengajarStaff'),
    path('Detailpengajarstaff/<int:id>', Detailpengajarstaff, name='Detailpengajarstaff' ),
    path('pengumuman/', Datapengumuman, name= 'DataPengumuman' ),
    path('pengumuman/<int:id>', Detaildatapengumuman, name='Detaildatapengumuman'),
    path('jadwal/', Datajadwal, name="datajadwal"),
    path('jadwal/<int:id>', Detaildatajadwal, name='Detaildatajadwal'),
    # path('pengaturan/<str:filename>', FileUploadView.as_view(), name='Datapengaturan'),
    path('pengaturan/<int:id>', Datapengaturan, name='Datapengaturandetail'),

]