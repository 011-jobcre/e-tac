from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "homepage.html"
    # template_name = "etac_page.html"


class AboutView(TemplateView):
    template_name = "about.html"


class ServicesView(TemplateView):
    template_name = "services.html"


class ContactView(TemplateView):
    template_name = "contact.html"


class InquiryView(TemplateView):
    template_name = "inquiry.html"


class GroupView(TemplateView):
    template_name = "group.html"
