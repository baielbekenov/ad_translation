from django.test import TestCase

from .models import Language

class LanguageTest(TestCase):
    def test_string_representation(self):
        language = Language(name="English")
        self.assertEqual(str(language), language.name)