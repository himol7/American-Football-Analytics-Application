#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 19:45:41 2020

@author: himol7
"""

class playsSeperator:
    
    def getDataframesByPlays(self, team, data):
        p = data[(data["pff_SPECIALTEAMSTYPE"] == "PUNT") & (data["pff_OFFTEAM"] == team)]
        kor = data[(data["pff_SPECIALTEAMSTYPE"] == "KICKOFF") & (data["pff_OFFTEAM"] == team)]
        
        pr = data[(data["pff_SPECIALTEAMSTYPE"] == "PUNT") & (data["pff_DEFTEAM"] == team)]
        ko = data[(data["pff_SPECIALTEAMSTYPE"] == "KICKOFF") & (data["pff_DEFTEAM"] == team)]
        
        epfg = data[(data["pff_SPECIALTEAMSTYPE"] == "EXTRA POINT") | (data["pff_SPECIALTEAMSTYPE"] == "FIELD GOAL")]
        fg = epfg[epfg["pff_OFFTEAM"] == team]
        fgb = epfg[epfg["pff_DEFTEAM"] == team]
        
        dict = {"PUNT" : p,
                "KICKOFF_RETURN" : kor,
                "PUNT_RETURN" : pr,
                "KICKOFF" : ko,
                "FIELDGOAL" : fg,
                "FIELDGOAL_BLOCK" : fgb}
        
        return dict