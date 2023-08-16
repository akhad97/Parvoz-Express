from django.urls import include, path

app_name = "flight"

urlpatterns = [
    path(
        "",
        include(
            ("main.apps.flight.urls.flight", "main.apps.flight.urls.flight"),
            namespace="",
        ),
    ),
    path(
        "",
        include(
            ("main.apps.flight.urls.calculation", "main.apps.flight.urls.calculation"),
            namespace="",
        ),
    )
]
