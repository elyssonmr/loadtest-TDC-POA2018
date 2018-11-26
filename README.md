# loadtest-TDC-POA2018


MAX_TIME=2000 locust --no-web --print-stats --logfile=logfile.txt -c 500 -r 50 -t 1m -L debug -H http://localhost:8000 -f locustfile.py
