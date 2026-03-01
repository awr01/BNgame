SOURCES = Nate.py
EXEC		= $(patsubst %.py,build/%.exe,${SOURCES})


default: requirements.txt ${EXEC}

${EXEC}: build/%.exe : %.py
	# pip install pyinstaller
	# pyinstaller --windowed --onefile --distpath=build --paths=. --add-data "audio.mp3;." --add-data "./img2;img2" --add-data "./imgs;imgs"	$?
	# -i ../OSM-logo.ico
	
	python -m nuitka --onefile --enable-plugin=tk-inter --enable-plugin=no-qt --windows-console-mode=disable --include-data-file=audio.mp3=audio.mp3 --include-data-dir=img2=img2 --include-data-dir=imgs=imgs --output-dir="build" $?

	
requirements.txt :
#	pip install --no-deps pipreqs
#	pipreqs .
	pip freeze . > requirements.txt