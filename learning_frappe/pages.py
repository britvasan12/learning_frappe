import frappe


def custom_404_context(context):
    context.error_title = "Oops! Page not found."
    context.message = "Check The URL!"
    return context


