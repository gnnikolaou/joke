# Red30 Tech - Django Web Application

A modern, responsive landing page for Red30 Tech built with Django. The application features a beautiful landing page with a contact form that collects user information.

## Features

- **Modern Landing Page**: Beautiful, responsive design with Bootstrap 5
- **Contact Form**: Collects name and email with form validation
- **Admin Interface**: Django admin panel to manage contact submissions
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Modern UI**: Gradient backgrounds, hover effects, and smooth animations

## Technology Stack

- **Backend**: Django 5.2.4
- **Frontend**: Bootstrap 5, Font Awesome Icons
- **Database**: SQLite (default)
- **Python**: 3.13+

## Installation & Setup

### Prerequisites

- Python 3.13 or higher
- pip (Python package installer)

### Installation Steps

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd red30tech
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (optional):
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the application**:
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/
     - Username: admin
     - Password: admin123

## Project Structure

```
red30tech/
├── landing/                 # Main app
│   ├── models.py           # Contact model
│   ├── views.py            # Landing page view
│   ├── forms.py            # Contact form
│   ├── admin.py            # Admin configuration
│   └── templates/
│       └── landing/
│           └── landing_page.html  # Main template
├── red30tech/              # Project settings
│   ├── settings.py         # Django settings
│   └── urls.py             # Main URL configuration
├── static/                 # Static files directory
├── manage.py               # Django management script
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Features Overview

### Landing Page Sections

1. **Navigation Bar**: Responsive navigation with company branding
2. **Hero Section**: Eye-catching introduction with call-to-action
3. **Services Section**: Six service cards showcasing company offerings
4. **Contact Form**: User-friendly form with validation
5. **Footer**: Social media links and company information

### Contact Form

- **Fields**: Name and Email
- **Validation**: Server-side validation with error messages
- **Success Messages**: User-friendly success notifications
- **Database Storage**: All submissions stored in SQLite database

### Admin Interface

- **Contact Management**: View, search, and filter contact submissions
- **User Management**: Manage admin users and permissions
- **Secure Access**: Password-protected admin panel

## Customization

### Styling

The application uses custom CSS variables for easy theming:

```css
:root {
    --primary-color: #dc3545;    /* Main brand color */
    --secondary-color: #6c757d;  /* Secondary color */
    --accent-color: #fd7e14;     /* Accent color */
}
```

### Content

- Update company information in the template
- Modify services in the services section
- Change contact form fields in `landing/models.py`
- Update social media links in the footer

## Development

### Running in Development Mode

```bash
python manage.py runserver
```

### Making Database Changes

```bash
python manage.py makemigrations
python manage.py migrate
```

### Creating New Migrations

```bash
python manage.py makemigrations landing
```

## Deployment

For production deployment, consider:

1. **Environment Variables**: Move sensitive settings to environment variables
2. **Database**: Use PostgreSQL or MySQL for production
3. **Static Files**: Configure proper static file serving
4. **Security**: Set `DEBUG = False` and configure `ALLOWED_HOSTS`
5. **Web Server**: Use Gunicorn with Nginx or Apache

## License

This project is created for demonstration purposes.

## Support

For questions or issues, please contact the development team.