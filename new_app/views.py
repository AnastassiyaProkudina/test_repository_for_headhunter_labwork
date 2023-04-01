from django.views.generic import RedirectView, ListView

from new_app.models import Vacancy


class IndexView(ListView):
    template_name = 'index.html'
    model = Vacancy
    context_object_name = 'vacancies'


class IndexRedirectView(RedirectView):
    pattern_name = 'index'



