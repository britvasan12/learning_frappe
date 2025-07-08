// Copyright (c) 2025, Brit and contributors
// For license information, please see license.txt

frappe.ui.form.on("Dialog API", {
    refresh(frm) {
        // Create Dialog form via code

        // let D = new frappe.ui.Dialog({
        //     title: 'Enter Details',
        //     fields: [
        //         {
        //             label: 'Full Name',
        //             fieldname: 'full_name',
        //             fieldtype: 'Data'
        //         },
        //         {
        //             label: 'Email',
        //             fieldname: 'email',
        //             fieldtype: 'Data'
        //         },
        //         {
        //             label: 'Phone',
        //             fieldname: 'phone',
        //             fieldtype: 'Data'
        //         },
        //         {
        //             label: 'Age',
        //             fieldname: 'age',
        //             fieldtype: 'Int'
        //         }
        //     ],
        //     size: 'small',
        //     primary_action_label: 'Save',
        //     primary_action(values) {
        //         console.log(values);
        //         D.hide();
        //     }
        // })
        // D.show();

        // frappe.msgprint(__('Document Opened Successfully!'))

        // --------------------------------------------------------------------------------------------

        // frappe.msgprint({
        //     title:__('Remainder'),
        //     indicator:'grey',
        //     message:__('Remainder Message!?')
        // })
        // -------------------------------------------------------------------------------------------
        // frappe.msgprint({
        //     title: __('Confirm'),
        //     message: __('Are you sure want to proceed!'),
        //     primary_action_label: 'Yes',
        //     primary_action: {
        //         action(values) {
        //             frappe.set_route('List', 'Dialog API', 'List')
        //             console.log(values)
        //         }
        //     },
        // })

        // -------------------------------------------------------------------------------------------
        // SERVER ACTION
        // Its working using dialog box proceed to submit the cur doc using frm.save() 
        // its basic method without using server and client action here Method 1.

        // frm.add_custom_button('Confirm', () => {
        //     if (!frm.doc.name) {
        //         frappe.msgprint('Please save the document before proceeding.');
        //         return;
        //     }

        //     frappe.msgprint({
        //         title: __('Confirmation'),
        //         message: __('Sure you want to proceed!'),
        //         primary_action: {
        //             label: 'Proceed',
        //             action: () => {
        //                 frappe.msgprint('Submitting document...');
        //                 frm.save('Submit')
        //             }
        //         }
        //     });
        // });

        // -------------------------------------------------------------------------------------------
        // SERVER ACTION
        // The same thing we can with frappe.confirm method with server action call
        // Its method 2 using dialog proceed to submit the cur doc!
        // We cant do this inside the frappe.msgprint it hits different 

        // frm.add_custom_button('Confirm', () => {
        //     if (!frm.doc.name) {
        //         frappe.msgprint('Please save the document before proceeding.');
        //         return;
        //     }

        //     frappe.confirm(
        //         'Sure you want to proceed?',
        //         () => {
        //             frappe.call({
        //                 method: 'learning_frappe.learning_frappe.doctype.dialog_api.dialog_api.confirm_data',
        //                 args: {
        //                     name: frm.doc.name
        //                 },
        //                 callback: (r) => {
        //                     if (r.message) {
        //                         frappe.msgprint(r.message);
        //                         frm.reload_doc();
        //                     }
        //                 }
        //             });
        //         }
        //     );
        // });
        // --------------------------------------------------------------------------------------------
        // SERVER ACTION
        // This method works but without submitted notification
        // after refresh the form the doc has submitted!?

        // frm.add_custom_button('Confirm', () => {
        //     if(!frm.doc.name){
        //         frappe.msgprint('Please save the document before proceeding.')
        //         return;
        //     }

        //     frappe.msgprint({
        //         title: __('Confirmation'),
        //         message: __('Sure you want to proceed!'),
        //         primary_action: {
        //             label: 'Proceed',
        //             server_action: 'learning_frappe.learning_frappe.doctype.dialog_api.dialog_api.confirm_data',
        //             args:{
        //                 name: frm.doc.name
        //             },
        //             callback:(r)=>{
        //                 if(r.message){
        //                     frappe.msgprint(r.message);
        //                     frm.reload_doc()
        //                 }
        //             }
        //         }
        //     })

        // })

        // -------------------------------------------------------------------------------------------
        // CLIENT ACTION - Not working
        // frm.add_custom_button('Show Alert',()=>{
        //     frappe.msgprint({
        //         title:__('Alert'),
        //         message:__('This is alert Message'),
        //         primary_action:{
        //             label:'Proceed',
        //             client_action:'show_custom_alert'
        //         } 

        //     })
        // })

        // -------------------------------------------------------------------------------------------

        // frm.add_custom_button('Prompt', () => {
        // FOR SINGLE FIELDS

        // frappe.prompt('Full Name', ({value})=> console.log(value))
        // frappe.prompt('Full Name', console.log, 'Enter Full Name', 'Submit')

        // FOR MULTIPLE FIELDS

        // frappe.prompt([
        //     {
        //         label: 'Full Name',
        //         fieldname: 'full_name',
        //         fieldtype: 'Data'
        //     },
        //     {
        //         label: 'Email',
        //         fieldname: 'email',
        //         fieldtype: 'Data'
        //     }
        // ], (values) => {
        //     console.log(values.full_name, values.email)
        // })  

        // FOR Update the field values using prompt

        // frappe.prompt([
        //     {
        //         label: 'Status',
        //         fieldname: 'status',
        //         fieldtype: 'Select',
        //         options: ['', 'Open', 'In Progress', 'Closed'],
        //         reqd: 1
        //     }
        // ],
        //     (values) => {
        //         frappe.db.set_value('Dialog API', frm.doc.name, 'status', values.status)
        //             .then(() => {
        //                 frappe.msgprint('Status Updated to:' + values.status)
        //                 frm.reload_doc()
        //             })

        //         //frm.set_value also we can use but its works only on editable document
        //         // Not in submitted doc
        //         // but frappe.db.set_value works even if the document as submitted
        //         // not opened also anywhere we can access 
        //         frm.set_value('status', values.status)
        //         frm.save()
        //     },
        //     'Update Status',
        //     'Set')

        // })
        // --------------------------------------------------------------------------------------------
        // Yes or No methods with some operations!!

        // frm.add_custom_button('Confirm', () => {
        //     frappe.confirm('Are you sure you want to proceed?',
        // If Yes
        //         () => {
        //             frappe.call({
        //                 method: 'learning_frappe.learning_frappe.doctype.dialog_api.dialog_api.success',
        //                 args: {
        //                     name: frm.doc.name
        //                 },
        //                 callback:(r)=>{
        //                     frappe.msgprint(`Message Type: ${r.message}`)
        //                     frm.reload_doc();
        //                 }
        //             })
        //         }, 
        // If No
        //          () => {
        //             frappe.call({
        //                 method: 'learning_frappe.learning_frappe.doctype.dialog_api.dialog_api.failure',
        //                 args: {
        //                     name: frm.doc.name
        //                 },
        //                 callback:(r)=>{
        //                     frappe.msgprint(`Message Type: ${r.message}`)
        //                     frm.reload_doc();
        //                 }
        //             })
        //         })
        // })  
        // -------------------------------------------------------------------------------------------
        // Warning kind of Notification works but cancel not working

        // frm.add_custom_button('Warn', () => {
        //     frappe.warn("Do you want to proceed further!?",
        //         "There are unsaved changes in on this page!",
        //         () => {
        //             frm.set_value('status', 'In Progress')
        //             frappe.msgprint('You clicked Continue: Status set to In progress')
        //         },
        //         'Continue',
        //         () => {
        //             frappe.msgprint('Cancel clicked');
        //             frm.reload_doc();
        //         }
        //     )
        // })
        // -------------------------------------------------------------------------------------

        // frm.add_custom_button('Alert',()=>{
        // frappe.show_alert('Hi, You have Message',5)

        // setTimeout(()=>{
        //     frappe.show_alert('Hi, You have Message',5)
        // },100)    

        // setInterval(()=>{
        //     frappe.show_alert('Hi, You have Message',5)
        // },1000) 

        // frappe.show_alert({
        //     message:__('You got a message',5),
        //     indicator: 'green'
        // },5)

        // })
        // --------------------------------------------------------------------------------
        // Progress Bar
        // frm.add_custom_button("Progress",()=>{
        //     frappe.show_progress('Loading.....',25,100,'Wait a minute!')
        // })
        // -----------------------------------------------------------------------------------
        // Create a new document in dialog API along with frappe.prompt!

        // frm.add_custom_button('New Doc', () => {
        //     frappe.prompt([
        //         {
        //             label: 'Full Name',
        //             fieldname: 'full_name',
        //             fieldtype: 'Data'
        //         },
        //         {
        //             label: 'Email',
        //             fieldname: 'email',
        //             fieldtype: 'Data'
        //         },
        //         {
        //             label: 'Phone',
        //             fieldname: 'phone',
        //             fieldtype: 'Data'
        //         },
        //         {
        //             label: 'Age',
        //             fieldname: 'age',
        //             fieldtype: 'Int'
        //         },
        //         {
        //             label: 'Status',
        //             fieldname: 'status',
        //             fieldtype: 'Select',
        //             options: 'Open\nIn Progress\nClosed'
        //         }
        //     ],
        //         (values) => {
        //             let doc = frappe.model.get_new_doc('Dialog API');
        //             doc.full_name = values.full_name
        //             doc.email = values.email
        //             doc.phone = values.phone
        //             doc.age = values.age
        //             doc.status = values.status
        //             frappe.set_route('Form', 'Dialog API', doc.name)
        //         },
        //         "New Dialog API",
        //         "Create"
        //     );
        // })
        // -----------------------------------------------------------------------------------
    },
});


