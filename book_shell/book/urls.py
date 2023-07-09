from django.urls import path
from . import views
# from django.conf import settings
# from django.conf.urls.static import static

# Add the following lines at the end of the file



urlpatterns = [
    path('index/', views.say_hello),
    path('form/',),
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




