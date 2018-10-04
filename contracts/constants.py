# Constant definitions for the contracts app
from django.utils.translation import ugettext_lazy as _

EXPENDITURES = (
    ('',  _('unknown')),
    ('c', _('CAPEX')),
    ('o', _('OPEX')),
)
SUBJECTS = (
    ('',   _('unknown')),
    ('hw', _('Hardware')),
    ('sw', _('Software')),
    ('ps', _('Service')),
)
