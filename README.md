# Gas Utility Service Request System

##  Description

This is a Django-based web application for a gas utility company to manage customer service requests efficiently. The system allows customers to submit service requests, track their status, and receive updates. Additionally, admins can manage requests through the Django admin panel.

##  Features

- **Customer Request Submission**: Users can submit gas service requests online.
- **Request Tracking**: Customers can view the status of their requests.
- **Admin Panel**: Admins can manage and update service requests.
- **Django-Based**: Built using Django framework with an easy-to-use UI.

##  Tech Stack

- **Backend**: Django, Python
- **Database**: SQLite (default) or PostgreSQL (for production)
- **Frontend**: HTML, CSS, Django Templates

##  Installation & Setup

### 1️ Clone the Repository

```sh
git clone https://github.com/anantmayuri/gas_utility.git
cd gas_utility
```

### 2️ Create and Activate Virtual Environment

```sh
python -m venv myworld
# Activate on Windows
myworld\Scripts\activate
# Activate on Mac/Linux
source myworld/bin/activate
```

### 3️ Install Dependencies

```sh
pip install -r requirements.txt
```

### 4️ Run Migrations

```sh
python manage.py makemigrations
python manage.py migrate
```

### 5️ Create a Superuser (for Admin Panel)

```sh
python manage.py createsuperuser
```

### 6️ Run the Development Server

```sh
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

## 🏗 Project Structure

```
├── gas_utility/        # Main Django project
│   ├── settings.py     # Project settings
│   ├── urls.py         # Main URL configurations
│   ├── wsgi.py         # WSGI entry point
│   ├── asgi.py         # ASGI entry point
│
├── service_requests/   # App for handling service requests
│   ├── models.py       # Database models
│   ├── views.py        # Business logic
│   ├── urls.py         # App-specific URLs
│   ├── templates/      # HTML templates
│
├── manage.py           # Django management script
├── db.sqlite3          # Database file (ignored in production)
└── requirements.txt    # Required dependencies
```

##  License

This project is licensed under the MIT License - see the `LICENSE` file for details.

##  Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss.

##  Contact

For inquiries, contact **Anant Mayuri** at [GitHub Profile](https://github.com/anantmayuri).



