#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 13:47:15 2020

@author: himol7
"""


class photoCoordinates:
    
    allCoordinates = {}
    
    kickoff_coordinates = {
        "R1" : (20, 140),
        "R2" : (65, 140),
        "R3" : (110, 140),
        "R4" : (155, 140),
        "R5" : (200, 140),
        "PK" : (245, 140),
        "L5" : (290, 140),
        "L4" : (335, 140),
        "L3" : (380, 140),
        "L2" : (425, 140),
        "L1" : (470, 140)
        }
    
    kickoff_return_coordinates = {
        
        }
    
    punt_coordinates = {}
        
    punt_return_coordinates = {
        "VRo" : (0, 0),
        "VRi" : (0, 0),
        "PDR1" : (0, 0)
        }
    
    fieldgoal_coordinates = {}
    
    fieldgoal_block_coordinates = {}
    
    def __init__(self):
        self.allCoordinates['KICKOFF'] = self.kickoff_coordinates
        self.allCoordinates['KICKOFF_RETURN'] = self.kickoff_return_coordinates
        self.allCoordinates['PUNT'] = self.punt_coordinates
        self.allCoordinates['PUNT_RETURN'] = self.punt_return_coordinates
        self.allCoordinates['FIELDGOAL'] = self.fieldgoal_coordinates
<<<<<<< HEAD
        self.allCoordinates['FIELDGOAL_BLOCK'] = self.fieldgoal_block_coordinates
        
=======
        self.allCoordinates['FIELDGOAL_BLOCK'] = self.fieldgoal_block_coordinates
>>>>>>> 2ca6e4f726f10e81794c6b55299d20457eb0884f
