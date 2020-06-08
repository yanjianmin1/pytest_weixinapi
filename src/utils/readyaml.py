#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import yaml

def Read_File_Yaml(file_path):
    with codecs.open(file_path,'r',encoding='utf8') as load_f:
        load_dict = yaml.load(load_f)
        return load_dict

def Update_File_Yaml(file_path,case_name,dict_key,new_values):
    load_dict = Read_File_Yaml(file_path)
    load_dict[case_name][dict_key] = new_values
    with codecs.open(file_path, "w", encoding='utf-8') as dump_f:
        yaml.dump(load_dict, dump_f, allow_unicode=True, default_flow_style=False)
    return load_dict


