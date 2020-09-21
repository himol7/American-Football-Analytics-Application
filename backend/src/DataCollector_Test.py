from dataCollector import dataCollector
import pandas
import pytest

data_collector = dataCollector()


def test_method():
  x = data_collector.readfile('American-Football-Analytics-Application/backend/src/NCSU.csv')
  print (x)
//  assert data_collector.readfile('American-Football-Analytics-Application/backend/src/NCSU.csv') is not None
