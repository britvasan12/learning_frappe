frappe.listview_settings['Database API'] = {
    onload: function(listview) {
        listview.page.add_inner_button('Load Movies', function() {
            frappe.call({
                method: "learning_frappe.learning_frappe.doctype.database_api.database_api.random",
                callback: function(r) {
                    if (r.message) {
                        console.log(r.message);
                        
                    }
                }
            });
        });
    }
};