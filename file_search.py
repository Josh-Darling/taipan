#!/usr/bin/env python3.3
# -*- coding: UTF-8 -*-
# enable debugging

import re
from os import listdir
from os.path import isfile, join

class FileSearch:
    """This object does the following: 
    1. looks into a specified folder
    2.returns a list of all files.
    3. excludes '~' files
    4. evaluates the type of based on encoding ".php",".js",".py" 
    file types are comma delimited written like this: php,js,py.
    However I sugjest using only one file type.
    5. Creates and returns a list based files matching said encoding
    (this is useful) if you are creating an image viewer and do not need
    link names. Or if building headers (see header file)
    6. creates dictionary with LINKNAME --instructions:
            in the file comment using an octothrope 
            and key word in capital letters [# LINKNAME:]
            example (exactly like this):
            # LINKNAME:My Home Page
    """
    def __init__(self,file_location):
        self.file_location=file_location
    def find_all_files(self):
        """finds all files in specified directory"""
        look4files = [ f for f in listdir(self.file_location) if isfile(join(self.file_location,f)) ]
        return look4files
    def files_in_folder(self):
        """This removes all duplicate files and "compiled" files,
        then returns a list, FILES ONLY.
        
        What this is good for:
        if you need to access ALL types of files in a folder.
        And can be used to create a loop that will produce 
        a pic viewer in bootstrap (if you have different pic types)
        """
        non_til = set()
        filesInFolder = []
        for f in self.find_all_files():
            newstr = f.replace("~", "")   
            if newstr in self.find_all_files():
                non_til.add(newstr)
        for fs in non_til:
            filesInFolder.append(fs)
        return filesInFolder
    def find_enc(self,en_code):
        """Looks for file encoding type and returns a list of just that.
        Typing hte dot before encode type is not necessary just "py"
        Simple example of usage: 
            Pic viewer of just .jpg files.
            list of redirect headers based on indexed values from a url or cookie
        """
        encode = "(."+en_code+")"
        file_of_type = []
        for file_en in self.files_in_folder():
            found = re.search(encode, file_en)
            if found:
                file_of_type.append(file_en)
        return file_of_type
    def get_page_name(self,en_code):
        """This looks for files in folder with specafied encoding
        and looks for "# LINKNAME:" Everything after the colon is 
        what will be the name unless there is white space BEFORE the 
        first character. 
        
        Then a dictionary is created
        
        If no linkname is found then for the sake security it will be 
        assumed that this is NOT a file you want published to the 
        internet and the file information will not be included in the final
        dictionary that is returned.
        
        For example of object use to access php files:
            for k in all_files.get_page_name('php'):
                print("key:",k, "value",all_files.get_page_name('php')[k]) 
        """
        files_and_names = {}
        for files_named in self.find_enc(en_code):
            search_in_file = open(self.file_location+"/"+files_named)
            for line in search_in_file:
                if '# LINKNAME:' in line:
                    #print(line)
                    new_line = line.split('# LINKNAME:')
                    for nl in new_line:
                        fnl = nl.strip()
                        if fnl is not None:
                            files_and_names[files_named] = fnl
            search_in_file.close()
        return files_and_names
