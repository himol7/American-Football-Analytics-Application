from dataCollector import dataCollector
import pandas
import pytest

data_collector = dataCollector()


def test_method():
  data = data_collector.readfile('https://github.com/himol7/American-Football-Analytics-Application/blob/KrisshaJ-Testing/backend/src/NCSU.csv')
  print("DATA",data)
  assert data is not None
