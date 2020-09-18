#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 19:36:42 2020

@author: himol7
"""

from dataCollector import dataCollector 
from playsSeperator import playsSeperator

class afaaRunner:
    
    def  __init__(self):
        dc = dataCollector()
        ps = playsSeperator()
        
        team = "NCST"
        data = dc.readfile()    
        
        print(data.head())
        
        all_plays = ps.getDataframesByPlays(team, data)
        print(all_plays)
        
        
    

a = afaaRunner()