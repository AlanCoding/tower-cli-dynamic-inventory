#!/usr/bin/python

import tower-cli

inventory_res = tower_cli.get_resource('inventory')

json_result = inventory_res.inventory_source(name="inventory_name")