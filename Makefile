python := # path to python3
all:
	cd src/
	$(python) generate_neo4j_csv.py
	