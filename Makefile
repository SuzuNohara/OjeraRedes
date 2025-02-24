# Makefile

.PHONY: all run clean install

all: run

serve:
	python3 practicas/ServerManager.py

client:
	python3 practicas/client.py

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +

install:
	pip install -r requirements.txt


blocking-connection-server:
	python3 programs/blocking-connection/blocking-connection-server.py

blocking-connection-client:
	python3 programs/blocking-connection/blocking-connection-client.py