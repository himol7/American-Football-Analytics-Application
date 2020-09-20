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
        self.all_images['KICKOFF'] = "formationImages/kickoff_coverage.png"
        self.all_images['KICKOFF_RETURN'] = "formationImages/kickoff_return.png"
        self.all_images['PUNT'] = "formationImages/punt_coverage.png"
        self.all_images['PUNT_RETURN'] = "formationImages/punt_return.png"
        self.all_images['FIELDGOAL'] = "formationImages/fieldgoal_coverage.png"
        self.all_images['FIELDGOAL_BLOCK'] = "formationImages/fieldgoal_block.png"
    
    def imposeDataOnImage(self, playType, countsAndRatingsData, downloadPath):
        coordinates = self.allCoordinates.get(playType)
        
        image = Image.open(self.all_images.get(playType))
        font = ImageFont.truetype('arial_bold.ttf', size=10)
        draw = ImageDraw.Draw(image)
        
        for position, positional_group in countsAndRatingsData.groupby(['POSITION']):
            (x, y) = (0, 0)
            if position in coordinates:
                (x, y) = coordinates.get(position)
            message = ''
            for index, player in positional_group.iterrows():
                message = message + str(player["PLAYER"]) + " " + str(player["COUNT"]) + " " + str(player["RATING"]) + '\n'
            color = 'rgb(0, 0, 0)'
            draw.text((x, y), message, fill=color, font=font)
        
        imagename = './' + downloadPath + '/' + playType + '_ANALYSIS.png'
        print("Image name = ")
        print(imagename)
        image.save(imagename)
