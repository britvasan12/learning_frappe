// Copyright (c) 2025, Brit and contributors
// For license information, please see license.txt

frappe.ui.form.on("Show", {
	refresh() {
        frappe.msgprint('Hello There!')
	},

    validate(frm){
        if(frm.doc.movie){
            frm.set_value('base_ticket_price', 200);
            frm.set_df_property('base_ticket_price', 'read_only',1)
        }
        else{
            frm.set_value('base_ticket_price', 0);
        }
    }
});
