from dataCollector import dataCollector
import pandas
import pytest

data_collector = dataCollector()


def test_method():
  y = "https://github.com/himol7/American-Football-Analytics-Application/blob/KrisshaJ-Testing/backend/src/NCSU.csv"
  x = data_collector.readfile(y)
  print (x)
#  assert data_collector.readfile('American-Football-Analytics-Application/backend/src/NCSU.csv') is not None
