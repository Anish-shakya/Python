
class DataPipeline:
    def __init__(self,extractor,loader):
        self.extractor = extractor
        self.loader = loader

    def run(self):
        all_data=[]
        
        
        for extractor in self.extractor:
            data = extractor.extract()
            all_data.extend(data)
        
        self.loader.load(all_data)