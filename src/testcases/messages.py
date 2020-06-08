#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests


def getToken():
    url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    payload = {"corpid": 'ww5283cbb77b230605',
               "corpsecret": 'UhH7sMhfRGvTXkVwixSudsPz4FFspjZLVSgagqOaRnM'}

    res = requests.get(url, params=payload, verify=False)
    return res.json()['access_token']

def upload_image():
    access_token = getToken()
    url ='https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token='+access_token+'&type=image'
    myfiles = {'media': ('24.jpg', open("../image/24.jpg", 'rb'), 'image/jpg')}
    res = requests.post(url, files=myfiles, verify=False)
    print(res.json()["media_id"])
    return res.json()["media_id"]


def test_message_file():
    access_token = getToken()
    media_id = upload_image()
    url1 = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token='+access_token
    send_json = {
           "touser" : "zero",
           "toparty" : "PartyID1|PartyID2",
           "totag" : "TagID1 | TagID2",
           "msgtype" : "voice",
           "agentid" : 1000002,
           "voice" : {
                "media_id" : media_id
           },
           "enable_duplicate_check": 0,
           "duplicate_check_interval": 1800
        }
    result = requests.post(url1, json=send_json, verify=False)
    #print(result.json())
    assert result.json()["invaliduser"] == ''

def test_message_txt():
    access_token = getToken()
    media_id = upload_image()
    url2 = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token='+access_token
    send_json = {
           "touser" : "zero",
           "toparty" : "PartyID1|PartyID2",
           "totag" : "TagID1 | TagID2",
           "msgtype" : "text",
           "agentid" : 1000002,
           "text" : {
               "content" : "人生苦短，我用python;"
           },
           "safe":0,
           "enable_id_trans": 0,
           "enable_duplicate_check": 0,
           "duplicate_check_interval": 1800
        }
    result = requests.post(url2, json=send_json, verify=False)
    #print(result.json())
    assert result.json()["invaliduser"] == ''
