## Bureau of Transportation Statistics (BTS) Webscraper

Date: 17 May 2023
<br>Author: @bendlev (Ben Levesque)
<br>Institution: Dartmouth College

### Startup

The `.venv` folder contains the Python virtual environment (known as a "venv") needed to run `scrape.py` and `clean.ipynb`. This webscraper primarily relies on the *selenium* and *pandas* Python packages. You cannot run these files without first setting up the venv.

Depending on your Integrated Development Environment (IDE), you may need to select the path the interpreter manually.

For myself, I use VS Code and I am on Windows. I entered the path to the Python interpreter manually as such:
```
bts_webscraper\.venv\Scripts\python.exe
```
After selecting the Python interpreter manually, VS Code was able to recognize the `.venv` and my import statements were valid (my IDE shows me when an import is successful, this may not be the case for other IDEs, i.e. Vim, Emacs, Jupyter...). If you cannot tell whether your imports were successful, running the file should tell you (it should say "could not find specified module selenium", or something similar).

### Structure

*scrape.py* - Uses a selenium webdriver to open the Bureau of Transporation Statistics website, and navigate through panes to download desired files.

- The scraper is focused on airline delay data for six major airlines. This scraper is only used to exactly replicate the data used in ths module.

*clean.ipnyb* - Uses pandas to clean data after it has been received and stored by *scrape.py*.