# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
#
# Copyright 2012 Cisco Systems, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
Views for managing Quantum Subnets.
"""
import logging

from horizon.api import quantum
from horizon import exceptions
from horizon import forms
from horizon import tables
from .tables import SubnetsTable
from .forms import CreateSubnet


LOG = logging.getLogger(__name__)


class IndexView(tables.DataTableView):
    table_class = SubnetsTable
    template_name = 'nova/networks/subnets/index.html'

    def get_data(self):
        network = quantum.network_get(self.request, self.kwargs['network_id'])
        return network.subnets


class CreateView(forms.ModalFormView):
    form_class = CreateSubnet
    template_name = 'nova/networks/subnets/create.html'
