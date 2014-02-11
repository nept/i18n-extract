# i18n-extract

> a simple Python script to parse usage of [Polyglot](https://github.com/airbnb/polyglot.js), a tiny I18n helper library written in JavaScript.

>This script retrieves the anchors in the project and added to the language files.
If an anchor is no longer present in the project, it is removed from the language files.
If it is present in the project and in the language files, it is simply ignored (not delete)

## Usage 

- First clone the repository into your folder
- Then execute the script without forgetting to set
    - `-t` is the directory where your templates file are stored
    - `-l` is the directory where your translates file re stored
        
### Example

```python
#To extract the anchors (all extension) and add in the language files
./i18n_extract.py -t templates/ -l locales/
```

### Script Output

    4 anchors have been found in /Users/pierrejolivet/Sites/GITHUB/i18n-extract/templates/sidebar.jade: 
    ['user.welcome', 'user.account', 'user.logout', 'help']

    1 anchors have been found in /Users/pierrejolivet/Sites/GITHUB/i18n-extract/templates/test.jade: 
    ['calendar.date']

    1 anchors have been found in /Users/pierrejolivet/Sites/GITHUB/i18n-extract/templates/js_files/index.js: 
    ['user.account']

    Processing ['en.json'] file.
    ['user.logout'] as been added.
    ['calendar.date'] as been added.
    ['user.account'] as been added.
    ['user.welcome'] as been added.
    ['help'] as been added.
    --UPDATED FILE--

    Processing ['fr.json'] file.
    ['user.logout'] as been added.
    ['calendar.date'] as been added.
    ['user.account'] as been added.
    ['user.welcome'] as been added.
    ['help'] as been added.
    --UPDATED FILE--

### Result

```js
In fr.json and en.json
{
    "calendar.date": null, 
    "help": null, 
    "user.account": null, 
    "user.logout": null, 
    "user.welcome": null
}
```

## Change Log

`0.3.0` - February 11, 2014

-Removed the option to set one argument for found anchors in special extentions. [Now all extensions are supported]

-Updated script message and README


`0.2.0` - January 20, 2014

-Added recurrence to allow fully search the directory templates and records are in.

-Added the option to set one argument for finded anchors in special extentions (.html, .jade, .hbs...).


`0.1.0` - January 19, 2014

-Initial i18n_extract release.  Added source code and documentation.
