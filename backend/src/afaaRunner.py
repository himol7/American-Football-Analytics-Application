#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 19:36:42 2020

@author: himol7
"""

from dataCollector import dataCollector
from playsSeperator import playsSeperator
from dataAnalytics import dataAnalytics
from photoImposer import photoImposer
import pandas as pd

class afaaRunner:
    
    def  __init__(self, inputFile, downloadPath):
        dc = dataCollector()
        ps = playsSeperator()
        da = dataAnalytics()
        pi = photoImposer()
        
        team = "NCST"
        print("download path = ")
        print(downloadPath)
        if(len(inputFile) == 1):
            data = dc.readfile(inputFile[0])
        else:
            data=dc.readfile(inputFile[0])
            for i in range(1,len(inputFile)):
                df2=dc.readfile(inputFile[i])
                data=pd.concat([data,df2])
        print(data)
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
            pi.imposeDataOnImage(playType, countsAndRatings, downloadPath)
