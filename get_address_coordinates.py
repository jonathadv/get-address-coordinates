#!/usr/bin/python3
#!-*- conding: utf8 -*-

import json
import os

try:
    import requests

except ImportError:
    print('Please install Python3 Requests.')
    os._exit(1)


google_maps_endpoint = 'http://maps.googleapis.com/maps/api/geocode/json?address='


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


def get_address_info(address, city):
    params = '%s %s' % (address, city)

    response = requests.get(google_maps_endpoint + params)

    if response.ok:
        address_object = None

        json_obj = json.loads(response.text)
        results = json_obj['results']

        if len(results) is not 0:
            address_obj = json_obj['results'][0]
            formatted_address = address_obj['formatted_address']
            latitude = address_obj['geometry']['location']['lat']
            longitude = address_obj['geometry']['location']['lng']

            address_object = Address(formatted_address, latitude, longitude)

        return address_object
    else:
        raise Exception('Error when calling API for address: %s. Error %s' % (address, response.reason))


def read_file_as_list(filename):
    try:
        new_file = open(filename, 'r').readlines()
    except IOError:
        print('File \'%s\' not found. Please create it.' % filename)
        os._exit(1)

    for index, line in enumerate(new_file):
        new_line = line.replace('\n', '')
        new_file[index] = new_line

    return new_file


def save_file_from_list(filename, list_of_items):
    with open(filename, 'w') as output_file:

        for item in list_of_items:
            output_file.write(('%s\n' % item))

        output_file.close()

    print('File %s saved!' % filename)


def main():
    address_json_list = []
    address_with_fail = []
    current_city = None
    input_filename = 'addresses.txt'

    address_list = read_file_as_list(input_filename)

    for address in address_list:
        if len(address) is 0:
            continue

        if address[0] is '#':
            current_city = address[1:]
            print('Setting city as %s' % current_city)
            continue

        print('[GET GMaps API] - Address: (%s %s)' % (address, current_city))
        address_object = get_address_info(address, current_city)
        print('[Result] %s' % str(address_object))

        if address_object is not None:
            address_json_list.append(address_object.to_json())
        else:
            address_with_fail.append(address)

    if len(address_json_list) > 0:
        save_file_from_list('addresses.json', address_json_list)
    else:
        print('No successfull results to save.')

    if len(address_with_fail) > 0:
        save_file_from_list('addresses_fail.txt', address_with_fail)
    else:
        print('No failed results to save.')


if __name__ == '__main__':
    main()
