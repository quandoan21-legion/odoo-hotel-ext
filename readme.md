# Hotel Extension Module

## Summary
This module extends the functionality of the existing Hotel Management module in Odoo. It adds new features and customizations to enhance the management of hotel rooms, orders, and order history.

## Description
The `hotel-ext` module provides additional capabilities for managing hotel rooms and orders. It includes custom views, models, and logic to improve the overall functionality of the hotel management system.

## Folder Structure
```plain_text
addons/
└── hotel-ext/
    ├── __init__.py
    ├── __manifest__.py
    ├── models/
    │   ├── __init__.py
    │   ├── RoomExtend.py
    │   ├── RoomOrderHistory.py
    │   ├── HotelExtend.py
    │   ├── RoomOrderExtend.py
    ├── views/
    │   ├── views.xml
    │   ├── templates.xml
    │   ├── form_views/
    │   │   ├── view_hotel_form_extend.xml
    │   │   ├── view_hotel_room_form_extend.xml
    │   ├── list_views/
    │   │   ├── view_hotel_room_list_extend.xml
    ├── security/
    │   ├── ir.model.access.csv
    ├── demo/
    │   ├── demo.xml
    ├── README.md
```
## Features
- Extended room order model to include order history whenever new record of the RoomOrder model is created.
- Custom views for hotel and room forms.
  - User can see the hotel orders and order history in the hotel form view.
- Additional search and filter options for hotel rooms.
  - Room size
  - Allow smoking
  - Maximum occupancy
- Automatic creation of order history records upon room order creation.

## Installation
1. Ensure that the base [hotel](https://github.com/quandoan21-legion/hotel_management_odoo) module is installed.
2. Copy the `hotel-ext` module to your Odoo add-ons directory.
3. Update the module list by running the following command:
   ```bash
   odoo -u all