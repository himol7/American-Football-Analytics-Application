#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 13:46:38 2020

@author: himol7
"""

<<<<<<< HEAD
from src.photoCoordinates import photoCoordinates
=======
from photoCoordinates import photoCoordinates
>>>>>>> 2ca6e4f726f10e81794c6b55299d20457eb0884f
from PIL import Image, ImageFont, ImageDraw

class photoImposer:

    pc = photoCoordinates()
    allCoordinates = pc.allCoordinates
    all_images = {}
    
    def __init__(self):
<<<<<<< HEAD
        self.all_images['KICKOFF'] = "src/formationImages/kickoff_coverage.png"
        self.all_images['KICKOFF_RETURN'] = "src/formationImages/kickoff_return.png"
        self.all_images['PUNT'] = "src/formationImages/punt_coverage.png"
        self.all_images['PUNT_RETURN'] = "src/formationImages/punt_return.png"
        self.all_images['FIELDGOAL'] = "src/formationImages/fieldgoal_coverage.png"
        self.all_images['FIELDGOAL_BLOCK'] = "src/formationImages/fieldgoal_block.png"
=======
        self.all_images['KICKOFF'] = "formationImages/kickoff_coverage.png"
        self.all_images['KICKOFF_RETURN'] = "formationImages/kickoff_return.png"
        self.all_images['PUNT'] = "formationImages/punt_coverage.png"
        self.all_images['PUNT_RETURN'] = "formationImages/punt_return.png"
        self.all_images['FIELDGOAL'] = "formationImages/fieldgoal_coverage.png"
        self.all_images['FIELDGOAL_BLOCK'] = "formationImages/fieldgoal_block.png"
>>>>>>> 2ca6e4f726f10e81794c6b55299d20457eb0884f
    
    def imposeDataOnImage(self, playType, countsAndRatingsData, downloadPath):
        coordinates = self.allCoordinates.get(playType)
        
        image = Image.open(self.all_images.get(playType))
<<<<<<< HEAD
        font = ImageFont.truetype('src/arial_bold.ttf', size=10)
=======
        font = ImageFont.truetype('arial_bold.ttf', size=10)
>>>>>>> 2ca6e4f726f10e81794c6b55299d20457eb0884f
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
        
<<<<<<< HEAD
        imagename = downloadPath + '/' + playType + '_ANALYSIS.png'
=======
        imagename = './' + downloadPath + '/' + playType + '_ANALYSIS.png'
        print("Image name = ")
        print(imagename)
>>>>>>> 2ca6e4f726f10e81794c6b55299d20457eb0884f
        image.save(imagename)
