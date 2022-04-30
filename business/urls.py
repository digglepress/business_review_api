from django.urls import include, path

from business import views

app_name = "business"
urlpatterns = [
    path(
        "",
        include(
            [
                path("", views.business_list, name="list"),
                path("create", views.business_create, name="create"),
            ]
        ),
    ),
    path(
        "<business_id>/",
        include(
            [
                path("", views.business_detail, name="detail"),
                path(
                    "reviews/",
                    include(
                        [
                            path(
                                "create",
                                views.business_reviews_create,
                                name="business_reviews_create",
                            ),
                            path(
                                "",
                                include(
                                    [
                                        path(
                                            "",
                                            views.business_reviews,
                                            name="business_reviews",
                                        ),
                                        path(
                                            "<review_id>",
                                            views.business_reviews_detail,
                                            name="business_reviews_detail",
                                        ),
                                    ]
                                ),
                            ),
                        ]
                    ),
                ),
            ]
        ),
    ),
]
