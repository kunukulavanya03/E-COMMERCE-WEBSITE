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

- User registration and authentication
- Product browsing and searching
- Product details page
- Shopping cart management
- Order placement and tracking
- Admin panel for product management
- Category management
- User role management (Admin)
- Secure password storage
- JWT based authentication
- Database interaction using SQLAlchemy ORM

## API Endpoints

- `POST /api/auth/register` - Registers a new user account.
- `POST /api/auth/login` - Logs in an existing user.
- `GET /api/products` - Retrieves a list of all products, with optional pagination and filtering.
- `GET /api/products/{product_id}` - Retrieves a specific product by its ID.
- `POST /api/products` - Creates a new product (Admin only).
- `PUT /api/products/{product_id}` - Updates an existing product (Admin only).
- `DELETE /api/products/{product_id}` - Deletes a product (Admin only).
- `GET /api/categories` - Retrieves a list of all product categories.
- `GET /api/cart` - Retrieves the user's shopping cart.
- `POST /api/cart/add/{product_id}` - Adds a product to the user's shopping cart.

## License

MIT
