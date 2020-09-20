from playsSeperator import playsSeperator
from dataCollector import dataCollector

dc = dataCollector()
data = dc.readfile()
ps = playsSeperator()
plays = ps.getDataframesByPlays("NCST", data)

def test02():
  for k, v in plays.items():
    assert v is not None