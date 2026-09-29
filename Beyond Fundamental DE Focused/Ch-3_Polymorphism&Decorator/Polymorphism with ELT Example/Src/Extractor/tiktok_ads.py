from Extractor.base import BaseExtractor

class TikTokAdsExtractor(BaseExtractor):
    
    def __init__(self, client_id):
        self.client_id = client_id
    
    def extract(self):
        print(f"Extracting data from TikTok Ads for client {self.client_id}")
        
        data = [
            {
                "platform": "tiktok_ads",
                "campaign": "TikTok Awareness Campaign",
                "impressions": 15000,
                "clicks": 900,
                "spend": 500,
                "conversions": 40
            }
        ]

        return data