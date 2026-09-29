from Extractor.base import BaseExtractor

class GoogleAdsExtractor(BaseExtractor):
    
    def __init__(self, client_id):
        self.client_id = client_id
    
    def extract(self):
        print(f"Extracting data from Google Ads for client {self.client_id}")
        
        data = [
            {
                "platform": "google_ads",
                "campaign": "Search Campaign",
                "impressions": 12000,
                "clicks": 850,
                "spend": 450,
                "conversions": 32
            }
        ]

        return data