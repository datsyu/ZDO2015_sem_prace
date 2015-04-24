#! /usr/bin/python
# -*- coding: utf-8 -*-

import csv
"""
    Kostra k druhe casti semestralni práce na predmet ZDO.

    Vystupem bude CSV soubor s nasledujicimi informacemi : 
       frameId, cellId, x, y, v_x, v_y
    
    V případě, že rychlosti v_x a v_y nebudou znamy (frame, na kterem se bunka objevila), pouzijte 0.

    Nemente nazev souboru, ani nazvy funkci. 
    
"""


class Tracker:
    """
        Trida pro trackovani bunek
        
    """

    def __init__(self):
        """
            Kontruktor tridy
        """
        self.data = []
        self.frameId = 0
        # self.predchozi = None
        # Zde je prostor pro inicializace
                 
    def track_in_frame(self, frame):
        """
            Tracking v novem framu            
        """
        # Uložení framu pro zpracování v příštím zavolání 
        # self.predchozi = frame
        self.frameId += 1

        # tady čekám spoustu vašeho kódu


        # Ukázka zápisu vypočítu polohy a rychlosti
        # self.data.append({
        #     'frameId': self.frameId,
        #     'cellId': 21,
        #     'x': 15,
        #     'y': 22,
        #     'v_x': 12.0,
        #     'v_y': -12.2
        #     })




    def getData():
        # Zde může být nějaká závěrečná analýza

        return self.data

    def saveCsvFile(self):
        csvfile = open("track.csv","wb")
        csvwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow(["frameId", "cellId", "x", "y", "v_x", "v_y"])
        for item in self.data:
            csvwriter.writerow([
                str(item['frameId']),
                str(item['cellId']), 
                str(item['x']), 
                str(item['y']), 
                str(item['v_x']), 
                str(item['v_y'])])
        csvfile.close()
