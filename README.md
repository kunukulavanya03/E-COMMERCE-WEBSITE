# E-COMMERCE-WEBSITE

Backend API for E-COMMERCE-WEBSITE

## Tech Stack

- **Frontend**: React
- **Backend**: FastAPI + SQLAlchemy
- **Frontend Source**: GitHub ([Repository](https://github.com/Malleswar-249/E-COMMERCE-WEBSITE))

## Project Structure

```
E-COMMERCE-WEBSITE/
├── frontend/          # Frontend application
├── backend/           # Backend API
├── README.md          # This file
└── docker-compose.yml # Docker configuration (if applicable)
```

## Getting Started

### Prerequisites

- Node.js 18+ (for frontend)
- Python 3.11+ (for Python backends)
- Docker (optional, for containerized setup)

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

### Backend Setup

```bash
cd backend
# Follow backend-specific setup instructions in backend/README.md
```

## Features

- product_browsing
- cart_management
- order_tracking
- admin_product_management

## API Endpoints

- `GET /api/products` - Retrieve a list of all products.
- `GET /api/products/{product_id}` - Retrieve a specific product by ID.
- `POST /api/cart` - Add a product to the user's cart.
- `GET /api/orders` - Retrieve a list of all orders for the authenticated user.
- `POST /api/orders` - Place a new order for the authenticated user.
- `POST /api/admin/products` - Create a new product as an admin.
- `PUT /api/admin/products/{product_id}` - Update an existing product as an admin.
- `DELETE /api/admin/products/{product_id}` - Delete a product as an admin.

## License

MIT
