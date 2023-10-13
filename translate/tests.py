from django.test import TestCase

from .models import Language, DetailLanguage, LatestUpdate, OurOffer

class LanguageTest(TestCase):
    def test_string_representation(self):
        language = Language(name="English")
        self.assertEqual(str(language), language.name)
        
        
# class DetailLanguageTest(TestCase):
#     def test_string_representation(self):
#         detaillanguage = DetailLanguage(id=1)
#         self.assertEqual(str(detaillanguage), detaillanguage.name)
        
        
class LatestUpdateTest(TestCase):
    def test_string_representation(self):
        latestupdate = LatestUpdate(title="Black spider")
        self.assertEqual(str(latestupdate), latestupdate.title)
        
        
class OurOfferTest(TestCase):
    def test_string_representation(self):
        ouroffer = OurOffer(title="Ouroffer")
        self.assertEqual(str(ouroffer), ouroffer.title)