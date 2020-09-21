from dataCollector import dataCollector
import pandas
import pytest

data_collector = dataCollector()


def test_method():
  assert data_collector.readfile("20191130 NCST K vs NCUN 31 PLAYS K.KR.P.PR.FG.FGB.csv") is not None
