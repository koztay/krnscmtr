from django.views.generic.base import TemplateView
from portfolio.models import Project, PortfolioShortIntro


from .models import SliderImageThumb


class HomePageView(TemplateView):

    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        context['slider_thumbs'] = SliderImageThumb.objects.all().order_by('?')
        context['short_intro'] = PortfolioShortIntro.objects.first()
        print('short_intro', context['short_intro'])

        return context
