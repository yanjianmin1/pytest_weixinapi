#!/usr/bin/env python
# -*- coding: utf-8 -*-

import  configparser
import os
import logging


def read_config(cfg_file):
    cfg = configparser.ConfigParser()
    if os.path.isfile(cfg_file):
        cfg.read(cfg_file)
        return cfg
    else:
        logging.warning(cfg_file+'file is not exist')

sys_cfg = read_config('../cfg/auto.cfg')
