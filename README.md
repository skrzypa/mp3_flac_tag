# Versions
1. python 3.11.1
1. mutagen 1.46.0
1. PyQt6 6.5.2
1. pyinstaller 5.7.0
```
pip install mutagen==1.46.0 PyQt6==6.5.2 pyinstaller==5.7.0
```

# Choose your language in settings.json file
Available languages:  
1. Polish - PL  
1. English - EN  

# How to use
1. Create folder with 
    1. tracklist.txt file
    1. cover image in .jpg, .jpeg or .png 
    1. music files
  
1. The tracklist file must look like this
    ```
    artist name
    album title
    release year
    genre
    song title
    song title
    ...
    ```

# If you want add your language
Translate languages.json like this on each row
```
"Wybierz plik z tracklistą","Select a tracklist file","<text in your language>"
```

Add code in paths_settings.py
```
langs = {"PL": 0,
        "EN": 1,
        "<code>": 2}
```

Change code in settings.json
```
{
    "language": "<code>"
}
```

# Create .exe file with pyinstaller
1. Comment line in paths_settings.py
```
PATH: str = str(pathlib.Path(sys.executable).parent)
# PATH: str = str(pathlib.Path(pathlib.Path(__file__).parent)) # Comment out this line when converting to exe
```
2. In terminal
```
pyinstaller "path/to/main.py" -F --icon="path/to/icon.png" --noconsole
```