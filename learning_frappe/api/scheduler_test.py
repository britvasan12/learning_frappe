import frappe
import random
from frappe.utils import now

# def daily_task():
#     frappe.log_error(f"Daily Task Triggered! at {now()}", "Scheduler Log")
#     print("Daily Task ran")

# def hourly_task():
#     frappe.log_error("Hourly Task Triggered!", "Scheduler Log")


# @frappe.whitelist()
# def push_sales_data():
#     data = {
#         "label": now().split(" ")[1][:5],  # e.g., "14:32"
#         "points": random.randint(1,10)
#     }
#     frappe.log_error("Realtime Sales Push", f"{data}")
#     frappe.publish_realtime("sales_realtime_event", data)


# @frappe.whitelist()
# def send_test_record():

#     age = random.randint(18,25)
#     full_name = 'Brit'

#     doc = frappe.get_doc({
#         'doctype': 'Test',
#         'full_name': full_name,
#         'age': age
#     })

#     doc.insert(ignore_permissions = True)
#     frappe.db.commit()

#     frappe.log_error("Test Scheduler", f"Created Test record: {full_name}, Age: {age}")