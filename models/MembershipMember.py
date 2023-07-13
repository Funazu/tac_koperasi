from odoo import fields, models, api
from odoo.exceptions import ValidationError

class Member(models.Model):
    _name = 'membership.member'
    _description = 'Membership Management'
    _inherits = {'res.partner': 'partner_id'}
    _order = 'membership_number asc'

    partner_id = fields.Many2one('res.partner', string='Partner', required=True, ondelete='cascade')
    membership_number = fields.Char(string='Membership Number', copy=False, readonly=True)
    join_date = fields.Date(string='Join Date', default=fields.Date.today())
    status = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('terminated', 'Terminated')
    ], string='Status', default='active')
    
    # share_capital_ids = fields.One2many('membership.share.capital', 'member_id', string='Share Capital')
    # mandatory_savings_ids = fields.One2many('membership.mandatory.savings', 'member_id', string='Mandatory Savings')
    # voluntary_savings_ids = fields.One2many('membership.voluntary.savings', 'member_id', string='Voluntary Savings')
    # savings_transaction_ids = fields.One2many('membership.savings.transaction', 'member_id', string='Savings Transactions')

    @api.model
    def create(self, vals):
        if 'membership_number' not in vals:
            vals['membership_number'] = self.env['ir.sequence'].next_by_code('membership.member') or '/'
        return super(Member, self).create(vals)

    def action_activate(self):
        if not self.membership_number:
            self.membership_number = self.env['ir.sequence'].next_by_code('membership.member') or '/'
        self.status = 'active'

    def action_deactivate(self):
        self.status = 'inactive'

    def action_terminate(self):
        self.status = 'terminated'


class Sequence(models.Model):
    _inherit = 'ir.sequence'

    is_membership_registration = fields.Boolean(string='Membership Registration')

    def _next(self):
        if self.is_membership_registration:
            self.ensure_one()
            if self._context.get('membership_registration_date'):
                date = fields.Date.from_string(self._context['membership_registration_date'])
                return self.next_by_date(date)
        return super(Sequence, self)._next()

class ShareCapital(models.Model):
    _name = 'membership.share.capital'
    _description = 'Share Capital'

    name = fields.Char(string='Name', required=True)
    amount = fields.Float(string='Amount', required=True)
    member_id = fields.Many2one('membership.member', string='Member')