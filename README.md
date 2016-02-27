# tower-cli-dynamic-inventory

Ansible dynamic inventory source that pulls inventory from Ansible Tower

This operates in conjunction with the tower-cli inventory script feature.
Ordinarily, that can be run with the following type of command:

```bash
tower-cli inventory script --name="QA_machines"
```

This produces a Ansible-compatible JSON output which can be used as the
dynamic inventory source. The intent for this module is to link that 
capability to Ansible core with something like the following command:

```bash
ansible -i tower-inventory.py -u ubuntu us-east-1d -m ping
```

Credit to [ansible docs](http://docs.ansible.com/ansible/intro_dynamic_inventory.html)
for the example with the framework for that structure.

## Setup

For now, testing this will have to be done straight from source, and since
the inventory_source feature for tower-cli still hasn't been released,
that will percolate into the requirements here.

It is suggested that you use a virtual environment specific to this project.

You may need to `chmod +x` the `tower-inventory.py` file in this repo.

## Use Stories

### I want Tower to update my Ansible inventory

I have a dynamic inventory source stored in Ansible Tower. Let's say this
contains ec2 machines, for which I have the `.pem` file stored on my computer
locally, but I do not
have the cloud credentials too. Or someone else manages those cloud credentials.
This dynamic inventory would allow me to automatically launch commands

## Further Reading

An canon example of using the tower-cli libraries directly in python can be
found at the [tower-populator](https://github.com/jsmartin/tower_populator)
repo. The general cadence of coding by this guideline is:

```python
import tower_cli

user_res = tower_cli.get_resource('user')

user = user_res.create(
  username='Sherlock', password='p4ass12986', email='email@domain.com',
  first_name='Sherlock', last_name="Holmes", 
)
```

The inventory source command would be accessed similarly, replacing `user`
with `inventory` and `create` with `inventory_source`.

These will be implemented in the dynamic inventory source `.py` file in
this repository.