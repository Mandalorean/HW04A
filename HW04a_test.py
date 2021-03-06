# By Pranav
import unittest
from HW04a import getrepo

class TestGitHub(unittest.TestCase):

    def testGithub1(self):
        self.assertEqual(getrepo('aljhdfjabfbfb'), False)

    def testGithub2(self):
        self.assertNotEqual(getrepo('aljhdfjabfbfb'), True)

    def testGithub3(self):
        self.assertEqual(getrepo('Pranavzagade'), False)

    def testGithub4(self):
        self.assertNotEqual(getrepo('GautamP2393'), True)

    def testGithub5(self):
        self.assertEqual(getrepo('Mandalorean'), True)
