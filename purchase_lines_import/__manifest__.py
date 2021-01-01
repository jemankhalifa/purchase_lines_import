################################################

{ 
    "name": "Purchase Lines Import",
    "summary": """Custom Feature to allow import purchase order lines from excel files""",
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
