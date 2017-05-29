# This file is part account_asset_percent module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pyson import Eval
from trytond.pool import PoolMeta

__all__ = ['Asset']


class Asset:
    __metaclass__ = PoolMeta
    __name__ = 'account.asset'

    square_account = fields.Many2One('account.account', 'Square Account',
        domain=[
            ('company', '=', Eval('context', {}).get('company', -1)),
            ],
        depends= ['company'])

    def get_closing_move(self, account):
        if self.square_account:
            account = self.square_account
        return super(Asset, self).get_closing_move(account)
