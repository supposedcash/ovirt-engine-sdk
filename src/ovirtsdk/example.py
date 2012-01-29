#
# Copyright (c) 2010 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#           http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from ovirtsdk.api import API
from ovirtsdk.xml import params

#create proxy
api = API(url='http://host:port', username='user@domain', password='password')

#list
vms1 = api.vms.list()

#list by oVirt query
vms2 = api.vms.list(query='name=python_vm')

#list by oVirt query and supported extra parameter/s
events = api.events.list(query='severity=error', from_event_id=9183)

#search vms by property constraint
vms3 = api.vms.list(memory=536870912)

#update resource
vm1 = api.vms.get(name='python_vm')

mem = vm1.memory
vm1.description = 'updated_desc'
vm2 = vm1.update()
vm3 = api.vms.get(name='python_vm')

#list by constraints
vms4 = api.vms.list(name='pythond_sdk_poc2')

#get by name
vm4 = api.vms.get(name='pythond_sdk_poc2')

#get by constraints
vm5 = api.vms.get(id='02f0f4a4-9738-4731-83c4-293f3f734782')

if vm4 is None:

    #add vm
    cluster = api.clusters.get(name='Default_nfs')
    template = api.templates.get(name='nfs_desktop_tmpl')
    param = params.VM(name='pythond_sdk_poc2', cluster=cluster, template=template, memory=1073741824)
    vm6 = api.vms.add(param)

    #add nic to vm
    network = cluster.networks.get('engine')
    nic = params.NIC(name='eth0', network=network, interface='e1000')
    vm6.nics.add(nic)

    #list vm's nics
    nics1 = vm6.nics.list()

    #list vm's nics by constraints
    nics2 = vm6.nics.list(name='eth0')
    nics3 = vm6.nics.list(interface='e1000')

    #get sub resource
    nic1 = vm6.nics.get(name='eth0')

    #update sub-resource
    nic1.name = 'eth01'
    nic2 = nic1.update()
    nic3 = vm6.nics.get(name='eth01')

    #perform action on resource
    result = vm6.start()

#delete the vm
else:
    result = vm4.delete()