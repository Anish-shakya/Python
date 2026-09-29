from Extractor.base import BaseExtractor

class MetaAdsExtractor(BaseExtractor):
    
    def __init__(self, client_id):
        self.client_id = client_id
    
    def extract(self):
        print(f"Extracting data from Meta Ads for client {self.client_id}")
        
        data = [
            {
                "platform": "meta_ads",
                "campaign": "Instagram Retargeting",
                "impressions": 18000,
                "clicks": 1200,
                "spend": 600,
                "conversions": 45
            }
        ]

        return data