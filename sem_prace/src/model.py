#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
    Kostra k prvni casti semestralni práce na predmet ZDO.
    
    Nemente nazev souboru, ani nazvy funkci. 
    
"""


class BackgroundModel:
    """
        Trida pro vypocet modelu pozadi
        
    """

    def __init__(self):
        """
            Kontruktor tridy
        """
        self.model = None
        
    def add_frame(self, frame):
        """
            Prida frame do kolekce pro vypočet modelu pozadi.

            :param frame: Jeden frame z nacteného videa
            :type frame: numpy matice M x N

        """
        # primitivní způsob stanovení modelu, určitě vymyslíte něco lepšího
        self.model = frame
            
    def get_model(self):
        """
            Vypocíta model pozadi a vrati ho    
            
            :returns: numpy matice M x N
        """
        # zde bude váš kód pro výpočet modelu
        return self.model

