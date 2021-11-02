from newsapi import NewsApiClient
# from ..config import from news
 
class NewsRequests:
   API_KEY = '2c668aaf75c744c190238ad94b7efe83'
   n = NewsApiClient(api_key=API_KEY)
  
   def get_top_headlines(self,**kwargs):
       return self.n.get_top_headlines(**kwargs)
  
   def get_everything(self,**kwargs):
       return self.n.get_everything(**kwargs)
  
   def get_sources(self,**kwargs):
       return self.n.get_sources(**kwargs)
