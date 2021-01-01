# purchase_lines_import
Odoo App to import purchase lines from excel file.

If you have a list of items to create PO by, you don't need to create this PO manualy and select product and fill info line by line.

Preparation of this data in excel file is easier, write this PO lines in excel file like: 

Product name | Description | Quantity | Tax | Discount
======================================================

then import this data iin the Menue of (Import Order Lines) showed in Purchase main menue

import this file lines in this model, then select lines you  want to create PO by, click on action
and select Create Purchase Order, a wizard will be arised to let you select order date, supplier, and order type (If you want to created in Draft state or as Done).

then PO created will be opened to you.

^-^ And Have Fun ^-^
