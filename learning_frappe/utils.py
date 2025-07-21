import frappe

def get_fullname(user):
    first, last = frappe.db.get_value("User", user, ["first_name", "last_name"])
    return f"{first or ''} {last or ''}".strip()

def format_currency(value, currency):
    return f"{currency} {float(value):,.2f}"
