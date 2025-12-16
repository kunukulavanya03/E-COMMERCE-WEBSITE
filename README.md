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

- Product browsing and filtering
- Cart management
- Order history tracking
- Admin product management

## API Endpoints

- `GET /api/products` - Retrieve a list of all available products.
- `POST /api/cart/add` - Add a product to the user's cart.
- `GET /api/orders` - Retrieve a list of all orders for the authenticated user.
- `POST /api/admin/products` - Create a new product.

## License

MIT
