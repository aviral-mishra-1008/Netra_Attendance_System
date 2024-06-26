from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home"),
    path('profLogin/',views.profLogin,name="profLogin"),
    path('profRegister/',views.prof,name="profRegister"),
    path('studLogin/',views.studLogin,name="studLogin"),
    path('camera/',views.TakeAttendance,name='cameraFeed'),
    path('attendance/',views.BeginCameraFeed,name='BegincameraFeed'),
    path('registerSubjects/',views.Subjects, name="Subject"),
    path('addStudent/',views.makeEmbed, name="addStudent"),
    path('studLogin/',views.studLogin,name="studLogin"),
    path('studRegister/',views.studRegistration,name="studRegister"),
    path('percent/',views.percent,name="percent"),
    path('logout/',views.Logout,name="logout"),
    path('adminView/',views.adminView,name="adminView"),
    path('adminLogin/',views.adminLogin,name="adminLogin"),
    path('countStudent/',views.counts, name='count')
]
