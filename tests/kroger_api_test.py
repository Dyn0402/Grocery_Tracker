#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on September 07 10:44 AM 2022
Created in PyCharm
Created as Grocery_Tracker/kroger_api_test.py

@author: Dylan Neff, Dylan
"""

import requests
import json
import base64


def main():
    client_id = 'grocerypricetracker-f4a13239b8e6ea71373e5fc2ff0f30aa3026571454930215297'
    client_secret = 'EubZ4YsJ6kzlAwEtP4NvEW9uvmTuVzUdYMy4q9V2'

    token = get_token(client_id, client_secret)
    # get_product_test(token)
    # token = get_token_loc(client_id, client_secret)
    # token = get_client_access_token_test(client_id, client_secret)
    # get_product_test(token)
    # get_chains(token)
    get_location_id(token, 90025)
    print('donzo')


def get_location_id(token, zip_code):
    location_url = 'https://api-ce.kroger.com/v1/locations'
    loc_head = {'Accept': 'application/json', 'Authorization': f'bearer {token}'}
    loc_params = {'filter.zipCode.near': f'{zip_code}'}
    r = requests.get(location_url, headers=loc_head, params=loc_params)
    print(r)
    print(r.json()['data'])


def get_chains(token):
    chains_url = 'https://api-ce.kroger.com/v1/chains'
    chains_head = {'Accept': 'application/json', 'Authorization': f'Bearer {token}'}
    # loc_params = {'filter.zipCode.near': f'{zip_code}'}
    r = requests.get(chains_url, headers=chains_head)
    print(r)
    print(r.json())


def get_token(client_id, client_secret):
    token_url = 'https://api-ce.kroger.com/v1/connect/oauth2/token'
    r = requests.post(token_url, data={'grant_type': 'client_credentials', 'scope': 'product.compact'},
                      auth=(client_id, client_secret))
    token = r.json()["access_token"]

    return token


def get_token_loc(client_id, client_secret):
    token_url = 'https://api-ce.kroger.com/v1/connect/oauth2/token'
    r = requests.post(token_url, data={'grant_type': 'client_credentials'},
                      auth=(client_id, client_secret))
    print(r.json())
    token = r.json()["access_token"]

    return token


def get_product_test(token):
    product_url = 'https://api-ce.kroger.com/v1/products'
    prod_head = {'Accept': 'application/json', 'Authorization': f'Bearer {token}'}
    prod_params = {'filter.locationID': '01400943', 'filter.productId': '0007680853357', 'filter.fulfillment': 'ais',
                   'filter.limit': '5'}
    r = requests.get(product_url, headers=prod_head, params=prod_params)
    print(r)
    print(r.json())


if __name__ == '__main__':
    main()
