import frappe

def personal_note_query(user):
    if not user:
        user = frappe.session.user
    
    # only show notes created by the current user
    return "`tabPersonal Notes`.owner = {user}".format(user=frappe.db.escape(user))

def event_has_permission(doc, user=None, permission_type=None):
    if not user:
        user = frappe.session.user

    # Rule 1: Anyone can read public events
    if permission_type == "read" and doc.event_type == "Public":
        return True

    # Rule 2: Only owner can write
    if permission_type == "write" and doc.owner == user:
        return True

    # Others - no access
    return False