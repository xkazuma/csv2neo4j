define Usage
	@echo "--- usage ---"
	@echo "make {all | generate | import | shell | clean}"
	@echo "  make all"
	@echo "  make dblist"
	@echo "  make generate"
	@echo "  make import delim=<character with quote characters> neo4j_dirpath=<path to a directory of neo4j data> gdb_name=<dbname>"
	@echo "  make shell neo4j_dirpath=<neo4j's path> gdb_name=<dbname>"
	@echo "  make clean neo4j_dirpath=<path to a directory of neo4j data> gdb_name=<dbname>"
	@exit 1
endef

NEO4jDIRPATH := ~/src/neo4j-community-3.4.7
all:
	$(call Usage)


python := `which python3.6` # path to python3
generate:
	rm -rf resource/neo4j/*.csv
	cd src/ && $(python) generate_neo4j_csv.py

neo4j_dirpath := $NEO4jDIRPATH
gdb_name      := NULL
delim         := NULL
nodes         := $(shell ls resource/neo4j/node_*.csv)
rels          := $(shell ls resource/neo4j/rel_*.csv)
import:
ifeq (NULL, $(neo4j_dirpath))
	@echo invalid neo4j_dirpath
	$(call Usage)
endif
ifeq (NULL, $(gdb_name))
	@echo invalid gdb_name
	$(call Usage)
endif
ifeq (NULL, $(delim))
	@echo invalid delim
	$(call Usage)
endif
	$(foreach node, $(nodes), $(eval cl_node := $(cl_node) --nodes $(node)))
	$(foreach rel,  $(rels),  $(eval cl_rel  := $(cl_rel) --relationships $(rel)))
	neo4j-admin import --mode csv \
	                   --database $(gdb_name).db \
	                   --delimiter=$(delim) \
	                   $(cl_node) $(cl_rel) 

neo4j_dirpath := $(NEO4jDIRPATH)

dblist:
ifeq (NULL, $(neo4j_dirpath))
	$(call Usage)
endif
	ls -l $(neo4j_dirpath)/data/databases/

neo4j_dirpath := $(NEO4jDIRPATH)
gdb_name      := NULL
shell:
ifeq (NULL, $(neo4j_dirpath))
	$(call Usage)
endif
ifeq (NULL, $(gdb_name))
	$(call Usage)
endif
	neo4j-shell --path $(neo4j_dirpath)/data/databases/$(gdb_name).db

neo4j_dirpath := $(NEO4jDIRPATH)
gdb_name      := NULL
clean:
ifeq (NULL, $(gdb_name))
	$(call Usage)
endif
ifeq (NULL, $(neo4j_dirpath))
	$(call Usage)
endif
	rm -r $(neo4j_dirpath)/data/databases/$(gdb_name).db
