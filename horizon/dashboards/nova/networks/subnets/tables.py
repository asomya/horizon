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


class DeleteSubnet(tables.DeleteAction):
    data_type_singular = _("Subnet")
    data_type_plural = _("Subnets")

    def delete(self, request, obj_id):
        pass


class CreateSubnet(tables.LinkAction):
    name = "create"
    verbose_name = _("Create Subnet")
    classes = ("ajax-modal", "btn-create")

    def get_link_url(self, datum=None):
        network_id = self.table.kwargs['network_id']
        return reverse(
            'horizon:nova:networks:subnets:create',
            args=[network_id])


class SubnetsTable(tables.DataTable):
    id = tables.Column("id", verbose_name=_("Subnet Id"))
    cidr = tables.Column("cidr", verbose_name=_("CIDR"))

    def get_object_id(self, subnet):
        return subnet.id

    class Meta:
        name = "subnets"
        verbose_name = _("Subnets")
        table_actions = (CreateSubnet, DeleteSubnet)
        row_actions = (DeleteSubnet,)
