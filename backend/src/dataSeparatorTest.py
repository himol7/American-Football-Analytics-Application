from playsSeperator import playsSeperator
from dataCollector import dataCollector
class dataSeparatorTest:
  def test02(self):
    dc = dataCollector()
    data = dc.readfile()
    ps = playsSeperator()
    plays = ps.getDataframesByPlays("NCST", data)
    for k,v in plays.items():
      if v is not None:
        return("True")
      else:
        return("False")

# print(test02())
