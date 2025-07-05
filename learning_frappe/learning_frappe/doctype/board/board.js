// Copyright (c) 2025, Brit and contributors
// For license information, please see license.txt

frappe.ui.form.on("Board", {
	refresh(frm) {
        frm.add_custom_button("Open Board", () => {
            frappe.set_route('board-view', frm.doc.name);
        });
    }
});
