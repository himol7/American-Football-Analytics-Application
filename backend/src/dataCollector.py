#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 19:13:07 2020

@author: himol7
"""

import pandas as pd

class dataCollector:
    
    def readfile(self):
        data = pd.read_csv('20191130 NCST K vs NCUN 31 PLAYS K.KR.P.PR.FG.FGB.csv')
        return data

    
