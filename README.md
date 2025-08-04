# Ecommerce API Gateway

Routes API requests to services and handles WebSocket connections for real-time events.

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the service:
   ```bash
   uvicorn src.main:app --reload
   ```

## Endpoints
- `GET /customer`: Fetch customer data
- `POST /customer/address`: Update customer address
- `WS /ws`: WebSocket endpoint for real-time events

## Dependencies
- User Service, Cart Service, Order Service, Payment Service
- Event Bus: For WebSocket event forwarding
