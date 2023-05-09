
from django.urls import path
from django.contrib import admin


from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("index/", views.index2, name="index2"),
    path("create/", views.create, name="EntryPage"),
    path("empC/", views.empC, name="EntryPage"),

    path("read/", views.read, name="ReadPage"),
    path("empread/", views.empread, name="ReadPage"),
    path("allread/", views.empread, name="ReadPage"),
    path("view/", views.view),
    path("delete/", views.delete),
    path("edit/", views.edit),
    path("update/", views.update),
    # path("show/", views.showformatdata),


# path('save-pdf/', save_pdf, name='save-pdf'),
]
