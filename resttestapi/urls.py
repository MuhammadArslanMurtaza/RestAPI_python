from django.urls import path
from resttestapi.views import index,loginss,loguots,saveemp,Employee_list,employeedetails,Employeeview,employeedetail

urlpatterns = [
    path('', index),
    path('userlogin', loginss),
    path('loguots',loguots),
    path('saveemp',saveemp),
    path('employee_list',Employee_list),
    path('employee/<int:pk>', employeedetails),
    path('employeeview',Employeeview.as_view()),
    # path('employeedetail/<int:id>',employeedetails.as_view()),
    path('employeedetail', employeedetail.as_view()),
]