from django.test import TestCase
from app.models import *
# Create your tests here.

class TestQuestionPull(TestCase):
    def test1(self):
        load_questions()
        print(QInfo(1,'question'))
    def testChoiceSplit(self):
        load_questions()
        print(split_choices(1))