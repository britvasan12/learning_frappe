// Copyright (c) 2025, Brit and contributors
// For license information, please see license.txt

frappe.ui.form.on("Booked Seat", {
	////////////////{}_on_form_rendered //////////////////////                      Working

	// booked_seat_on_form_rendered: (frm, cdt, cdn) =>{
	// 	frappe.msgprint("Child Row is Opened!")

	// 	let row = locals[cdt][cdn]
	// 	if(row.ticket_count && row.price){
	// 		row.total_amount = row.ticket_count * row.price
	// 		frm.refresh_field('booked_seat')
	// 	}
	// },
	

	////////////////{field_name}_on_form_rendered ///////-> Need to update child doctype name           Working

	before_booked_seat_remove: (frm, cdt, cdn)=>{

		let row = locals[cdt][cdn]

		if(row.ticket_count > 2){
			frappe.throw("Can't Remove")
		}else{
			frappe.msgprint("Removed")
		}

	},

	////////////////{field_name}_add ///////-> Need to update child doctype name           Working

	// booked_seat_add: (frm, cdt, cdn) =>{
	// 	let row = locals[cdt][cdn]
	// 	frappe.msgprint("New Row Added")

	// 	row.ticket_count = 2
	// 	row.price = 200
	// 	frm.refresh_fields('booked_seat')
	// },

	////////////////{field_name}_remove ///////-> Need to update child doctype name           Working

	// booked_seat_remove: (frm, cdt, cdn)=>{
	// 	let row = locals[cdt][cdn]
	// 	frappe.msgprint("Task Removed")
	// },

	///////////////{field_name}_move ///////-> Need to update child doctype name           Working

	// booked_seat_move: (frm, cdt, cdn)=>{
	// 	let row = locals[cdt][cdn]
	// 	frappe.msgprint("Task Moved")
	// }

	///////////////form_render///////-> Need to update child doctype name           Working

	// form_render: (frm)=>{
	// 	frappe.msgprint("Child table Opened as Form View For Access fields!!")
	// }

	// onload: function (frm) {
	// 	frappe.msgprint("Welcome To Booking Page!")
	// },

	// before_save: function(frm){
	// 	if(!frm.doc.booking_time && !frm.doc.show){
	// 		frappe.throw('How Can you Book a ticket without mentioning a time and show?')
	// 	}
	// },

	// after_save: function (frm) {
	// 	frappe.msgprint('Document Saved')
	// },

	// refresh: function (frm) {
	// 	frm.add_custom_button('Message', () => {
	// 		frm.set_value('checked_in', 1)
	// 		frappe.msgprint('Button is Clicked!')
	// 	})
	// }

});

////////////////Child table Calculation////////////////////

// frappe.ui.form.on("Booked Seat", {
// 	price(frm, cdt, cdn) {
// 		calculate_total(frm, cdt, cdn);
// 	},
// 	ticket_count(frm, cdt, cdn) {
// 		calculate_total(frm, cdt, cdn);
// 	}
// });

// function calculate_total(frm, cdt, cdn) {
// 	let row = locals[cdt][cdn];
// 	row.total_amount = (row.ticket_count) * (row.price);
// 	frm.refresh_field('booked_seat');
// }




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


