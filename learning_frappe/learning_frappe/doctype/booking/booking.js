// Copyright (c) 2025, Brit and contributors
// For license information, please see license.txt

frappe.ui.form.on("Booking", {
	onload: function (frm) {
		frappe.msgprint("Welcome To Booking Page!")
	},

	before_save: function(frm){
		if(!frm.doc.booking_time && !frm.doc.show){
			frappe.throw('How Can you Book a ticket without mentioning a time and show?')
		}
	},

	after_save: function (frm) {
		frappe.msgprint('Document Saved')
	},

	refresh: function (frm) {
		frm.add_custom_button('Message', () => {
			frm.set_value('checked_in', 1)
			frappe.msgprint('Button is Clicked!')
		})
	}

});

////////////////Child table Calculation////////////////////

frappe.ui.form.on("Booked Seat", {
	price(frm, cdt, cdn) {
		calculate_total(frm, cdt, cdn);
	},
	ticket_count(frm, cdt, cdn) {
		calculate_total(frm, cdt, cdn);
	}
});

function calculate_total(frm, cdt, cdn) {
	let row = locals[cdt][cdn];
	row.total_amount = (row.ticket_count) * (row.price);
	frm.refresh_field('booked_seat');
}




// frappe.ui.form.on("Booked Seat", function(){
// 	before_save: (frm)=>{
// 		frm.add_custom_button("Calculate total", ()=>{
// 			frappe.call({
// 				method: 'learning_frappe.learning_frappe.doctype.booking.booking.calculate_total',
// 				args:{
// 					ticket_count: frm.doc.ticket_count,
// 					price: frm.doc.price
// 				},
// 				callback: function(r){
// 					if(r.mesaage){
// 						frm.set_value('total',total_amount)
// 						frappe.msgprint(`Total Amount:${r.mesaage}`)
// 					}
// 				}
// 			})
// 		})
// 	}
// });


