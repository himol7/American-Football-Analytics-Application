language: python
python: "3.6"
install:
    - pip install -r requirements.txt
script:
    - pytest dataCollector_Test.py
    - pytest dataSeparatorTest.py
    - pytest dataAnalyticsTest.py
