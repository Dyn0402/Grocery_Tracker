#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on September 07 10:44 AM 2022
Created in PyCharm
Created as Grocery_Tracker/kroger_api_test.py

@author: Dylan Neff, Dylan
"""

import requests


def main():
    # For Grocery_Price_Tracker certification app
    # client_id = 'grocerypricetracker-f4a13239b8e6ea71373e5fc2ff0f30aa3026571454930215297'
    # client_secret = 'EubZ4YsJ6kzlAwEtP4NvEW9uvmTuVzUdYMy4q9V2'

    # For Grocery_Price_Tracker_Prod production app
    client_id = 'grocerypricetrackerprod-9e1d70bdba77eae8f0c7ed39392614b78421945594214916533'
    client_secret = 'FCN04h2MgWOyTB-NkfgVwpPLw15lifRgDwYwR2jn'

    token = get_token(client_id, client_secret)
    # get_product_test(token)
    # token = get_token_loc(client_id, client_secret)
    # token = get_client_access_token_test(client_id, client_secret)
    # get_product_test(token)
    # get_product_details_test(token)
    product_search(token, "Kellogg's Protein")
    # get_chains(token)
    # get_location_id(token, 90025)
    # get_loc_details(token, '70300759')
    print('donzo')


def get_location_id(token, zip_code):
    location_url = 'https://api-ce.kroger.com/v1/locations'
    loc_head = {'Accept': 'application/json', 'Authorization': f'bearer {token}'}
    loc_params = {'filter.zipCode.near': f'{zip_code}', 'filter.chain': 'Ralphs'}
    r = requests.get(location_url, headers=loc_head, params=loc_params)
    locations = r.json()['data']
    print(len(locations))
    print(locations[0].keys())
    for location in locations:
        print(location['name'])
        print(location['address'])
        print(location['locationId'])
        print()


def get_chains(token):
    chains_url = 'https://api-ce.kroger.com/v1/chains'
    chains_head = {'Accept': 'application/json', 'Authorization': f'Bearer {token}'}
    # loc_params = {'filter.zipCode.near': f'{zip_code}'}
    r = requests.get(chains_url, headers=chains_head)
    print(r)
    print(r.json())


def get_token(client_id, client_secret):
    token_url = 'https://api.kroger.com/v1/connect/oauth2/token'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    params = {'grant_type': 'client_credentials', 'scope': ['product.compact']}
    r = requests.post(token_url, headers=headers, data=params,
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


def get_loc_details(token, loc_id):
    loc_details_url = f'https://api-ce.kroger.com/v1/locations/{loc_id}'
    head = {'Accept': 'application/json', 'Authorization': f'Bearer {token}'}
    r = requests.get(loc_details_url, headers=head)
    print(r)
    print(r.json()['data'])


def get_product_test(token):
    product_url = 'https://api-ce.kroger.com/v1/products'
    prod_head = {'Accept': 'application/json', 'Authorization': f'Bearer {token}'}
    westwood_id = '70300759'
    prod_params = {'filter.locationID': westwood_id, 'filter.productId': '0007680853357', 'filter.fulfillment': 'ais',
                   'filter.limit': '5'}
    r = requests.get(product_url, headers=prod_head, params=prod_params)
    products = r.json()['data']
    print(products)
    print(len(products))
    print(type(products[0]))
    print(products[0].keys())
    for product in products:
        print(product)
        print()


def get_product_details_test(token):
    product_url = 'https://api.kroger.com/v1/products/0003800020066'
    prod_head = {'Content-Type': 'application/json', 'Authorization': f'Bearer {token}'}
    westwood_id = '70300759'
    # prod_params = {'filter.locationID': westwood_id}
    prod_params = {'filter.term': None, 'filter.locationId': '70300759', 'filter.product_id': None,
                   'filter.brand': None, 'filter.fulfillment': 'ais', 'filter.limit': None}
    r = requests.get(product_url, headers=prod_head, params=prod_params)
    print(r)
    product = r.json()['data']
    print(product)
    print(product.keys())
    print(product['items'])


def product_search(token, name):
    product_url = 'https://api.kroger.com/v1/products'
    prod_head = {'Content-Type': 'application/json', 'Authorization': f'Bearer {token}'}
    westwood_id = '70300759'
    # prod_params = {'filter.locationID': westwood_id, 'filter.fulfillment': 'ais', 'filter.term': name,
    #                'filter.limit': '10', 'filter.brand': None, 'filter.product_id': None}
    prod_params = {'filter.term': "Kellogg's Protein", 'filter.locationId': '70300759', 'filter.product_id': None,
                   'filter.brand': None, 'filter.fulfillment': 'ais', 'filter.limit': 10}
    print(prod_params)
    r = requests.get(product_url, headers=prod_head, params=prod_params)
    print(r)
    products = r.json()['data']
    print(products)
    print(len(products))
    print(type(products[0]))
    print(products[0].keys())
    for product in products:
        print(product['description'], product['productId'], product['items'])
        print()


if __name__ == '__main__':
    main()
