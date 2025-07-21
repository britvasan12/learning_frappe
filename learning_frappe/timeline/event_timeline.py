import frappe
from frappe.utils import now

def event_timeline(doctype, docname):
    return [
        {
            "creation": frappe.utils.now(),
            "template": "learning_frappe.templates.includes.event_custom_log",  
            "template_data": {
                "title": "Test Event",
                "description": "This is a custom log in the timeline."
            },
        }
    ]
