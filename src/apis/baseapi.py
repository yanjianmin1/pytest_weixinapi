#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from initialization.sysconfig import sys_cfg
import logging

class BaseApi:

    def __init__(self):
        logging.info("Init base api interface")
        self.host = sys_cfg.get('host_para', 'host')
        self.corp_id = sys_cfg.get('corp_para', 'corp_id')
        self.token_url = sys_cfg.get('corp_para', 'token_url')
        self.res = ' '

    def get_token(self, secret):

        params = {'corpid': self.corp_id, 'corpsecret': secret}
        logging.info('params:' + str(params))
        token_url =  self.host + self.token_url
        logging.info('token_rul:' + str(token_url))
        token_res = requests.get(token_url, params=params, verify=False)
        return token_res.json().get("access_token")


    def post_json(self,url,json_obj,params=None):
        if params:
            self.res = requests.post(url, json=json_obj, params=params, verify=False)
        else:
            self.res = requests.post(url, json=json_obj, verify=False)

    def get_response(self):
        logging.debug('response:' + str(self.res.json()))
        return self.res.json()

    def get_params(self, url, params):
        self.res = requests.get(url, params=params, verify=False)