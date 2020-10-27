from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.template.loader import render_to_string


class HomePageTest(TestCase):
    """ Тест домашней страницы """

    def test_uses_home_template(self):
        """ home page returns correct html"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')