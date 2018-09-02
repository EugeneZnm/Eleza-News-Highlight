# import articles
import unittest

# import class Articles
from app.models import Articles


class ArticlesTest(unittest.TestCase):
    """
    Parent class to test articles variables

    """

    def setUp(self):
        """
        method to run before every test

        """
        self.new_article = Articles("abc-news", "Luke Barr", "For safety on campuses, law enforcement increasingly "
                                                             "turns to apps",
                                    "The apps allow students to communicate more effectively with safety officers.",
                                    "https://abcnews.go.com/US/safety-campuses-law-enforcement-increasingly-turns-apps"
                                    "/story?id=57558628",
                                    "https://s.abcnews.com/images/US/police-security-gty-jt-180902_hpMain_16x9_992.jpg",
                                    "2018-09-02T19:57:44Z")
