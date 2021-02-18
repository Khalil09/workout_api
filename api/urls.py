from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

router = routers.DefaultRouter()
# router.register(r'workout', views.WorkoutViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', views.api_root),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('workout/', views.WorkoutList.as_view(), name='workout-list'),
    path('workout/<int:pk>', views.WorkoutDetail.as_view(), name='workout-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)