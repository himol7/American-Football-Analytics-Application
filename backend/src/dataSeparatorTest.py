from playsSeperator import playsSeperator
from dataCollector import dataCollector

data_collector = dataCollector()
data = data_collector.readfile()
play_separator = playsSeperator()
plays = play_separator.getDataframesByPlays("NCST", data)

def test02():
  for k, v in plays.items():
    assert v is not None
