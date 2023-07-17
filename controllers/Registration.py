from odoo import http, fields
from odoo.http import request
from odoo.tools import float_round

class MemberRegistration(http.Controller):

    # @http.route('/membership/registration', type='http', auth='public', website=True)
    # def index(self):
    #     membership_fee = request.env['membership.fee'].sudo().search([])
    #     return request.render('tac_koperasi.membership_registration_form')

    @http.route('/member/registration', auth='public', website=True)
    def membership_registration(self, **post):
        fees = request.env['membership.fee'].search([])  # Mendapatkan semua biaya keanggotaan
        if request.httprequest.method == 'POST':
            # Proses data pendaftaran anggota yang dikirim melalui formulir
            # Ambil data dari post parameter
            partner_name = post.get('name')
            partner_email = post.get('email')
            partner_phone = post.get('phone')
            # fee_id = post.get('fee_id')
            # membership_amount = post.get('membership_amount')
            # membership_type = post.get('membership_type')
            # ...
            
            # Lakukan validasi data pendaftaran anggota
            
            # Buat partner baru
            partner = request.env['res.partner'].create({
                'name': partner_name,
                'email': partner_email,
                'phone': partner_phone
                # ...
            })
            
            # Buat pendaftaran anggota dengan memilih biaya keanggotaan yang sesuai
            member_registration = request.env['membership.registration'].create({
                'partner_id': partner.id,
                'registration_date': fields.Date.today(),
                # ...
            })
            
            # Lakukan tindakan lain yang diperlukan
            
            # Redirect ke halaman konfirmasi pendaftaran anggota
            return request.redirect('/membership/registration/success')
        
        # Render tampilan formulir pendaftaran anggota dengan pilihan biaya keanggotaan
        return http.request.render('tac_koperasi.membership_registration_form', {
            'fees': fees,
        })


    @http.route('/membership/fee/get', type='json', auth='public')
    def get_membership_fee(self, fee_id=None, **kwargs):
        if fee_id:
            fee = request.env['membership.fee'].sudo().browse(int(fee_id))
            if fee:
                return {
                    'amount': float_round(fee.amount, precision_digits=2),
                    'type': fee.membership_type,
                }
        return False