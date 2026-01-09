# E-COMMERCE-WEBSITE

Backend API for E-COMMERCE-WEBSITE

## Tech Stack

- **Frontend**: React
- **Backend**: FastAPI + SQLAlchemy
- **Frontend Source**: GitHub ([Repository](https://github.com/HimaShankarReddyEguturi/Hotelbookinguidesign.git))

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

- User authentication and authorization
- Product catalog management
- Shopping cart functionality
- Order processing and management
- Category management
- Admin panel for managing products and users
- Search functionality
- Pagination for product listing

## API Endpoints

- `POST /api/auth/register` - Register a new user account.
- `POST /api/auth/login` - Log in an existing user.
- `GET /api/products` - Retrieve a list of products, with optional pagination and filtering.
- `GET /api/products/{product_id}` - Retrieve details for a specific product.
- `POST /api/products` - Create a new product (Admin only).
- `PUT /api/products/{product_id}` - Update an existing product (Admin only).
- `DELETE /api/products/{product_id}` - Delete a product (Admin only).
- `GET /api/categories` - Retrieve a list of product categories.
- `GET /api/cart` - Retrieve the user's shopping cart.
- `POST /api/cart/add` - Add a product to the user's shopping cart.

## License

MIT
