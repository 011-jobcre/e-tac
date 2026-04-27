from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "homepage.html"

class AboutView(TemplateView):
    template_name = "about_us.html"

class ServicesView(TemplateView):
    template_name = "services.html"

class ContactView(TemplateView):
    template_name = "contact_us.html"
