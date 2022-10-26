from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import *

router = SimpleRouter()

router.register(r'pip', MusicdirViewSet)

urlpatterns = [
    path('', HomeMusicdir.as_view(), name='home'),
    path('category/<int:category_id>#', get_category, name='category'),
    path('login', login, name='login'),
    path('register', register, name='register'),

]

urlpatterns += router.urls
