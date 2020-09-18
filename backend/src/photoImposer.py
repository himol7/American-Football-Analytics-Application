#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 13:46:38 2020

@author: himol7
"""

from photoCoordinates import photoCoordinates
from PIL import Image, ImageFont, ImageDraw

class photoImposer:
    
    pc = photoCoordinates()
    allCoordinates = pc.allCoordinates
    
    all_images = {}
    
    def __init__(self):
        self.all_images['KICKOFF'] = "kickoff_coverage.png"
        self.all_images['KICKOFF_RETURN'] = "kickoff_return.png"
        self.all_images['PUNT'] = "punt_coverage.png"
        self.all_images['PUNT_RETURN'] = "punt_return.png"
        self.all_images['FIELDGOAL'] = "fieldgoal_coverage.png"
        self.all_images['FIELDGOAL_BLOCK'] = "fieldgoal_block.png"
    
    def imposeDataOnImage(self, playType, countsAndRatingsData):
        
        coordinates = self.allCoordinates.get(playType)
        print(coordinates)
        
        image = Image.open(self.all_images.get(playType))
        font = ImageFont.truetype('arial_bold.ttf', size=10)
        draw = ImageDraw.Draw(image)
        
        for position, positional_group in countsAndRatingsData.groupby(['POSITION']):
            (x, y) = coordinates.get(position)
            message = ''
            for index, player in positional_group.iterrows():
                message = message + str(player["PLAYER"]) + " " + str(player["COUNT"]) + " " + str(player["RATING"]) + '\n'
            color = 'rgb(0, 0, 0)'
            draw.text((x, y), message, fill=color, font=font)
        
        imagename = playType + '_ANALYSIS.png'
        image.save(imagename)
