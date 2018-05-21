# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import simplejson as json
import requests
from urllib import parse


AUTHORIZATION_URL = 'https://www.linkedin.com/uas/oauth2/authorization'
ACCESS_TOKEN_URL = 'https://www.linkedin.com/uas/oauth2/accessToken'

class LinkedinOauthClient(object):

    is_authorized = False

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def get_authorize_url(self):
        auth_setting = {'response_type' : 'code',
                        'client_id' : self.client_id,
                        'client_secret' : self.client_secret,
                        'redirect_uri' : '/hackathon/',
                        'state' : 'DCEeFWf45A53sdfKef424',
                        'scope': 'r_basicprofile'}

        params = parse.urlencode(auth_setting)
        authURL = AUTHORIZATION_URL + '?' + params
        return authURL

    def get_access_token(self, code):
        settings = {'grant_type' : 'authorization_code',
                    'code' : code,
                    'redirect_uri' : '/hackathon/',
                    'client_id' : self.client_id,
                    'client_secret': self.client_secret}

        header = {'content-type' : 'application/x-www-form-urlencoded'}
        req = requests.post(ACCESS_TOKEN_URL, data=settings)#, headers=header)

        if req.status_code != 200:
            raise Exception('Invalid response %s' %req.status_code)

        content = json.loads(req.content)
        self.access_token = content['access_token']
        self.is_authorized = True

    def getUserInfo(self):
        #link = 'https://api.linkedin.com/v1/people/~?format=json&oauth2_access_token=' + self.access_token
        link = 'https://api.linkedin.com/v1/people/~:(id,first-name,skills,educations,languages,twitter-accounts)?oauth2_access_token='+self.access_token
        headers = {'x-li-format' : 'json',
                   'content-type' : 'application/json'}
        req = requests.get(link, headers=headers)
        content = json.loads(req.content)

        if req.status_code != 200:
            raise Exception('Invalid response %s' %req.status_code)

        self.user_id = content['id']
        print (content)
        return content
