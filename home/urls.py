from django.urls import path
from django.conf import settings  
from django.conf.urls.static import static 
from home import views  
from.views import logout_view

urlpatterns = [
    path('', views.index, name="index"),
    path('edit/<int:id>/',views.edit, name="edit"),
    path('remove/<int:id>/',views.remove, name="remove"),
    path('login/', views.login_view, name="login"),
    path('signup/', views.signup, name="signup"),
    path('logout/', logout_view, name="logout_view")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
