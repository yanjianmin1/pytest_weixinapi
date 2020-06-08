#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from apis.baseapi import BaseApi
from initialization.sysconfig import sys_cfg
import logging
from utils.readyaml import *
from utils.randomchinese import *

class DeptManagement(BaseApi):

    def __init__(self):
        BaseApi.__init__(self)
        logging.info("Init department management API")
        self.create_dep_url = sys_cfg.get('contact_para', 'crate_dep_url')
        self.dep_secure = sys_cfg.get('contact_para', 'secure')
        self.dep_lists_url = sys_cfg.get('contact_para', 'dep_lists_url')

    def create_dept_nameRandom(self, dep_name):
        logging.info("dep_name:"+str(dep_name))
        new_name = "自动化" + get_random_char1(3)
        logging.info("new_name:"+str(new_name))
        new_dict = Update_File_Yaml('../testdata/create_dep.yaml', dep_name, 'name', new_name)
        new_part = new_dict.get(dep_name)
        logging.debug("new_part:"+str(new_part))
        param = {'access_token': self.get_token(self.dep_secure)}
        create_dep_url = self.host + self.create_dep_url
        logging.debug("url:" + str(create_dep_url))
        logging.debug("params:" + str(param))
        self.post_json(create_dep_url, new_part, params=param)

    def get_create_dept_res(self):
        return self.get_response()


    def create_dept(self, dep_name):
        new_part = (Read_File_Yaml('../testdata/create_dep.yaml')).get(dep_name)
        logging.debug("new_part:"+str(new_part))
        param = {'access_token': self.get_token(self.dep_secure)}
        create_dep_url = self.host + self.create_dep_url
        logging.debug("url:" + str(create_dep_url))
        logging.debug("params:" + str(param))
        self.post_json(create_dep_url, new_part, params=param)

    def get_dep_lists(self, id=None):
        #param = {}
        if id:
            param = {'access_token': self.get_token(self.dep_secure), 'id': id}
        else:
            param = {'access_token': self.get_token(self.dep_secure)}
        logging.info("param:"+str(param))
        dep_lists_url = self.host + self.dep_lists_url
        self.get_params(dep_lists_url, params=param)