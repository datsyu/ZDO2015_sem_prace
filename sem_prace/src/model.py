#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
    Kostra k prvni casti semestralni práce na predmet ZDO.
    
    Nemente nazev souboru, ani nazvy funkci. 
    
"""
import numpy as np
import skimage.filter

class BackgroundModel:
    """
        Trida pro vypocet modelu pozadi
        
    """

    def __init__(self):
        """
            Kontruktor tridy
        """
        self.frames = []
        self.model = []
        
    def add_frame(self, frame):
        """
            Prida frame do kolekce pro vypočet modelu pozadi.

            :param frame: Jeden frame z nacteného videa
            :type frame: numpy matice M x N

        """
        # primitivní způsob stanovení modelu, určitě vymyslíte něco lepšího
        if len(self.frames) < 51:
            self.frames.append(frame)
        self.model = self.frames[0]*0.0
        for pic in self.frames:
            self.model += pic*1.0
        self.model /= len(self.frames)
        self.model = np.array(self.model, dtype = np.uint8)
    def get_model(self):
        """
            Vypocíta model pozadi a vrati ho    
            
            :returns: numpy matice M x N
        """
        # zde bude váš kód pro výpočet modelu - průměr
        return self.model
