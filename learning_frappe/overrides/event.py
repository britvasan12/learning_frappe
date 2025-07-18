import frappe
from frappe.model.document import Document

class CustomEvent(Document):
    def before_save(self):
        self.custom_alert()

    def custom_alert(self):
        frappe.msgprint("⚠️ This is a custom method inside Event override.")
