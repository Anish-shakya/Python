from abc import ABC, abstractmethod

class BaseExtractor(ABC):
    
    def __init__(self,client_id):
        self.client_id = client_id
    
    
    @abstractmethod
    def extract(self):
        pass