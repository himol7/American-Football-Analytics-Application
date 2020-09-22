from dataCollector import dataCollector
import pandas
import pytest

data_collector = dataCollector()


def test_method():
  assert data_collector.readfile('https://github.com/himol7/American-Football-Analytics-Application/blob/KrisshaJ-Testing/backend/src/NCSU.csv?raw=true') is not None
