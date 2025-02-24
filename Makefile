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

blocking-serialization-server:
	python3 programs/serialization/blocking-connection-serial-server.py

blocking-serialization-client:
	python3 programs/serialization/blocking-connection-serial-client.py

not-connection-blocking-server:
	python3 programs/not-connection-blocking/not-connection-blocking-server.py

not-connection-blocking-client:
	python3 programs/not-connection-blocking/not-connection-blocking-client.py

threads-server:
	python3 programs/threads/multithreads-server.py

threads-client:
	python3 programs/threads/multithreads-client.py