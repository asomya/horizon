# vim: tabstop=4 shiftwidth=4 softtabstop=4

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
import logging

from django.contrib import messages
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from horizon import api
from horizon import tables


LOG = logging.getLogger(__name__)


class DeleteNetwork(tables.DeleteAction):
    data_type_singular = _("Network")
    data_type_plural = _("Networks")

    def delete(self, request, obj_id):
        pass


class CreateNetwork(tables.LinkAction):
    name = "create"
    verbose_name = _("Create Network")
    url = "horizon:nova:networks:create"
    classes = ("ajax-modal", "btn-create")


def _get_subnets(network):
    str = ''
    for subnet in network.subnets:
        if str:
            str = str.join((',', subnet.cidr))
        else:
            str = str.join(subnet.cidr)

    return str


class NetworksTable(tables.DataTable):
    id = tables.Column("id", 
                       verbose_name=_("Network Id"),
                       link='horizon:nova:networks:subnets:index')
    name = tables.Column("name", verbose_name=_("Network Name"))
    subnets = tables.Column(_get_subnets, 
                            verbose_name=_("Subnets Associated"),)

    def get_object_id(self, network):
        return network.id

    class Meta:
        name = "networks"
        verbose_name = _("Networks")
        table_actions = (CreateNetwork, DeleteNetwork)
        row_actions = (DeleteNetwork,)
