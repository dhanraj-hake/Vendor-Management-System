# Vendor Management System API

This is a Vendor Management System API built using Django and Django REST Framework. It provides endpoints for managing vendors, purchase orders, and evaluating vendor performance metrics.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Apply database migrations:
   ```
   python manage.py migrate
   ```

4. Create a superuser (for admin access):
   ```
   python manage.py createsuperuser
   ```

5. Run the development server:
   ```
   python manage.py runserver
   ```

6. Access the API at `http://localhost:8000/api/`

## API Endpoints

### Vendors
- **GET /api/vendors/**: List all vendors.
- **POST /api/vendors/**: Create a new vendor.
- **GET /api/vendors/{vendor_id}/**: Retrieve details of a specific vendor.
- **PUT /api/vendors/{vendor_id}/**: Update details of a specific vendor.
- **DELETE /api/vendors/{vendor_id}/**: Delete a specific vendor.

### Purchase Orders
- **GET /api/purchase_orders/**: List all purchase orders.
- **POST /api/purchase_orders/**: Create a new purchase order.
- **GET /api/purchase_orders/{po_id}/**: Retrieve details of a specific purchase order.
- **PUT /api/purchase_orders/{po_id}/**: Update details of a specific purchase order.
- **DELETE /api/purchase_orders/{po_id}/**: Delete a specific purchase order.
- **POST /api/purchase_orders/{po_id}/acknowledge/**: Acknowledge a purchase order.

### Vendor Performance Metrics
- **GET /api/vendors/{vendor_id}/performance/**: Retrieve performance metrics for a specific vendor.

