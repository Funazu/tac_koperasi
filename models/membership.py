from odoo import fields, models, api
from odoo.exceptions import ValidationError

class Member(models.Model):
    _name = 'membership.member'
    _description = 'Membership Member Koperasi'

    name =  fields.Char(string="Nama Member", required=True)


class MembershipFee(models.Model):
    _name = 'membership.fee'
    _description = 'Membership Fee'

    name = fields.Char(string='Name', required=True)
    amount = fields.Float(string='Amount', required=True)
    membership_type = fields.Selection([
        ('reguler', 'Reguler'),
        ('premium', 'Premium')
    ], string='Membership Type', required=True)
    # is_active = fields.Boolean(string='Active', default=True)


class MemberRegistration(models.Model):
    _name = 'membership.registration'
    _description = 'Member Registration'

    partner_id = fields.Many2one('res.partner', string='Partner', required=True, ondelete='cascade')
    registration_date = fields.Date(string='Registration Date', default=fields.Date.today())
    fee_id = fields.Many2one('membership.fee', string='Membership Fee')
    fee_amount = fields.Float(string='Fee Amount', compute='_compute_fee_amount', store=True)
    approved = fields.Boolean(string='Approved')

    @api.depends('fee_id')
    def _compute_fee_amount(self):
        for registration in self:
            registration.fee_amount = registration.fee_id.amount

    @api.onchange('fee_id')
    def _onchange_fee_id(self):
        if self.fee_id:
            self.fee_amount = self.fee_id.amount
        else:
            self.fee_amount = 0.0

    def action_approve(self):
        self.approved = True
        # Perform any other actions required upon approval

    def action_reject(self):
        self.approved = False
        # Perform any other actions required upon rejection

    @api.constrains('fee_id')
    def _check_fee_id(self):
        if not self.fee_id:
            raise ValidationError("Membership Fee is required.")
