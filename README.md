
# Travease - Online Bus Booking System 🚍

Travease is a full-stack web application that allows users to book bus tickets online. It offers features for user registration, login, bus browsing, seat booking, and viewing bookings.

---

## 🛠 Tech Stack

### Frontend:
- React.js (with React Router)
- Tailwind CSS

### Backend:
- Django REST Framework (DRF)
- Python

### Deployment:
- Render (Frontend and Backend)

---

## 🚀 Features

- 🔐 User Authentication (Register/Login/Logout)
- 🚌 Browse Available Buses
- 🪑 Seat Booking (only for logged-in users)
- 💳 Checkout with passenger details and payment method
- 📋 View and Cancel My Bookings

---

## 🧩 Project Structure

```
Travease/
├── frontend/          # React application
├── backend/           # Django project
```

---

## ⚙️ Setup Instructions

### ✅ 1. Clone the Repository

```bash
git clone https://github.com/your-username/Travease.git
cd Travease
```

### 🧠 2. Backend Setup (Django + DRF)

#### a. Navigate to the backend folder:

```bash
cd Travels_App_DjangRF/travels
```

#### b. Create virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

#### c. Install dependencies:

```bash
pip install -r requirements.txt
```

#### d. Apply migrations and run the server:

```bash
python manage.py migrate
python manage.py runserver
```

> 📌 Backend will run on: `http://127.0.0.1:8000` or deployed Render URL

---

### 🌐 3. Frontend Setup (React)

#### a. Navigate to the frontend folder:

```bash
cd ../React_travels/travels
```

#### b. Install dependencies:

```bash
npm install
```

#### c. Start the React development server:

```bash
npm start
(or)
npm run dev
```

> 📌 Frontend runs on: `http://localhost:5173`

---

## 🌍 Deployment (Render)

- Ensure both frontend and backend are deployed on Render.
- **Important:** On Render's frontend service settings, go to **Redirects/Rewrites** and add:

| Source | Destination | Action   |
|--------|-------------|----------|
| `/*`   | `/index.html` | Rewrite |

This allows React routes to work properly on page reload.

---

## 🔑 Usage Instructions

1. Visit the home page.
2. New users must **Register** to book tickets.
3. Registered users can **Login** to:
   - View buses
   - View available seats
   - Book seats (navigates to **Checkout**)
   - View **My Bookings**
   - Cancel a booking
   - Logout

---

## 📦 APIs

- Backend REST APIs exposed under `/api/`
- Auth, buses, seats, booking endpoints available

---

## 📧 Contact

For any issues or suggestions, feel free to contact:
- Anirudh Vempati - anirudhedu.05@gmail.com

---

© 2025 Travease. All rights reserved.
