from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from core import views
from .views import save_user_profile

urlpatterns = [
    path('signup/', views.signup_page, name='signup'),
    path('login/', views.login_page, name='login'),
    path('profile/', views.profile_view, name='profile'),
    re_path(r'^login\.html$', views.login_page),
    path('home/', views.home, name='home'),
    path('search/', views.search_results, name='search_results'),
     path('', views.home, name='home_root'),
    path('conditions/', views.all_conditions, name='all_conditions'),
    path('disease/<int:disease_id>/', views.disease_detail, name='disease_detail'),
    path('autocomplete/', views.autocomplete_search, name='autocomplete_search'),
    path('api/save-profile/', save_user_profile, name='save_user_profile'),
     
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)