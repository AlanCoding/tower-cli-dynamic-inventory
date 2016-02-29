#!/usr/bin/python

"""
Ansible Tower external inventory script
=================================

Ansible has a feature where instead of reading from /etc/ansible/hosts
as a text file, it can query external programs to obtain the list
of hosts, groups the hosts are in, and even variables to assign to each host.

Ansible Tower has a feature where a specfic endpoint will output data
compatible with using it as such an external inventory source.

"""

# 2016, Alan Rominger <alan.rominger@gmail.com>
#
# The necessary free license will be added here when the code is
# submitted for inclusion as a part of Ansible modules extras.

######################################################################


import tower-cli

import argparse

try:
    import json
except ImportError:
    import simplejson as json


class CobblerInventory(object):

    def __init__(self):

        """ Main execution path """
        self.conn = None

        self.inventory = dict()  # A list of groups and the hosts in that group
        self.cache = dict()  # Details about hosts in the inventory
        
        # Read settings and parse CLI arguments
        self.read_settings()
        self.parse_cli_args()
        
        inventory_res = tower_cli.get_resource('inventory')

        dict_result = inventory_res.inventory_source(name="inventory_name")
        
        self.inventory = self.json_format_dict(dict_result)

        print(self.inventory)


    def parse_cli_args(self):
        """ Command line argument processing """

        parser = argparse.ArgumentParser(description='Produce an Ansible Inventory file from Tower')
        parser.add_argument('--list', action='store_true', default=True, help='List instances (default: True)')
        parser.add_argument('--host', action='store', help='The inventory ID or name to get data on')
        self.args = parser.parse_args()


    def json_format_dict(self, data, pretty=False):
        """ Converts a dict to a JSON object and dumps it as a formatted string """

        if pretty:
            return json.dumps(data, sort_keys=True, indent=2)
        else:
            return json.dumps(data)

CobblerInventory()