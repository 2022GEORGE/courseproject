from django.urls import path,include
from .import views

urlpatterns = [
   path('',views.home,name='home'),
   path('addcourse',views.addcourse,name='addcourse'),
   path('add',views.add,name='add'),
   path('addstudent',views.addstudent,name='addstudent'),
   path('details',views.details,name='details'),
   path('addstudentdb',views.addstudentdb,name='addstudentdb'),
   path('editpage/<int:pk>',views.editpage,name='editpage'),
   path('edit/<int:pk>',views.edit,name='edit'),
   path('delt/<int:pk>',views.delt,name='delt')
]
