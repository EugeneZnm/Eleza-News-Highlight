# import unittest
import unittest


# import class Sources
from app.models import Sources


class SourcesTest(unittest.TestCase):
    """
    Test instances of test class

    """
    def setUp(self):
        """
        setup method to run before tests
        :return:
        """
        self.new_source = Sources("abc-news", "ABC News", "Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.", "http://abcnews.go.com",
                                  "general","en", "us")

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_source.id, 'abc-news')
        self.assertEquals(self.new_source.name, 'ABC News')
        self.assertEquals(self.new_source.description, 'Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.')
        self.assertEquals(self.new_source.url, 'http://abcnews.go.com')
        self.assertEquals(self.new_source.url, 'general')
        self.assertEquals(self.new_source.country, 'us')
        self.assertEquals(self.new_source.language, 'en')

