// Copyright (c) 2025, Brit and contributors
// For license information, please see license.txt

frappe.ui.form.on("Student Mark", {
    student_name: (frm) => {
        frm.set_df_property('marks', 'reqd', 1)
        if (!frm.doc.subject) {
            frm.set_intro('Please fill the subject below!', 'red')
            frm.set_df_property('subject', 'reqd', 1)
        }
    },

    marks: frm => {
        if (!frm.doc.marks && frm.doc.marks !== 0) {
            frappe.throw('Marks cannot be empty')
        } else if (frm.doc.marks >= 35) {
            frm.set_value('status', 'Pass')
        } else {
            frm.set_value('status', 'Fail')
        }
    },

    refresh: frm => {
        frm.add_custom_button("Submit to server", () => {
            frappe.call({
                method: 'learning_frappe.learning_frappe.doctype.student_mark.student_mark.student_data',
                args: {
                    name: frm.doc.name
                },
                callback: (r) => {
                    d = r.message
                    msg = (`
                        Record Name: ${d.name}</br>
                        Student Name: ${d.student_name}</br>
                        Subject: ${d.subject}</br>
                        Marks: ${d.marks}</br>
                        Status: ${d.status}</br>
                    `);

                    frappe.msgprint(msg);
                }
            })
        })
    }
});
