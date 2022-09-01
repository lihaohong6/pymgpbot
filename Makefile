.PHONY : build clean
build:
	pyinstaller pwb.py --noconfirm
	cp user-config.py dist/pwb
	mkdir -p dist/pwb/pywikibot/families

clean:
	rm -r build dist __pycache__
