from django.urls import include, path



urlpatterns = [
    path(
        "account/",
        include(
            ("main.apps.account.urls", "main.apps.account.urls"),
            namespace="account",
        ),
    ),
    path(
        "client/",
        include(
            ("main.apps.client.urls", "main.apps.client.urls"),
            namespace="client",
        ),
    ),
    path(
        "flight/",
        include(
            ("main.apps.flight.flight", "main.apps.flight.flight"),
            namespace="flight",
        ),
    ),
    path(
        "hotel/",
        include(
            ("main.apps.hotel.urls", "main.apps.hotel.urls"),
            namespace="hotel",
        ),
    ),
    path(
        "outfit/",
        include(
            ("main.apps.outfit.urls", "main.apps.outfit.urls"),
            namespace="outfit",
        ),
    ),
    path(
        "expense/",
        include(
            ("main.apps.expense.urls", "main.apps.expense.urls"),
            namespace="expense",
        ),
    ),
    path(
        "transport/",
        include(
            ("main.apps.transport.urls", "main.apps.transport.urls"),
            namespace="transport",
        ),
    ),
    path(
        "visa/",
        include(
            ("main.apps.visa.urls", "main.apps.visa.urls"),
            namespace="visa",
        ),
    ),
    path(
        "package/",
        include(
            ("main.apps.package.urls", "main.apps.package.urls"),
            namespace="package",
        ),
    ),
    path(
        "employee/",
        include(
            ("main.apps.employee.urls", "main.apps.employee.urls"),
            namespace="employee",
        ),
    ),
]

