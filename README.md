# Versions
1. python 3.11.1
1. mutagen 1.46.0
1. pyinstaller 6.1.0
```
pip install mutagen==1.46.0 pyinstaller==6.1.0
```

# Choose your language in settings.json file
Available languages:  
1. Polish - PL  
1. English - EN  

# How to use
1. Create folder with 
    1. tracklist.txt file
    1. cover image (.jpg, .jpeg or .png)
    1. music files (.mp3 or .flac)
  
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
    pyinstaller -F "path/to/file.py"

#### Optional with icon, title and without console
    pyinstaller -F "path/to/file.py" --icon="path/to/icon.png" --noconsole -n "AppName"