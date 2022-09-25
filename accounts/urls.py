from django.urls import path

from .views import *

urlpatterns = [
    path('login/', login_page, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout_page, name='logout'),
    path('tester/<int:pk>', tester, name='tester'),
]

handler404 = 'accounts.views.error_404'
handler500 = 'accounts.views.error_500'