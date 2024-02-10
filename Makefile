all: zigen_data rust_all
rust_all: zigen_data
	cargo build
lint:
	cargo clippy

target/debug/%: lists/wordslist.csv
	cargo build --bins --no-default-features

zigen_data: lists/english_variants.json

lists/wordslist.csv:
	cd lists && curl -O https://words.hk/faiman/analysis/wordslist.csv

lists/%.json: lists/varcon.txt.bz2 target/debug/zigen
	# Funny enough make's basename doesn't strip away the directory...
	./target/debug/zigen generate_$(shell basename $@ .json) $< $@
	# Ensure .gitignore has the file
	grep -q $@ .gitignore || echo '/$@' >> .gitignore

clean:
	cd lists && git clean -f -x -d

release:
	cargo build --release
