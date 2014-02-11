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
import fnmatch

class I18nExtract:
    regex = r"polyglot.t\(['\"](.*)['\"]\)"
    __correct_index = []

    def __init__(self, template_folder, locale_folder):
        self.template_folder = template_folder
        self.locale_folder = locale_folder

        self.__extract_template_keys()

    def __extract_template_keys(self):
        
        '''
        Finds all files in the given directory, as well as those in subdirectories
        '''
        template = [
            os.path.join(dirpath, f)
            for dirpath, dirnames, files in os.walk(os.path.join(os.path.realpath(self.template_folder)))
            for f in files
        ]

        '''
        Just a simple loop for read and add current key to a list
        '''
        for file_ in template:
            results = re.findall(self.regex, open(file_).read())
            print "%s anchors have been found in %s: \n%s\n" % (len(results), file_, results)

            for result in results:
                self.__correct_index.append(result)

        self.__update_locales()

    '''
    Intert the news keys founded in all templates
    '''
    def __insert_data(self, json_file):
        for data_index in set(self.__correct_index):
            if data_index not in self.json_datas.keys():
                self.json_datas.update({data_index: None})
                print "['%s'] as been added." % (data_index)

        json.dump(self.json_datas, open(json_file, 'w'), indent=4, sort_keys=True)

    '''
    Updates all the keys contained in the nTranslation files
    '''
    def __remove_data(self, json_file):
        for key in self.json_datas.keys():
            if key not in set(self.__correct_index):
                del self.json_datas[key]
                print "['%s'] as been deleted." % (key)

        json.dump(self.json_datas, open(json_file, 'w'), indent=4, sort_keys=True)

    '''
    Call __remove_data function and __insert_data function
    '''
    def __update_locales(self):
        for json_file in glob.glob(os.path.join(os.path.realpath(self.locale_folder), "*.json")):
            if os.stat(json_file)[stat.ST_SIZE] > 0:
                
                print "\nPROCESSING %s file." % json_file.split('/')[-1:]
                with open(json_file, "r") as feed_json:
                    try:
                        self.json_datas = json.loads(feed_json.read())

                        self.__remove_data(json_file)
                        self.__insert_data(json_file)

                        print "--UPDATED FILE--"

                    except (ValueError, KeyError, TypeError):
                        print "\n--------------- JSON FORMAT ERROR ---------------\n ValuError: %s\n KeyError: %s\n TypeError: %s\n" % (
                            ValueError, KeyError, TypeError)


try:
    if len(sys.argv) > 1:
        options, args = getopt.getopt(sys.argv[1:], "t:l:e:")
        templates_folder = None
        locales_folder = None
        
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
