// Copyright (c) 2025, Brit and contributors
// For license information, please see license.txt

frappe.ui.form.on("Form API", {
    // checked: function (frm) {
    //     frappe.msgprint('Checked field triggered!');
    //     frm.add_custom_button("FRM Trigger", () => {
    //         frm.trigger('checked');
    //     })
    // },



    // refresh(frm) {

    // SET VALUE

    // frm.set_value('age',23).then(()=>{
    //     frm.reload_doc();
    //     frm.set_value('age',20)
    // })



    // REFRESH

    // frm.add_custom_button('Refresh',()=>{
    //     frappe.msgprint("Refreshed!")
    // })



    // SAVE - SUBMIT, CANCEL, UPDATE

    // frm.add_custom_button('Custom Save',()=>{
    //     frm.set_value('full_name','Brit')
    //     frm.save()
    //     frappe.show_alert({
    //         message:"Save Button Clicked",
    //         indicator:"Yellow"
    //     }, 5)
    // }),

    // frm.add_custom_button('Custom Submit',()=>{
    //     frm.set_value('age','22')
    //     frm.save('Submit')
    //     frappe.show_alert({
    //         message:"Submit Button Clicked",
    //         indicator:"Blue"
    //     }, 5)
    // }),

    // frm.add_custom_button('Custom Cancel',()=>{
    //     frm.set_value('email','Brit')
    //     frm.save('Cancel')
    //     frappe.show_alert({
    //         message:"Cancel Button Clicked",
    //         indicator:"Red"
    //     }, 5)
    // }),

    // frm.add_custom_button('Custom Update',()=>{
    //     frm.set_value('email','Brit@gmail.com')
    //     frm.save('Update')
    //     frappe.show_alert({
    //         message:"Update Button Clicked",
    //         indicator:"green"
    //     }, 5)
    // })
    // },

    // ENABLE and DISABLE SAVE

    // checked(frm){
    //     if(frm.doc.checked){
    //         frm.enable_save()

    //     }else{
    //         frm.disable_save()
    //     }
    // }

    refresh(frm) {
        // EMAIL DOC

        // frm.add_custom_button('Email',()=>{
        //     frm.email_doc()
        //     frappe.show_alert('Email Doc Clicked')
        // })

        // Works on submit only not in save 
        // RELOAD DOC

        // frm.add_custom_button('Reload Doc',()=>{               
        //     frm.reload_doc()
        //     frappe.show_alert('Reloaded')
        // }),

        // REFRESH FEILDS

        // frm.add_custom_button('Refresh Fields',()=>{
        //     frm.refresh_fields('age')
        //     frappe.msgprint("R")
        // })

        // DIRTY

        // frm.add_custom_button('Dirty?',()=>{
        //     if(!frm.doc.age){
        //         frappe.show_alert('Dirty')
        //     }else{
        //         frappe.show_alert('Not Dirty')
        //     }
        // })


        // IS NEW

        // frm.add_custom_button("New?",()=>{
        //     if(frm.is_new()){
        //         frappe.show_alert("New Form")
        //     }else(
        //         frappe.show_alert("Not a New Form")
        //     )
        // })

        // SET INTRO

        // if (!frm.doc.age) {
        //     frm.set_intro('Age is Missing', 'red')
        // }

        // // CUSTOM BUTTON
        //     frm.add_custom_button('Custom',()=>{
        //         frappe.set_route('List', 'Form API', 'List')
        //     })

        // MULTIPLE CUSTOM BUTTON

        // frm.add_custom_button('New', () => {
        //     frappe.set_route('Form','Form API', 'Form API-001')

        //     // frappe.new_doc('Form API')
        // }, 'Action');

        // frm.add_custom_button('Edit', () => {
        //     frappe.set_route('List/Booking')
        // }, 'Action');

        // frm.add_custom_button('Delete', () => {
        //     frappe.set_route('Form/Booking/Booking-002')
        // }, 'Action');

        // frm.add_custom_button("Remove",()=>{
        //     frm.remove_custom_button('New', 'Action')
        // })

        // frm.add_custom_button("Remove All",()=>{
        //     frm.clear_custom_buttons()
        // })

        // SET DF PROPERTY

        // frm.add_custom_button('DF',()=>{
        //     frm.set_df_property('full_name', 'read_only', 1)
        // })

        // TOGGLE ENABLE

        // frm.add_custom_button('Button1',()=>{
        //     frm.toggle_enable('status', frm.doc.checked==1)
        // })

        // TOGGLE REQUIRED

        // frm.add_custom_button("Required",()=>{
        //     frm.toggle_reqd('email', frm.doc.full_name)
        // })

        // frm.add_custom_button('Display',()=>{
        //     const hasName = frm.doc.full_name;
        //     frm.toggle_display('age',hasName)
        // }

        

    }
        

});
