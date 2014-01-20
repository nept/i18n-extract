###Who to use **i18n_extract** python script for Polyglot ?###

	-First copy and paste the python script into your folder
	-Then do a chmod +x on the script to make it executable (sudo chmod +x i18n_extract.py)
	-Then execute the script without forgetting to set parameters
		- "-t" is the directory where your templates file are stored
		- "-l" is the directory where your translates file re stored
	
####Exemple###

	# ./i18n_extract.py -t < templates directory > -l < locales directory >

####Result####

    4 index were found in /i18n-extract/templates/sidebar.jade
    ['hello', 'sidebar', 'content', 'help']

    1 index were found in /i18n-extract/templates/test.jade
    ['welcome']

    Processing /Library/WebServer/Documents/i18n-extract/locales/en.json file:
    ['Test'] as been deleted from the /i18n-extract/locales/en.json
    ['Test2'] as been deleted from the file /i18n-extract/locales/en.json
    ['content'] as been added from the file /i18n-extract/locales/en.json
    ['sidebar'] as been added from the file /i18n-extract/locales/en.json
    ['hello'] as been added from the file /i18n-extract/locales/en.json
    ['welcome'] as been added from the file /i18n-extract/locales/en.json
    ['help'] as been added from the file /i18n-extract/locales/en.json
    Translation file is updated

    Processing /Library/WebServer/Documents/i18n-extract/locales/fr.json file:
    ['Test'] as been deleted from the file /i18n-extract/locales/fr.json
    ['Test2'] as been deleted from the file /i18n-extract/locales/fr.json
    ['content'] as been added from the file /i18n-extract/locales/fr.json
    ['sidebar'] as been added from the file /i18n-extract/locales/fr.json
    ['hello'] as been added from the file /i18n-extract/locales/fr.json
    ['welcome'] as been added from the file /i18n-extract/locales/fr.json
    ['help'] as been added from the file /i18n-extract/locales/fr.json
    Translation file is updated

**OR, if the script is not executable**

	# python i18n_extract.py -t < templates directory > -l < locales directory >

####WARGING
**The translated file must be json format and contain an valid json object**