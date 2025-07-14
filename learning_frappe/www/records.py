import frappe

def get_context(context):
    frappe.log_error("context",context)
    context.datas = frappe.get_all(
        'Jinja API',
        fields = ['full_name', 'phone', 'email', 'dob', 'age', 'salary'],
        order_by = 'dob desc',
        limit_page_length=10
    )