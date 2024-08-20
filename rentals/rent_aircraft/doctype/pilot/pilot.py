# Copyright (c) 2024, MK and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Pilot(Document):
	def before_save(self):
         self.full_name = f"{self.first_name} {self.last_name}"
	
def send_alert(self):
     print("sending msg")