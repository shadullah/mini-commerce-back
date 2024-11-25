# Wellcrafters Mini(Beauty e-commercer app)

Wellcrafters Mini is an e-commerce website built using **Django** as the backend framework. The frontend is powered by React, Javascript, Tailwind Css, React-icons, React-hook-form, react-hot-toast, react-router-dom, PostgreSQL ,React-icons, JWT and other modern web technologies. This README provides instructions for setting up and running the **Django** backend.

## Live backend github Link

- Watch the frontend GitHub repository here:  
  [Wellcrafters Mini Frontend GitHub](https://github.com/shadullah/mini-e-commerce)

---

## Prerequisites

Make sure you have the following installed:

- Python (3.x)
- Django (specific version if required)
- Virtualenv (optional but recommended)
- PostgreSQL or the database used in your settings (if applicable)

---

## Installation

Follow these steps to set up the Django backend:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/shadullah/mini-commerce-back.git
   cd django-backend-wellcrafters
   ```

2. **Install Dependencies**

```bash
   pip install -r requirements.txt
```

3. **Setup Environment variables**

```bash
   No variable set for convention and easy
```

4. **Apply database migrations**

```bash
   python manage.py migrate
```

5. **create a superuser**

```bash
   python manage.py createsuperuser

```

## Running the project

To start django development server, use this line:

```bash
   python manage.py runserver
```

## Features

1. **Authentication:** Authentication and JWT used for accessToken & refreshToken.
2. **CRUD on Carts:** Users can add to cart, remove from cart, Update cart information
3. **REST API:** Product Api taken from dummyJson. Maintained REST structure.

## Technologies Used

- React,
- Javascript,
- Tailwind Css,
- React-icons,
- React-hook-form,
- react-hot-toast,
- react-router-dom,
- PostgreSQL,
- React-icons,
- JWT,
- Django,
- Django-rest-framework
