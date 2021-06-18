from django.urls import path
from . import views

app_name='products'

urlpatterns = [
    path('', views.index,name="home"),
    path('keyword/', views.index_keyword,name="home_keyword"),
    path('ad-details/<int:id>',views.ad_details,name='ad-details'),
    path('admin-details/<int:id>',views.admin_details,name='admin-details'),
    path('approved/<int:id>',views.approved,name='approved'),
    path('rejected/<int:id>',views.rejected,name='rejected'),
    path('sell/',views.sell,name="sell"),
    path('admin/',views.admin_view,name="admin-view"),
    path('save_item/',views.save_item,name="save_item")
]

