from dataCollectorTest import dataCollectorTest
from dataSeparatorTest import dataSeparatorTest
from dataAnalyticsTest import dataAnalyticsTest
import pytest
import pandas

dc = dataCollectorTest()
print("Data collector test: \n", dc.test01())

ds = dataSeparatorTest()
print("Data separator test: \n", ds.test02())

da = dataAnalyticsTest()
print("Data analytics test: \n", da.test03())