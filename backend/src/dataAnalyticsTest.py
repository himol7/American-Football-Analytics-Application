from dataAnalytics import dataAnalytics
from playsSeperator import playsSeperator
from dataCollector import dataCollector


import warnings
import pytest
warnings.simplefilter(action='ignore', category=FutureWarning)


da = dataAnalytics()
dc = dataCollector()
data = dc.readfile()
ps = playsSeperator()
all_plays = ps.getDataframesByPlays("NCST", data)
offensive_plays = {"PUNT", "KICKOFF_RETURN", "FIELDGOAL"}
defensive_plays = {"PUNT_RETURN", "KICKOFF", "FIELDGOAL_BLOCK"}


def test03():

  for playType, playData in all_plays.items():

    if playType in offensive_plays:
      formations = playData["pff_OFFPLAYERS"]
      ratings = playData["pff_OFFPLAYERSRATINGS"]

    elif playType in defensive_plays:
      formations = playData["pff_DEFPLAYERS"]
      ratings = playData["pff_DEFPLAYERSRATINGS"]

    countsAndRatings = da.generateTotalCountsAndRatings(formations, ratings)

    assert countsAndRatings is not None

