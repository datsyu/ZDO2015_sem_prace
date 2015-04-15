#! /usr/bin/python
# -*- coding: utf-8 -*-

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
	self.data
        pass
                 
    def track_in_frame(self, frame):
        """
            Tracking v novem framu            
        """

        pass

    def getData():
        return self.data

    def saveCsvFile(self):
        csvfile = open("track.csv","wb")
        csvwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow(["frameId, cellId, x, y, v_x, v_y"])
        for item in self.data:
	    csvwriter.writerow([item['frameId'], item['cellId'], item['x'], item['y'], item['v_x'], item['v_y']])
	csvfile.close()
