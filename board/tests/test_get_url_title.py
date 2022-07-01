from django.test import TestCase

from board import get_url_title


class GetUrlTitleTest(TestCase):
    def test_get_url_title(self):
        title = get_url_title.get_title("https://www.google.com/")
        self.assertEqual(title, "Google")
