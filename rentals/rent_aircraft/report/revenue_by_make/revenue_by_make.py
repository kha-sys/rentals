# Copyright (c) 2024, MK and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    
    frappe.errprint(filters)
    
    columns = [{
        "fieldname": "make",
        "label": "Make",
        "fieldtype": "Data"
    }, {
        "fieldname": "total_revenue",
        "label": "Total Revenue",
        "fieldtype": "Currency",
        "options": "TL"
    }]
    
    data = frappe.get_all("Craft Booking",
        fields=["SUM(total_amount) AS total_revenue", "aircraft.make"], 
        filters={"docstatus": 1}, 
        group_by="make"
    )

    chart = {
        "data": {
            "labels": [x.make for x in data],
            "datasets": [{"values": [x.total_revenue for x in data]}],
        },
        "type": "pie"
    }
    
    return columns, data, "Hello this is report", chart
