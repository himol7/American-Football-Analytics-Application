#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 19:13:07 2020

@author: himol7
"""

import pandas as pd

class dataCollector:
    
    def readfile(self, fileName):
        data = pd.read_csv(fileName, error_bad_lines = False)
        return data
