// Copyright (c) 2025, Brit and contributors
// For license information, please see license.txt

frappe.ui.form.on("Demo Total", {

    //////////  Setup  ///////////                                                    Working

    setup: frm => {
        frm.set_value({
            'first_name': 'Brit',
            'last_name': "R"
        }).then(() => {
            const fullName = `${frm.doc.first_name} ${frm.doc.last_name}`;
            frm.set_value('full_name', fullName)

            frappe.msgprint("Values are setted")
        })
    },

    //////////  before_load  ///////////                                              Working  

    before_load: frm =>{
        frm.set_value('first_name', 'Brit')
        frm.set_df_property('first_name', 'read_only', 1)
        frm.set_df_property('count', 'reqd', 1)
        frappe.msgprint("Before Load Event")
    },

    //////////  onload_post_render  ///////////                                       Working

    onload_post_render: frm =>{
        frappe.msgprint("After the form is loaded and rendered Event")
        frm.set_value('first_name', 'Britto')
        frm.set_df_property('first_name', 'read_only', 1)
        frm.set_df_property('count', 'reqd', 1)
    },

    // //////////  onload  ///////////                                       Working   

    onload: frm =>{
        frm.set_value('first_name', 'Britvasan')
        frappe.msgprint("Onload Event")
    },


    // //////////  validate  ///////////                                       Working   

    validate: frm =>{
        if(!frm.doc.status){
            frappe.throw("Please Choose the Select Field")
        }
    },

    // //////////  refresh  ///////////                                       Working   

    refresh: frm => {
        if (frm.doc.first_name) {
            frm.set_value('description', 'First Name field is filled!')
            if (frm.doc.description) {
                frm.set_value('total', '200')
            }
        }
    },

    // //////////  before_save  ///////////                                       Working   


    before_save: (frm) => {
        if (frm.doc.first_name) {
            frm.set_value('description', 'First Name field is filled!')
            if (frm.doc.description) {
                console.log("works")
                frm.set_value('total', '200')
                frappe.msgprint("Event Triggered!")
            }
        }

    },

    // //////////  after_save  ///////////                                       Working 

    after_save: frm =>{
        if(frm.doc.first_name){
            frm.set_value('count', 10).then(()=>{
                frappe.msgprint("After Save Triggered")
            })
        }
    },

    // //////////  before_submit  ///////////                                    Working 

    before_submit: frm =>{
        if(!frm.doc.last_name){
            frappe.throw("Before Submit event triggered --> last name is missing!!")
        }
    },

    // //////////  on_submit  ///////////                                    Working 

    on_submit: frm => {
        frm.doc.full_name = 'Britvasan'
        frappe.msgprint("On Submit event triggered")
    },

    // //////////  before_cancel  ///////////                                    Working 

    before_cancel: frm => {
        frappe.throw("Do you want to cancel this Document!?")
    },

    // //////////  after_cancel  ///////////                                    Working 

    after_cancel: frm =>{
        frappe.msgprint("Successfully Cancelled!")
        frappe.throw("Successfully Cancelled!")
    },

    // //////////  before_discard  ///////////                                    Not Working 

    before_discard : (frm) => {
        if(frm.doc.__unsaved){
            frappe.msgprint("Plz save the doc")
        }
    },

    // //////////  after_discard  ///////////                                    Not Working 

    after_discard(frm) {
        frappe.throw("Do you want to Discard Changes?")
        console.log("About to discard unsaved changes");
    },

    after_discard(frm) {
        console.log("Form discarded, old data restored");
    },

    // //////////  timeline_refresh  ///////////                                    Working

        timeline_refresh: frm => {
        let comment_count = 0;

        frm.timeline.timeline_items.forEach(item => {
            if (item.content_type === "Comment") {
                comment_count++;
            }
        });

        frappe.call({
                method: "frappe.desk.form.utils.add_comment",
                args: {
                    reference_doctype: frm.doctype,
                    reference_name: frm.docname,
                    content: "This is a test comment added programmatically.",
                    comment_email: frappe.session.user,
                    comment_by: frappe.user.full_name()
                },
                callback: function (response) {
                    frappe.msgprint("Comment added successfully!");
                }
            });
    },

    timeline_refresh: function(frm) {
        frappe.show_alert({
            message: "Timeline was refreshed!",
            indicator: "blue"
        });
    },

    // //////////  field_name  ///////////                                    Working

    first_name: frm=>{
        frm.set_value('description', `Auto Generated text for ${frm.doc.first_name}`)
        .then(()=>{
            frappe.msgprint('Text is Added')
        })
    },



    last_name: frm =>{
        const fullName = `${frm.doc.first_name} ${frm.doc.last_name}`
        frm.set_value('full_name', fullName)
        .then(()=>{
            frappe.msgprint(`Full Name added as:${fullName}`)
        })
    },



    // if (frappe.user_roles.includes('System Manager')){
    //         frm.enable_save()
    //     }else{
    //         frm.disable_save()
    //     }

    // refresh: function (frm) {
    //     // if (frm.is_new()) {
    //     //     frm.add_custom_button('Click me', () => console.log('Clicked custom button'))
    //     // }

    //     if(!frm.doc.fullname){
    //         frm.set_intro('Please add a Fullname!', 'red')
    //     }
    // }
        
    // status: frm =>{
    // frm.set_df_property('status', 'options',['','New', 'Old'])
    // is_allowed = frappe.user_roles.includes("New User");
    // frm.toggle_enable(['status'], is_allowed)
    // frm.toggle_reqd('full_name', frm.doc.status==='Open');
    // }

    // refresh: function(frm) {
    //     frm.add_custom_button("Calculate total", function() {
    //         frappe.call({
    //             method: 'learning_frappe.learning_frappe.doctype.demo_total.demo_total.calculate_total',
    //             args: {
    //                 count: frm.doc.count,
    //                 price: frm.doc.price
    //             },
    //             callback: function (r) {
    //                 if (r.message) {
    //                     frm.set_value('total', r.message)
    //                     frappe.msgprint(`Total Amount:${r.message}`)
    //                 }
    //             }
    //         })
    //     })
    // }
});


