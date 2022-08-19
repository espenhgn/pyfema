import numpy as np

class FEMA(object):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def fit_model(self):
        raise NotImplementedError