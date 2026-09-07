#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on September 11 12:34 PM 2022
Created in PyCharm
Created as Grocery_Tracker/KrogerClient.py

Based off of python-kroger-client by jtbricker

@author: Dylan Neff, Dylan
"""

import requests


class Location:
    def __init__(self):
        self.id = None
        self.address = None
        self.chain = None
        self.name = None
        self.lat = None
        self.lng = None


class Product:
    def __init__(self):
        self.id = None
        self.upc = None
        self.brand = None
        self.in_store = None
        self.price = None
        self.promo = None
        self.size = None


class KrogerClient:
    def __init__(self, client_id, client_secret):
        self.token = get_token(client_id, client_secret)

    def get_product(self):
        pass

    def get_location(self):
        pass


def get_token(client_id, client_secret):
    token_url = 'https://api.kroger.com/v1/connect/oauth2/token'
    params = {'grant_type': 'client_credentials', 'scope': ['product.compact']}
    r = requests.post(token_url, data=params, auth=(client_id, client_secret))
    token = r.json()["access_token"]

    return token
