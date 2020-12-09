from django.test import TestCase

from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse

class testFunc(StaticLiveServerTestCase):

    def test_foo(self):
        self.assertEquals(1,1) 
