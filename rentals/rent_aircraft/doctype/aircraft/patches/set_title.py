import frappe

def execute():
    aircrafts = frappe.db.get_all("Aircraft", pluck="name")
    for a in aircrafts:
        aircraft = frappe.get_doc("Aircraft", a)
        aircraft.set_title()
        aircraft.save()

        frappe.db.commit()