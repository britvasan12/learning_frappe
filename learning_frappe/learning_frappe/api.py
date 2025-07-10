import frappe
import random
from datetime import datetime

@frappe.whitelist()
def push_leave_update():
    leave_count = random.randint(1, 4)
    

    data = {
        'label': frappe.utils.nowtime(),
        'points': leave_count
    }
    frappe.log_error("Scheduler", f"{data}")
    frappe.publish_realtime('leave_count_realtime', data)



# def push_leave_update():
#     current_time = datetime.datetime.now().strftime("%H:%M:%S")
#     leave_count = random.randint(1, 4)

#     frappe.publish_realtime(
#         event="leave_count_realtime",
#         message={
#             "label": current_time,
#             "points": leave_count
#         }
#     )