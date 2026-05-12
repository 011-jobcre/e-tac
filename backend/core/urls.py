from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from .views import (
    HomeView,
    AboutView,
    ServicesView,
    ContactView,
    InquiryView,
    GroupView,
    chubunrui_options,
    shobunrui_options,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),
    path("rosetta/", include("rosetta.urls")),
]

urlpatterns += i18n_patterns(
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("services/", ServicesView.as_view(), name="services"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("inquiry/", InquiryView.as_view(), name="inquiry"),
    path("group/", GroupView.as_view(), name="group"),
    path("api/chubunrui-options/", chubunrui_options, name="chubunrui-options"),
    path("api/shobunrui-options/", shobunrui_options, name="shobunrui-options"),
)
