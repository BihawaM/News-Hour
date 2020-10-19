import unittest
from app.models import Article

Article = article.Article

class ArticleTest(unittest.Testcase):
    '''
    Test Class to test the behaviour of the News class
    '''
    
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.article = Article('Mariella Moon','Digital Currency','There might be a plan of creating a digital currency','https://www.bbc.co.uk/news/business-54261382','https://ichef.bbci.co.uk/news/1024/branded_news/C414/production/_114569105_chandler.racks.jpg','2020-09-24T23:16:08Z','Image copyrightChandler GuoImage caption Chandler Guo at one of his cryptocurrency mines Chandler Guo was a pioneer in cryptocurrency, the digital currencies that can be created and used independe… [+5995 chars]')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))   
        
        
if __name__ == '__main__':
    unittest.main()         