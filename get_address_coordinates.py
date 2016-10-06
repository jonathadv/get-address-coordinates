#!/usr/bin/python3

#!-*- conding: utf8 -*-

import json, os
try:
    import requests
except ImportError:
    print('Please install Python3 requests.')
    os._exit(1)


google_maps_endpoint='http://maps.googleapis.com/maps/api/geocode/json?address='

class Address:
    def __init__(self, address, latitude, longitude):
        self.address = address
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        result = "address = [%s], latitude = [%s], longitude = [%s]" % (self.address, self.latitude, self.longitude)
        return result
    def to_json(self):
        result = '{ "address": "%s", "latitude": %s, "longitude": %s }' % (self.address, self.latitude, self.longitude)
        return result


def get_address_info(address, city):filename
    params = address +' '+ city
    print('[GET to Maps API] - Address: (%s)' % params)
    response = requests.get(google_maps_endpoint + params)


    if response.ok:
        addressObject = None

        json_obj = json.loads(response.text)
        results = json_obj['results']

        if len(results) is not 0:
            address_obj = json_obj['results'][0]
            formatted_address = address_obj['formatted_address']
            latitude = address_obj['geometry']['location']['lat']
            longitude = address_obj['geometry']['location']['lng']

            addressObject = Address(formatted_address, latitude, longitude)

        return addressObject

    else:
        raise Error('Error when calling API for address: ' + address + '. Error: '+response.reason)


def read_file_as_list(filename):
    try:        
        new_file = open(filename, 'r').readlines()
    except IOError:
        print('File \'%s\' not found. Please create it.' % filename)
        os._exit(1)
        
    for line in new_file:
        new_line = line.replace('\n', '')
        idx = new_file.index(line)
        new_file[idx] = new_line

    return new_file


def save_file_from_list(filename, list_of_items):
    f = open(filename, 'w')

    for item in list_of_items:
        f.write(item+'\n')

    f.close()

    print('File %s save!' % filename)


def main():
    address_json_list = []
    address_with_fail = []
    current_city=None
    input_filename='addresses.txt'
        
    address_list = read_file_as_list(input_filename)

    for addrr in address_list:
        if addrr[0] is '#':
            current_city = addrr[1:]
            print('Setting city as %s' % current_city)
            continue

        addressObject = get_address_info(addrr, current_city)
        print('addressObject: ' + str(addressObject))
        if addressObject is not None:
            address_json_list.append(addressObject.to_json())
        else:
            address_with_fail.append(addrr)


    save_file_from_list('addresses.json', address_json_list)
    save_file_from_list('addresses_fail.txt', address_with_fail)



''' Lets run it! '''
main()
