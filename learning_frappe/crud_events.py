import frappe

def check_private_event_permissions(doc, method=None):
    if doc.event_type == "Private" and frappe.session.user != "Administrator":
        frappe.throw("❌ Only Administrator can create Private Events!")
