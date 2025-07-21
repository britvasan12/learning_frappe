import frappe

def before_migrate():
    print("🔧 BEFORE MIGRATE: Preparing for schema changes...")

def after_migrate():
    print("✅ AFTER MIGRATE: Migration finished successfully.")