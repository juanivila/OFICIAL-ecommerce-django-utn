from django.views.generic import TemplateView, FormView


class Contact(FormView):
	template_name = 'contacto.html'
