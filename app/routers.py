from rest_framework import routers
from .views import StudentVs

router = routers.DefaultRouter()
router.register(r'Student', StudentVs)
urlpatterns = router.urls