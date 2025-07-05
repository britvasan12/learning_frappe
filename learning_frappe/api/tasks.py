import frappe

@frappe.whitelist(allow_guest=True)
def create_task(api_key, board, subject, description=None):
    frappe.only_for("Integration User")
    doc = frappe.get_doc({
        "doctype":"Task",
        "board":board,
        "subject":subject,
        "description":description,
        "status":"Backlog"
    })

    doc.insert(ignore_permissions=True)
    return {"name":doc.name}

@frappe.whitelist()
def get_tasks(board):
    tasks = frappe.get_all("Task", filters={"board": board}, fields=[
        "name", "subject", "status", "assignee", "priority", "due_date"
    ])
    return tasks