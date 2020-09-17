#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 23:02:35 2020

@author: himol7
"""


import pandas as pd
from PIL import Image, ImageFont, ImageDraw

data = pd.read_csv('20191130 NCST K vs NCUN 31 PLAYS K.KR.P.PR.FG.FGB.csv')

team = "NCST"

plays = {"KICKOFF", "PUNT", "FIELDGOAL"}

p = data[(data["pff_SPECIALTEAMSTYPE"] == "PUNT") & (data["pff_OFFTEAM"] == team)]
kor = data[(data["pff_SPECIALTEAMSTYPE"] == "KICKOFF") & (data["pff_OFFTEAM"] == team)]

pr = data[(data["pff_SPECIALTEAMSTYPE"] == "PUNT") & (data["pff_DEFTEAM"] == team)]
ko = data[(data["pff_SPECIALTEAMSTYPE"] == "KICKOFF") & (data["pff_DEFTEAM"] == team)]

epfg = data[(data["pff_SPECIALTEAMSTYPE"] == "EXTRA POINT") | (data["pff_SPECIALTEAMSTYPE"] == "FIELD GOAL")]
fg = epfg[epfg["pff_OFFTEAM"] == team]
fgb = epfg[epfg["pff_DEFTEAM"] == team]

#plays = ko["pff_DEFPLAYERS"]
plays = p["pff_OFFPLAYERS"]


df = pd.DataFrame(columns = ['POSITION', 'PLAYER', 'COUNT'])
for play in plays:
    play = play.replace('NCST ', '').replace('(', '').replace(')', '')
    for player in play.split('; '):
        player_no, player_position = player.split(' ')
        new_player = {"POSITION": player_position, "PLAYER": player_no, "COUNT": 1}
        df = df.append(new_player, ignore_index = True)
        position_player_total = df.groupby(['POSITION', 'PLAYER'], as_index=False).sum()
        

def coordinatesDictionaryGenerator():
    dict = {}
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
    
    punt_coordinates = {
        "GL": (40, 100),
        "PLW": (0, 0),
        "PLT": (0, 0),
        "PLG": (0, 0),
        "PLS": (0, 0),
        "PRG": (0, 0),
        "PRT": (0, 0),
        "PRW": (0, 0),
        "PC": (0, 0),
        "PPR": (0, 0),
        "PPL": (0,0),
        "PPLi": (0,0),
        "PPLo": (0,0),
        "P": (0, 0),
        "GR": (0, 0)
        }
    
    fieldgoal_coordinates = {}
    
    dict = {"KICKOFF" : kickoff_coordinates, "PUNT": punt_coordinates, "FIELDGOAL" : fieldgoal_coordinates}
    
    return dict

def imagesDictionaryGenerator():
    dict = {}
    
    kickoff_image = "kickoff_coverage.png"
    punt_image = "punt_coverage.png"
    fieldgoal_image = "fieldgoal_coverage.png"
    
    dict = {"KICKOFF": kickoff_image, "PUNT" : punt_image, "FIELDGOAL" : fieldgoal_image}
    
    return dict
    

image = Image.open(imagesDictionaryGenerator().get("PUNT"))
font = ImageFont.truetype('arial_bold.ttf', size=10)
draw = ImageDraw.Draw(image)

for position, positional_group in position_player_total.groupby(['POSITION']):
    coordinates = coordinatesDictionaryGenerator().get("PUNT")
    #print(position)
    (x, y) = coordinates.get(position)
    message = ''
    for index, player in positional_group.iterrows():
        message = message + str(player["PLAYER"]) + " " + str(player["COUNT"]) + '\n'
    color = 'rgb(0, 0, 0)'
    draw.text((x, y), message, fill=color, font=font)
image.save('output/punt.png')