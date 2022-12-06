#!/usr/bin/python3
# -*- coding:utf-8 -*-
#
# @name   : EmailAll - Email Information Gathering Tools
# @url    : http://github.com/Taonn
# @author : Tao. (Taonn)
# bug fixed by ccc-f 2022/12/06
import requests
import json
import re

from common.search import Search
from urllib.parse import unquote, quote
from config import settings
from config.log import logger


class Snov(Search):
    def __init__(self, domain):
        Search.__init__(self)
        self.domain = domain
        self.module = 'Datasets'
        self.source = 'Snov'
        self.addr = 'https://app.snov.io'
        self.username = settings.snov_username
        self.password = settings.snov_password
        self.num = 999
        self.session = requests.session()

    def login(self):

        resp = self.session.get(self.addr + '/login')
        if resp:
            token = re.findall(r'"csrf-token" content="(.*)"', resp.text)[0]
            param = {
                "email": settings.snov_username,
                "password": settings.snov_password,
                "remember": True
            }
            self.header.update({
                        'X-Csrf-Token': token,
                        'X-Requested-With': 'XMLHttpRequest',
                        'Content-Type': 'application/json;charset=utf-8',
                        'Referer': 'https://app.snov.io/login',
                        'Origin': 'https://app.snov.io'
                    })
            if token:
                rep = self.session.post(self.addr + '/login', headers=self.header, json=param)
                if rep.status_code == '301':
                    return True
            else:
                return

    def search(self):

        if self.login():
            resp = self.session.get(self.addr + '/domain-search')
            if resp:
                token = re.findall(r'"_meta" content="(.*)"', resp.text)[0]
                self.header.update({
                    'X-Csrf-Token': token,
                    })
            self.header.update({'Content-Type': 'application/json;charset=UTF-8'})
            params = {"domain": self.domain,
                      "isGreen": 'true',
                      "lastId": 0,
                      "perPage": 20}
            resp = self.session.post(self.addr + '/domain-search', headers=self.header, json=params)
            if hasattr(resp, 'json'):
                resp_json = resp.json()
                cid = resp_json["companyInfo"]["id"]
                params = {"isGreen": True,
                          "lastId": 0,
                          "perPage": self.num,
                          "page": 1}
                rep = self.session.post(self.addr + f'/companies/{cid}', headers=self.header)
                self.header.update({'Referer': f'https://app.snov.io/domain-search?name={self.domain}&tab=emails',
                                    'X-Requested-With': 'XMLHttpRequest'})
                rep = self.session.post(self.addr + f'/companies/{cid}/emails', headers=self.header, json=params)
                emails = self.match_emails(rep)
                if emails:
                    self.results.update(emails)
                else:
                    return
        else:
            logger.log('ALERT', 'Search Failed! you need to configure the username&password in api.py file')
            return

    def run(self):
        self.begin()
        self.search()
        self.finish()
        self.save_json()
        self.save_res()


def run(domain):
    search = Snov(domain)
    search.run()


if __name__ == '__main__':
    run('pingan.com.cn')
