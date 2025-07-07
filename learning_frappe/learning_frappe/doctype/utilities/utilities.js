// Copyright (c) 2025, Brit and contributors
// For license information, please see license.txt

frappe.ui.form.on("Utilities", {
    refresh(frm) {

        ///////////////////////////////GET ROUTE////////////////////////////////////////

        frm.add_custom_button('Get Route', () => {
            let route = frappe.get_route()
            console.log(route);

            let name = route[2]
            frappe.call({
                method: 'learning_frappe.learning_frappe.doctype.utilities.utilities.get_info',
                args: {
                    name: name
                },
                callback: (res) => {
                    frappe.msgprint("Current Route:" + JSON.stringify(res.message))
                }
            })
        });

        ///////////////////////////////Format Date///////////////////////////////////////


        frm.add_custom_button("Format Date", () => {
            frappe.call({
                method: 'learning_frappe.learning_frappe.doctype.utilities.utilities.get_info',
                args: {
                    name: frm.doc.name
                },
                callback: (res) => {
                    if (res.message) {
                        let response = res.message
                        console.log(response);

                        let format_date = response.date ? frappe.format(response.date, { fieldtype: "Date" }) : "N/A";
                        let msg = `
                            <b>Record:</b>${response.Record}</br>
                            <b>Name:</b>${response.name}</br>
                            <b>Phone:</b>${response.phone}</br>
                            <b>Email:</b>${response.email}</br>
                            <b>Date:</b>${format_date}</br>
                        `;
                        frappe.msgprint(msg)
                    }
                }
            })
        })


        ///////////////////////////////Require///////////////////////////////////////


        frm.add_custom_button("Require", () => {
            frappe.require('/assets/js/Require.js', () => {
                show_alert_message()
            })
        })

        ///////////////////////////////Single Parameter///////////////////////////////////////

        frm.add_custom_button('Ping', () => {
            frappe.call('ping')
                .then((res) => {
                    frappe.msgprint(res)
                })
        })

        frm.add_custom_button('Single Param', () => {
            let a = 5;
            frappe.call('learning_frappe.learning_frappe.doctype.utilities.utilities.single_parameter', {
                a: a
            }).then((res) => {
                frappe.msgprint(`Result ${res.message}`)
            })

        })

        frm.add_custom_button('Single Param', () => {
            frappe.call('learning_frappe.learning_frappe.doctype.utilities.utilities.single_parameter', {
                role_profile: 'Admin'
            }).then((res) => {
                frappe.msgprint(`Result: ${res.message}`)
            })

        })

        ///////////////////////////////call with all options///////////////////////////////////////

        frm.add_custom_button('Calculate Total', () => {
            let a = 10;
            let b = 20;
            frappe.call({
                method: 'learning_frappe.learning_frappe.doctype.utilities.utilities.calculate_total',
                args: { a, b },
                freeze: true,
                freeze_message: "Please wait your calculations are loading....",
                callback: (res) => {
                    if (res.message) {
                        frappe.msgprint(`Total:${res.message}`)
                    }
                },
                error: (res) => {
                    frappe.msgprint("Error while calculating")
                    console.error(res)
                }
            })
        })


        ///////////////////////////////Get Doc in JS///////////////////////////////////////


        frm.add_custom_button('Get Doc', () => {
            frappe.db.get_doc('Utilities', null, { status: 'Close' })
                .then((doc) => {
                    console.log(doc);
                })
        })

        ///////////////////////////////Get List in JS///////////////////////////////////////

        frm.add_custom_button("Get List", () => {
            frappe.db.get_list('Utilities', {
                fields: ['name1', 'email'],
                // fields:["*"], 
                filters: {
                    status: 'Close',
                    // status:'Open'
                }
            }).then((res) => {
                console.log(res);
            })
        })

        ///////////////////////////////Get Value in JS///////////////////////////////////////
        frm.add_custom_button("Get Value", () => {
            // single value

            frappe.db.get_value('Utilities', frm.doc.name, 'name1')
                .then((r) => {
                    console.log(r.message.name1);

                })

            // multiple values

            frappe.db.get_value('Utilities', frm.doc.name, ['name1', 'email'])
                .then((r) => {
                    console.log(r.message.name1, r.message.email);
                })

            // Values with filter

            frappe.db.get_value('Utilities', { 'status': 'Open' }, 'email')
                .then((r) => {
                    console.log(r.message.email);
                })


        })

        //////////////////////////Insert Date with DB/////////////////////////////////

        frm.add_custom_button('Insert Date', () => {
            frappe.db.insert({
                'doctype': 'Utilities',
                'name1': 'Sparkie',
                'email': 'sparkietarrezz@gmail.com',
                'phone': '9489225774',
                'date': '2002-12-12',
                'status': 'Open'
            })
                .then((r) => {
                    console.log(r);
                })
        })

        //////////////////////////Count with DB/////////////////////////////////

        frm.add_custom_button('Data Count', () => {
            // ---> total count
            frappe.db.count('Utilities')
            // -- > with filters count
            frappe.db.count('Utilities', { filters: { status: 'Close' } })
                .then(count => {
                    console.log(count)
                })
        })

        //////////////////////////Delete DOC/////////////////////////////////

        frm.add_custom_button('Delete', () => {
            frappe.db.delete_doc('Utilities', frm.doc.name)
        })

        //////////////////////////EXISTS?/////////////////////////////////

        frm.add_custom_button('Data Exists?', () => {
            frappe.db.exists('Utilities', frm.doc.name)
                .then((res) => {
                    if (res) {
                        frappe.msgprint("Data Already Exists!")
                    } else {
                        frappe.msgprint('Not Exist!')
                    }
                })
        })

    },
});
