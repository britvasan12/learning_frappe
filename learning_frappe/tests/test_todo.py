import frappe
import unittest

class TestToDo(unittest.TestCase):
    def test_create_todo(self):
        todo = frappe.get_doc({
            "doctype": "ToDo",
            "description": "Test Description"
        })
        todo.insert(ignore_permissions=True)

        self.assertIsNotNone(todo.name)

        self.assertEqual(todo.status, "Open")


# bench --site learn.local run-tests --app learning_frappe --module learning_frappe.tests.test_todo

# bench --site learn.local run-tests --app learning_frappe