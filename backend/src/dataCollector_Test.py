from dataCollector import dataCollector
import pandas
import pytest

data_collector = dataCollector()


def test_method():
  assert data_collector.readfile('backendinput_files20191130_NCST_K_vs_NCUN_31_PLAYS_K.KR.P.PR.FG.FGB.csv') is not None
