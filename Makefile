# targets that aren't filenames
.PHONY: all clean deploy build serve

all: build

BIBBLE = bibble

_includes/pubs.html: bib/pubs.bib bib/publications.tmpl
	git submodule init; git submodule update
	chmod +x bibble/bibble/main.py
	mkdir -p _includes
	$(PYTHON) bibble/bibble/main.py $+ > $@

build: _includes/pubs.html
	jekyll build --trace

# you can configure these at the shell, e.g.:
# SERVE_PORT=5001 make serve
SERVE_HOST ?= 127.0.0.1
SERVE_PORT ?= 5000

serve: _includes/pubs.html
	jekyll serve --port $(SERVE_PORT) --host $(SERVE_HOST)

clean:
	$(RM) -r _site _includes/pubs.html

#DEPLOY_HOST ?= yourwebpage.com
#DEPLOY_PATH ?= www/
#RSYNC := rsync --compress --recursive --checksum --itemize-changes --delete -e ssh

deploy: clean _includes/pubs.html
	jekyll build #--base '/group/rexlab' #Why doesn't this work?
	#$(RSYNC) _site/ $(DEPLOY_HOST):$(DEPLOY_PATH)
