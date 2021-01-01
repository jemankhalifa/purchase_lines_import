################################################

{ 
    "name": "Purchase Lines Import",
    "summary": """Custom Feature to allow import purchase order lines from excel files""",
    "Description": """ Allow you to import long list of purchases items from excel file 
        and create a PO by selecting a vendor, date and all products lines imported""",
    "version": '12.0',   
    "category": 'Purchase',   
    "author": "Eman Khalifa",
    "website": "https://www.emankhalifa.com",
   
    "depends": ["purchase"],

    "data": [
       'security/ir.model.access.csv',
       'wizard/product_lines_migration_view.xml',

    ],
  
    "sequence": 3,
    "application": False,
    "installable": True,
    "auto_install": False,
}
