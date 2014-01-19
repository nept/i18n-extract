#!/usr/bin/env python
# -*-coding:Utf-8 -*

import glob
import sys
import getopt
import os
import stat
import re
import pprint
import json

class I18nExtract:
    regex = r"polyglot.t\(['\"](.*)['\"]\)"
    __correct_index = []

    def __init__(self, template_folder, locale_folder):
        self.template_folder = template_folder
        self.locale_folder = locale_folder
        self.__extract_template_keys()

    def __extract_template_keys(self):
        os.chdir(self.template_folder)

        for template_file in glob.glob("*.jade"):
            file_ = open(template_file).read()
            results = re.findall(self.regex, file_)
            print "%s index were found in %s" % (len(results), template_file)
            pprint.pprint(results)

            for result in results:
                self.__correct_index.append(result)

        self.__update_locales()

    def __insert_data(self, json_file):
        for data_index in set(self.__correct_index):
            if data_index not in self.json_datas.keys():
                self.json_datas.update({data_index: None})
                print "['%s'] as been added from the file %s" % (data_index, json_file)

        json.dump(self.json_datas, open(json_file, 'w'), indent=4)

    def __remove_data(self, json_file):
        for key in self.json_datas.keys():
            if key not in set(self.__correct_index):
                del self.json_datas[key]
                print "['%s'] as been deleted from the file %s" % (key, json_file)

        json.dump(self.json_datas, open(json_file, 'w'), indent=4)

    def __update_locales(self):
        os.chdir(self.locale_folder)

        for json_file in glob.glob("*.json"):
            if os.stat(json_file)[stat.ST_SIZE] > 0:
                print "\nProcessing %s file:" % json_file
                with open(json_file, "r") as feed_json:
                    try:
                        self.json_datas = json.loads(feed_json.read())

                        self.__remove_data(json_file)
                        self.__insert_data(json_file)
                        print "Translation file is updated"
                    except (ValueError, KeyError, TypeError):
                        print "\n--------------- JSON FORMAT ERROR ---------------\n ValuError: %s\n KeyError: %s\n TypeError: %s\n" % (
                            ValueError, KeyError, TypeError)


try:
    templates_folder = None
    locales_folder = None
    options, args = getopt.getopt(sys.argv[1:], "t:l:")

    if sys.argv > 0:
    	for o, a in options:
	        if o == '-t':
	            templates_folder = a
	        elif o == '-l':
        		locales_folder = a
    	if templates_folder is not None and locales_folder is not None:
	        I18nExtract(templates_folder, locales_folder)
	else:
		print("Usage: %s -t < templates folder > -l < locales folder >" % sys.argv[0])
except:
    print("Usage: %s -t < templates folder > -l < locales folder >" % sys.argv[0])
