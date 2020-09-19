from dataCollector import dataCollector
import pandas
class dataCollectorTest:
  def test01(self):
    dc = dataCollector()
    data = dc.readfile()
    if data.shape[0] != 0:
      #Checks if file is empty
      return ("True")
    return("False")

# print(test01())
