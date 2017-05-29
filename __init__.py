# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from . import asset


def register():
    Pool.register(
        asset. Asset,
        module='account_asset_account_move_close', type_='model')
