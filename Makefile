test:
	pip install -r requirements.txt
	python3 -m unittest redis_tests.py
