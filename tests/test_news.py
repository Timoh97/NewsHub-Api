import unittest
from app.models import News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News('https://image.tmdb.org/t/p/w500/khsjha27hbs','toydas','Good to be alive','A not Javascript,funny!',897899,'Read more')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))
        
    def test_name(self):
        name_var = self.new_news.name
        self.assertTrue(name_var == "toydas")
        
    def test_title(self):
        title_var = self.new_news.title
        self.assertTrue(title_var == "Good to be alive")
        
    def test_description(self):
        description_var = self.new_news.descripion
        self.assertTrue(description_var == "A not Javascript,funny!")
        
    def test_publishedAt(self):
        publishedAt_int = self.new_news.publishedAt
        self.assertTrue(publishedAt_int == 897899)
        
    def test_url(self):
        url_var = self.new_news.url
        self.assertTrue(url_var == "url")
    
    
if __name__ == '__main__':
    unittest.main()