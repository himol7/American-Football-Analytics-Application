#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 19:36:42 2020

@author: himol7
"""

from src.dataCollector import dataCollector
from src.playsSeperator import playsSeperator
from src.dataAnalytics import dataAnalytics
from src.photoImposer import photoImposer

class afaaRunner:
    
    def  __init__(self, inputFile):
        dc = dataCollector()
        ps = playsSeperator()
        da = dataAnalytics()
        pi = photoImposer()
        
        team = "NCST"
        data = dc.readfile(inputFile)
        
        all_plays = ps.getDataframesByPlays(team, data)
        
        offensive_plays = {"PUNT", "KICKOFF_RETURN", "FIELDGOAL"}
        defensive_plays = {"PUNT_RETURN", "KICKOFF", "FIELDGOAL_BLOCK"}
        
        for playType, playData in all_plays.items():
        
            if playType in offensive_plays:
                formations = playData["pff_OFFPLAYERS"]
                ratings = playData["pff_OFFPLAYERSRATINGS"]
                
            elif playType in defensive_plays:
                formations = playData["pff_DEFPLAYERS"]
                ratings = playData["pff_DEFPLAYERSRATINGS"]
                
            countsAndRatings = da.generateTotalCountsAndRatings(formations, ratings)
            pi.imposeDataOnImage(playType, countsAndRatings)            
