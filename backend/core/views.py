from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from .models import Chubunrui, Shobunrui
from .forms import InquiryForm


class HomeView(TemplateView):
    template_name = "homepage.html"


class AboutView(TemplateView):
    template_name = "about.html"


class ServicesView(TemplateView):
    template_name = "services.html"


class ContactView(TemplateView):
    template_name = "contact.html"


class InquiryView(FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy("inquiry")


class GroupView(TemplateView):
    template_name = "group.html"


def chubunrui_options(request):
    """HTMX endpoint: trả về options cho 中分類"""
    dai_code = request.GET.get("daibunrui")

    chubunrui_list = Chubunrui.objects.filter(daibunrui_id=dai_code).values(
        "code", "name"
    )

    return render(
        request,
        "inquiry/partials/_chubunrui_select.html",
        {
            "chubunrui_list": chubunrui_list,
            "selected_dai": dai_code,
        },
    )


def shobunrui_options(request):
    """HTMX endpoint: trả về options cho 小分類"""
    chu_code = request.GET.get("chubunrui")

    shobunrui_list = Shobunrui.objects.filter(chubunrui_id=chu_code).values(
        "code", "name"
    )

    return render(
        request,
        "inquiry/partials/_shobunrui_select.html",
        {
            "shobunrui_list": shobunrui_list,
            "selected_chu": chu_code,
        },
    )
