from dataCollector import dataCollector
import pandas
import pytest

data_collector = dataCollector()


def test_method():
  assert data_collector.readfile('American-Football-Analytics-Application/backend/src/NCSU.csv') is not None
