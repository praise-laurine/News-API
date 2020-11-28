import unittest
from models import Source
News = news.News

class SourcesTest(unittest.Testcase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up mthod that will run before every Test
        '''
        self.new_source = Source('abc-news','ABC news','Your trusted source for breaking news',"https://abcnews.go.com","general","en","us")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

if __name__ == '__main__':
    unittest.main()
             

