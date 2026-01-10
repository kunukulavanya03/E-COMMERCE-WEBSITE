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
- Product catalog browsing and searching
- Shopping cart management
- Order placement and tracking
- Admin panel for product and user management
- Category management
- Secure password storage (hashing)
- API rate limiting to prevent abuse

## API Endpoints

- `POST /api/auth/register` - Registers a new user.
- `POST /api/auth/login` - Logs in an existing user.
- `GET /api/auth/me` - Retrieves the currently logged-in user's profile.
- `GET /api/products` - Retrieves a list of products, optionally filtered by category and search term.
- `GET /api/products/{product_id}` - Retrieves a specific product by ID.
- `POST /api/products` - Creates a new product (Admin only).
- `PUT /api/products/{product_id}` - Updates an existing product (Admin only).
- `DELETE /api/products/{product_id}` - Deletes a product (Admin only).
- `GET /api/categories` - Retrieves a list of product categories.
- `POST /api/cart/add` - Adds a product to the user's shopping cart.

## License

MIT
