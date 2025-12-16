# e-commerce-website

Backend API for e-commerce-website

## Tech Stack

- **Frontend**: React
- **Backend**: FastAPI + SQLAlchemy
- **Frontend Source**: GitHub ([Repository](https://github.com/Malleswar-249/E-COMMERCE-WEBSITE))

## Project Structure

```
e-commerce-website/
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

- User Authentication
- Product Management
- Shopping Cart
- Order Processing

## API Endpoints

- `POST /api/register` - Endpoint for user registration.
- `POST /api/login` - Endpoint for user login.
- `GET /api/products` - Endpoint to retrieve all products.
- `GET /api/products/{product_id}` - Endpoint to retrieve a specific product by ID.
- `POST /api/cart` - Endpoint to add a product to the user's cart.
- `GET /api/cart` - Endpoint to view all products in the user's cart.
- `DELETE /api/cart/{product_id}` - Endpoint to remove a product from the user's cart.
- `POST /api/orders` - Endpoint to create an order for the items in the user's cart.

## License

MIT
