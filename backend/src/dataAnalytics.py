#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 00:48:45 2020

@author: himol7
"""

import pandas as pd

class dataAnalytics:
        
    def generateTotalCountsAndRatings(self, formations, ratings):
        df = pd.DataFrame(columns = ['POSITION', 'PLAYER', 'COUNT', 'RATING'])
        
        for i in range(len(formations)):
            formation = formations.iloc[i]
            rating = ratings.iloc[i]
            
            formation = formation.replace('NCST ', '').replace('(', '').replace(')', '')
            rating = rating.replace('NCST ', '').replace('(', '').replace(')', '')
            
            player_positions = formation.split('; ')
            player_ratings = rating.split('; ')
            
            for j in range(len(player_positions)):
                player_position = player_positions[j]
                player_rating = player_ratings[j]
                
                player, position = player_position.split(' ')
                player, rating = player_rating.split(' ')
                
                new_player = {"POSITION": position, "PLAYER": player, "COUNT": int(1), "RATING": float(rating)}
                df = df.append(new_player, ignore_index = True)
                
        df["COUNT"] = df["COUNT"].astype('int')
        playerPositionCountsRatings = df.groupby(['POSITION', 'PLAYER'], as_index=False)['COUNT', 'RATING'].sum()        
        return playerPositionCountsRatings
