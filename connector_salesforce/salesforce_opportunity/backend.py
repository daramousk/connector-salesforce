# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Nicolas Bessi
#    Copyright 2015 Camptocamp SA
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import models, fields, api


class SalesforceOpportunityBackend(models.Model):

    _inherit = 'connector.salesforce.backend'

    sf_last_opportunity_import_sync_date = fields.Datetime(
        'Last Opportunity Import Date'
    )

    sf_sales_team_id = fields.Many2one(
        'crm.case.section',
        'Sales team to be used',
        required=True,
    )

    @api.multi
    def import_sf_opportunity(self):
        """Run the import of Salesforce opportunites for given backend"""
        self._import(
            'connector.salesforce.opportunity',
            'direct',
            'sf_last_opportunity_import_sync_date',
        )

    @api.multi
    def import_sf_opportunity_delay(self):
        """Run the import of Salesforce opportunites for given backend
        using jobs
        """
        self._import(
            'connector.salesforce.opportunity',
            'delay',
            'sf_last_opportunity_import_sync_date',
        )
