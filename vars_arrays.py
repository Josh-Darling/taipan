#!/usr/bin/env python3.3
# -*- coding: UTF-8 -*-
# enable debugging

class VarString:
    """variables with string data using two list, 
    the first list is the vairable name
    the second list is the string data"""
    def __init__(self,vari_list,data_list):
        self.vari_list=vari_list
        self.data_list=data_list
    def with_vars(self):
        """JavaScript, Mongodb"""
        n = 0
        for v in self.vari_list:
            print("var", v , "= \""+self.data_list[n]+"\";")
            n += 1
    def w_o_vars(self):
        """Python"""
        n = 0
        for v in self.vari_list:
            print(v , "= \""+self.data_list[n]+"\"")
            n += 1
    def dol_vars(self):
        """PHP"""
        n = 0
        for v in self.vari_list:
            print("$"+ v , "= \""+self.data_list[n]+"\";")
            n += 1
    def my_vars(self):
        """Perl"""
        n = 0
        for v in self.vari_list:
            print("my $"+ v , "= \""+self.data_list[n]+"\";")
            n += 1
    def char_vars(self):
        """C,C++,Java"""
        n = 0
        for v in self.vari_list:
            print("char "+ v , "= \""+self.data_list[n]+"\";")
            n += 1  
    def string_vars(self):
        """Java"""
        n = 0
        for v in self.vari_list:
            print("string "+ v , "= \""+self.data_list[n]+"\";")
            n += 1  
            
class VarInt:
    """variables with interger data using two list, 
    the first list is the interger name
    the second list is the interger data
    however the information in the list must
    be strings.
    """
    def __init__(self,vari_list,data_list):
        self.vari_list=vari_list
        self.data_list=data_list
    def with_vars(self):
        """Javascript, Mongodb"""
        n = 0
        for v in self.vari_list:
            print("var", v , "= "+self.data_list[n]+";")
            n += 1
    def w_o_vars(self):
        """Python"""
        n = 0
        for v in self.vari_list:
            print(v , "= "+self.data_list[n]+"")
            n += 1
    def dol_vars(self):
        """PHP,Shell"""
        n = 0
        for v in self.vari_list:
            print("$"+ v , "= "+self.data_list[n]+";")
            n += 1
    def my_vars(self):
        """Perl"""
        n = 0
        for v in self.vari_list:
            print("my $"+ v , "= "+self.data_list[n]+";")
            n += 1
    def int_vars(self):
        """C,C++,Java"""
        n = 0
        for v in self.vari_list:
            print("int "+ v , "= \""+self.data_list[n]+"\";")
            n += 1
    def float_vars(self):
        """C,C++,java"""
        n = 0
        for v in self.vari_list:
            print("float "+ v , "= \""+self.data_list[n]+"\";")
            n += 1 
    def double_vars(self):
        """java"""
        n = 0
        for v in self.vari_list:
            print("double "+ v , "= \""+self.data_list[n]+"\";")
            n += 1 
    
class ArrayAssoc:
    """Array with variables containing string 
    this uses a variable that names the array
    and two lists, 
    the first list is the variable name
    the second list is the string data
    however the information in the list must
    be strings.
    """
    def __init__(self,array_name,array_var_list,array_data):
        self.array_name = array_name
        self.array_var_list = array_var_list
        self.array_data = array_data
    def json(self):
        """creates a named JSON object"""
        n = 0
        stop = self.array_var_list
        stop_at = len(stop)
        print ("var",self.array_name,"= {")
        for v in self.array_var_list:
            if n <  (stop_at-1):
                print("\t", v , ": \""+self.array_data[n]+"\",")
                n += 1
            else:
                print("\t", v , ": "+self.array_data[n])
        print("};")
            
    def py_dic(self):
        """Since Python doesn't have "arrays" I
        felt this the best fit for dictionaries """
        n = 0
        stop = self.array_var_list
        stop_at = len(stop)
        print (self.array_name,"= {",end='')
        for v in self.array_var_list:
            if n < (stop_at-1):
                print(v , ": \""+self.array_data[n]+"\", ",end='')
                n += 1 
            else:
                print(v , ": \""+self.array_data[n]+"\"",end='')
        print("}",end='')
        print("\n")
    def php_array(self):
        """What WERE variable names merely
        become keys to access strings"""
        n = 0
        stop = self.array_var_list
        stop_at = len(stop)
        print ("$"+self.array_name,"= array(")
        for v in self.array_var_list:
            if n < (stop_at-1):
                print("\t\'"+v , "\' => \'"+self.array_data[n]+"\', ")
                n += 1 
            else:
                print("\t\'"+v , "\' => \'"+self.array_data[n]+"\'")
        print(");",end='')
        print("\n")
    def php_assoc_var(self):
        """WERE variable names merely
        become keys to access variables"""
        n = 0
        stop = self.array_var_list
        stop_at = len(stop)
        print ("$"+self.array_name,"= array(")
        for v in self.array_var_list:
            if n < (stop_at-1):
                print("\t\'"+v , "\" => $"+self.array_data[n]+", ")
                n += 1 
            else:
                print("\t\'"+v , "\" => $"+self.array_data[n])
        print(");",end='')
        print("\n")    
    
    def hash(self):
        """Since hash is unique to perl I felt it fit pest here"""
        n = 0
        print ("%"+self.array_name,"= (")
        for v in self.array_var_list:
                print("\t'"+v+ "' =>\""+self.array_data[n]+"\", ")
                n += 1 
        print(");",end='')
        print("\n")
    
class ArrayVarIndx:
    def __init__(self,array_name,array_var_list):
        self.array_name = array_name
        self.array_var_list = array_var_list
    def js_array(self):
        n = 0
        stop = self.array_var_list
        stop_at = len(stop)
        print ("var",self.array_name,"= [")
        for v in self.array_var_list:
            if n <  (stop_at-1):
                print("\t\""+ v +"\",")
                n += 1
            else:
                print("\t\""+ v +"\"")
        print("];") 
    def php_array(self):
        n = 0
        stop = self.array_var_list
        stop_at = len(stop)
        print ("$"+self.array_name,"= array(")
        for v in self.array_var_list:
            if n <  (stop_at-1):
                print("\t\""+ v +"\",")
                n += 1
            else:
                print("\t\""+ v +"\"")
        print(");")
    def py_list(self):
        n = 0
        stop = self.array_var_list
        stop_at = len(stop)
        print (self.array_name,"= [",end='')
        for v in self.array_var_list:
            if n <  (stop_at-1):
                print("\t\""+ v +"\",",end='')
                n += 1
            else:
                print("\t\""+ v +"\"",end='')
        print   
    def perl_array(self):
        n = 0
        stop = self.array_var_list
        stop_at = len(stop)
        print ("@"+self.array_name,"= (")
        for v in self.array_var_list:
            if n <  (stop_at-1):
                print("\t\""+ v +"\",")
                n += 1
            else:
                print("\t\""+ v +"\"")
        print(");")
