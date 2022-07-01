from django.test import TestCase

from board.models import IndexPage


class IndexPageModelTests(TestCase):
    def setUp(self):
        IndexPage.objects.create(
            welcome_title="welcome1", welcome_description="desc1", is_default=True
        )
        IndexPage.objects.create(
            welcome_title="welcome2", welcome_description="desc2", is_default=True
        )

    def test_indexpage_default_condition(self):
        default_index_welcome = IndexPage.objects.get(is_default=True).welcome_title
        self.assertEqual(default_index_welcome, "welcome2")
