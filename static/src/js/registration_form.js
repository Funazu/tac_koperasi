odoo.define('tac_koperasi.membership_registration_form', function(require) {
    'use strict';

    var ajax = require('web.ajax');

    $(document).ready(function() {
        var $form = $('#form_membership_registration');
        var $membershipAmountField = $form.find('input[name="membership_amount"]');
        var $membershipTypeField = $form.find('input[name="membership_type"]');
        var $feeSelectField = $form.find('select[name="fee_id"]');

        function updateMembershipFields() {
            var feeId = $feeSelectField.val();
            if (feeId) {
                ajax.jsonRpc('/membership/fee/get', 'call', {'fee_id': feeId}).then(function(result) {
                    if (result) {
                        $membershipAmountField.val(result.amount);
                        $membershipTypeField.val(result.type);
                    } else {
                        $membershipAmountField.val('');
                        $membershipTypeField.val('');
                    }
                });
            } else {
                $membershipAmountField.val('');
                $membershipTypeField.val('');
            }
        }

        $feeSelectField.on('change', function() {
            updateMembershipFields();
        });

        updateMembershipFields();
    });
}); 