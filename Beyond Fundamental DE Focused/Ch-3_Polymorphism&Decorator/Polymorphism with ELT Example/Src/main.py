from Extractor.google_ads import GoogleAdsExtractor
from Extractor.meta_ads import MetaAdsExtractor
from Extractor.tiktok_ads import TikTokAdsExtractor

from Loader.warehouse import WarehouseLoader

from Pipeline.pipeline import DataPipeline


def main():
    
    ### creating extractors for different platforms
    
    google_ads_extractor = GoogleAdsExtractor("google_client_123")
    meta_ads_extractor = MetaAdsExtractor("meta_client_456")
    tiktok_ads_extractor = TikTokAdsExtractor("tiktok_client_789")
    
    Extractors = [google_ads_extractor, meta_ads_extractor, tiktok_ads_extractor]
    
    loader = WarehouseLoader("DataWarehouse", "DW_001")
    
    pipeline = DataPipeline(Extractors, loader)
    pipeline.run()
    
if __name__ == "__main__":
    main()
