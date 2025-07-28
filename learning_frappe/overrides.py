import frappe

def successful_login(login_manager):
    frappe.msgprint(f"Welcome back {frappe.session.user}!")


def clear_user_cache(login_manager):
    user = frappe.session.user
    frappe.cache().hdel("user_profile", user)
    frappe.logger().info(f"User {user} logged out and cache cleared")

    