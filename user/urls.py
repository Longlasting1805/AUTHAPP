from django.urls import path, include

api_urlpatterns = [

    path('accounts/', include('rest_registration.api.urls')),
]

urlpatterns = [

    path('api/v1/', include(api_urlpatterns)),
]



