from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import RedirectView, ListView, CreateView

from accounts.forms import VacancyForm
from new_app.models import Vacancy


class IndexView(ListView):
    template_name = 'index.html'
    model = Vacancy
    context_object_name = 'vacancies'


class IndexRedirectView(RedirectView):
    pattern_name = 'index'


class VacancyCreateView(LoginRequiredMixin, CreateView):
    template_name = "vacancy_create.html"
    model = Vacancy
    form_class = VacancyForm

    def get_success_url(self):
        return reverse_lazy('index')



