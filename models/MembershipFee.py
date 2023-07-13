from odoo import fields, models, api
from odoo.exceptions import ValidationError

class MembershipFee(models.Model):
    _name = 'membership.fee'
    _description = 'Membership Fee'

    name = fields.Char(string='Name', required=True)
    amount = fields.Float(string='Amount', required=True)
    membership_type = fields.Selection([
        ('reguler', 'Reguler'),
        ('premium', 'Premium')
    ], string='Membership Type', required=True)
    is_active = fields.Boolean(string='Active', default=True)