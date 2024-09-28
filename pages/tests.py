from django.test import TestCase
from django.urls import reverse

class PageTests(TestCase):

    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))  # تأكد من أن الاسم هنا صحيح
        self.assertEqual(response.status_code, 200)  # تحقق من أن الحالة 200

    def test_about_page_status_code(self):
        response = self.client.get(reverse('about'))  # تأكد من أن الاسم هنا صحيح
        self.assertEqual(response.status_code, 200)  # تحقق من أن الحالة 200

    def test_home_template_used(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'pages/home.html')  # تأكد من استخدام القالب الصحيح

    def test_about_template_used(self):
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'pages/about.html')  # تأكد من استخدام القالب الصحيح
