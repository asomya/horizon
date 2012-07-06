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

from __future__ import absolute_import

import logging
import thread
import urlparse

from django.conf import settings

from horizon.api.base import APIResourceWrapper, APIDictWrapper, url_for


LOG = logging.getLogger(__name__)


class Network(APIDictWrapper):
    """Wrapper for quantum Networks"""
    _attrs = ['name', 'id', 'subnets']


class Subnet(APIDictWrapper):
    """Wrapper for quantum subnets"""
    _attrs = ['id', 'cidr', 'network']


def quantumclient(request):
    pass


def network_list(request):
    networks = []
    return networks


def network_get(request, network_id):
    pass


def network_create(request, network_name):
    pass


def network_modify(request, params):
    pass


def network_delete(request, network_id):
    pass


def subnet_create(request, cidr):
    pass


def subnet_delete(request, subnet_id):
    pass


def subnet_associate(request, network_id, subnet_id):
    pass


def subnet_disassociate(request, subnet_id):
    pass
