from django.test import TestCase
from .models import Project


class ProjectTestCase(TestCase):
    def setUp(self):
        Project.objects.create(title="Test project", video_url="https://www.youtube.com/watch?v=zX7MNbK-Cvw")

    def test_get_emebed_url(self):
        """Embed url is different from the video url so should return different url"""
        my_project = Project.objects.first()
        self.assertEqual(my_project.get_embed_url, 'https://www.youtube.com/embed/zX7MNbK-Cvw')
