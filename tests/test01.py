from dataCollector import dataCollector

data_collector = dataCollector()

def test_method():
  data = pd.read_csv("https://github.com/himol7/American-Football-Analytics-Application/blob/KrisshaJ-Testing/backend/src/NCSU.csv", engine = 'python')
  print(data)
  
  
