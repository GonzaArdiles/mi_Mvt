from django.urls import path
from django.contrib import admin
from familia.views import familia,familiar2,familiar3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('familia/', familia),
    path('familiar2/', familiar2),
    path('familiar3/', familiar3)

]
