from dataCollector import dataCollector
import pandas
import pytest

dc = dataCollector()


def test_method():
  assert dc.readfile() is not None
