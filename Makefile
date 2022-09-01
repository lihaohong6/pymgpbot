.PHONY : build
build:
	pyinstaller pwb.py --noconfirm
	cp user-config.py dist/pwb
	mkdir -p dist/pwb/pywikibot/families
