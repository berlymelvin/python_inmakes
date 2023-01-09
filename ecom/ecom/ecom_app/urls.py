from django.urls import path
from ecom_app import views
app_name='ecom_app'
urlpatterns = [
    path('',views.AllProductCat,name='AllProductCat'),
    path('<slug:c_slug>/',views.AllProductCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name='proCatDetail'),
]