from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


schema_view = get_schema_view(
    openapi.Info(
        title="New Project API",
        default_version="v1",
        description="New Project API Documentation ",
        # terms_of_service="https://www.eazyrooms.com/policies/terms/",
        # contact=openapi.Contact(email="eazyrooms@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
