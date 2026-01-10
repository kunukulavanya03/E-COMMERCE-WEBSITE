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

- User registration and authentication (JWT)
- Product catalog management (CRUD operations)
- Product categorization
- Shopping cart functionality
- Order placement and tracking
- Admin panel for product and user management
- Password reset functionality
- Search functionality

## API Endpoints

- `POST /api/auth/register` - Register a new user account.
- `POST /api/auth/login` - Login with an existing user account.
- `POST /api/auth/password_reset` - Request password reset for a user.
- `GET /api/products` - Retrieve a list of products (paginated).
- `GET /api/products/{product_id}` - Retrieve details for a specific product.
- `POST /api/products` - Create a new product (admin only).
- `PUT /api/products/{product_id}` - Update an existing product (admin only).
- `DELETE /api/products/{product_id}` - Delete a product (admin only).
- `GET /api/categories` - Retrieve a list of product categories.
- `GET /api/cart` - Retrieve the user's shopping cart.

## License

MIT
