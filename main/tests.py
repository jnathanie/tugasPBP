from django.test import TestCase
from django.urls import reverse, resolve
from main.views import show_main

# Create your tests here.
class TestUrls(TestCase):
    def test_urls(self):
        url = reverse("main:show_main")
        self.assertEquals(resolve(url).func, show_main)