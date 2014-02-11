# i18n-extract

> a simple Python script to parse usage of [Polyglot](https://github.com/airbnb/polyglot.js)

## Usage 

- First copy and paste the python script into your folder (or add as submodule)
- Then execute the script without forgetting to set
    - `-t` is the directory where your templates file are stored
    - `-l` is the directory where your translates file re stored

By default, these are files with the extension ".jade" that are sought. 
You can pass an optional parameter to specify the type of extension to be treated (.html, .hbs, ...)
To do this, write the same command with the "-e" option and the extension to be addressed preceded by a dot.

        
### Example

```python
#For treated templates with default extention .jade
./i18n_extract.py -t templates/ -l locales/

#For treated templates with extention .html
./i18n_extract.py -t templates/ -l locales/ -e ".html"
```

### Result

    4 index were found in /i18n-extract/templates/sidebar.jade
    ['hello', 'sidebar', 'content', 'help']

    1 index were found in /i18n-extract/templates/test.jade
    ['welcome']

    Processing /Library/WebServer/Documents/i18n-extract/locales/en.json file:
    ['Test'] as been deleted from the /i18n-extract/locales/en.json
    ['content'] as been added from the file /i18n-extract/locales/en.json
    ['sidebar'] as been added from the file /i18n-extract/locales/en.json
    ['hello'] as been added from the file /i18n-extract/locales/en.json
    ['welcome'] as been added from the file /i18n-extract/locales/en.json
    ['help'] as been added from the file /i18n-extract/locales/en.json
    Translation file is updated

    Processing /Library/WebServer/Documents/i18n-extract/locales/fr.json file:
    ['Test'] as been deleted from the file /i18n-extract/locales/fr.json
    ['content'] as been added from the file /i18n-extract/locales/fr.json
    ['sidebar'] as been added from the file /i18n-extract/locales/fr.json
    ['hello'] as been added from the file /i18n-extract/locales/fr.json
    ['welcome'] as been added from the file /i18n-extract/locales/fr.json
    ['help'] as been added from the file /i18n-extract/locales/fr.json
    Translation file is updated

---

## Change Log

`0.2.0` - January 20, 2014

-Adding recurrence to allow fully search the directory templates and records are in

-Added ability to set option (**-e**), to special extention


`0.1.0` - January 19, 2014

-Initial i18n_extract release.  Added source code and documentation.
