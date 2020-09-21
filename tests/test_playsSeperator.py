from playsSeperator import playsSeperator
from dataCollector import dataCollector

data_collector = dataCollector()
data = data_collector.readfile("https://github.com/himol7/American-Football-Analytics-Application/blob/KrisshaJ-Testing/backend/src/NCSU.csv")
play_separator = playsSeperator()
plays = play_separator.getDataframesByPlays("NCST", data)

def test02():
  for k, v in plays.items():
    assert v is not None
