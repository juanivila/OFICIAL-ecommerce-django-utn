from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from .forms import ContactoForm


class Contacto(FormView):
	template_name = 'contacto/contacto.html'
	success_url = reverse_lazy('contacto:success-contacto')
	form_class = ContactoForm
	
	def form_valid(self, form):
		form.save()
		return super().form_valid(form)


class SuccessContacto(TemplateView):
	template_name = 'contacto/success-contacto.html'
