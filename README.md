###Who to use **i18n_extract** python script ?###

	-First, copy and paste the python script into your folder
	-Then do a chmod +x on the script to make it executable (sudo chmod +x i18n_extract.py)
	-Then, execute the script without forgetting to set parameters
		- "-t" is the directory where your templates file are stored
		- "-l" is the directory where your translates file re stored
	
####Exemple###

	# ./i18n_extract.py -t < templates directory > -l < locales directory >

**OR, if the script is not executable**

	# python i18n_extract.py -t < templates directory > -l < locales directory >

####WARGING
**The translated file must be json format and contain an valid json object**