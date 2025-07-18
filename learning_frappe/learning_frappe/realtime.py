import frappe

def _room(board):
    return f"kanban_{board}"

def notify_task(doc, method=None):
    payload = {
        "task": doc.name,
        "board": doc.board,
        "status": doc.status,
        "assignee": doc.assignee,
        "by": frappe.session.user
    }

    frappe.publish_realtime(
        event = "task_update",
        message = payload,
        room  = _room(doc.board)
    )

# def notify_comment(doc, method=None):
#     task = frappe.db.get_value("Task Comment", doc.name, "parent")
#     board = frappe.db.get_value("Task", task, "board")

#     frappe.publish_realtime(
#         event = "new_comment",
#         message = {
#             "task": task, 
#             "comment_html":frappe.render_template("learning_frappe/templates/includes/comment.html",{"c":doc}),
#         },
#         room = _room(board)
#     )

