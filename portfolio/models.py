from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.


class Project(models.Model):
    PROJECT_TYPES = (
        ('videowall', 'Videowall'),
        ('cctv', 'CCTV'),
        ('signage', 'Digital-Signage'),
        ('global', 'LG-Global'),
    )
    title = models.CharField(max_length=150)
    slug = models.SlugField(blank=True, unique=True, max_length=200)  # unique=True)
    description = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=50, choices=PROJECT_TYPES, default='Videowall')
    finished_date = models.DateField(null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)  # if not null than just show video and ignore the rest

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        view_name = "projects:project_detail"
        return reverse(view_name, kwargs={"slug": self.slug})

    class Meta:
        ordering = ("-finished_date", "title")


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images')
    image = models.ImageField(upload_to="images/portfolio_images")


# Bu model ne  işe yarıyor anlamadım? Boşu boşuna koymuşum.
class PortfolioShortIntro(models.Model):
    intro_text = models.TextField()

    def __str__(self):
        return self.intro_text

