from django.urls import path,include
from .import views

urlpatterns = [
   path('',views.welcome,name='welcome'),
   path('home',views.home,name='home'),
   path('addcourse',views.addcourse,name='addcourse'),
   path('add',views.add,name='add'),
   path('addstudent',views.addstudent,name='addstudent'),
   path('details',views.details,name='details'),
   path('addstudentdb',views.addstudentdb,name='addstudentdb'),
   path('editpage/<int:pk>',views.editpage,name='editpage'),
   path('edit/<int:pk>',views.edit,name='edit'),
   path('delt/<int:pk>',views.delt,name='delt'),
   path('loginfun',views.loginfun,name='loginfun'),
   path('logout',views.logout,name='logout'),
   path('signup',views.signup,name='signup'),
   path('addteacher',views.addteacher,name='addteacher'),
   path('teacher',views.teacher,name='teacher'),
   path('teachetdetails',views.teacherdetails,name='teacherdetails'),
   path('dele/<int:pk>',views.dele,name='dele'),
   path('profile',views.profile,name='profile'),
   path('teacheredit',views.teacheredit,name='teacheredit'),
   path('updatedb/<int:pk>',views.updatedb,name='updatedb')
]
