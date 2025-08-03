# Red30 Tech - Django Web Application

A modern, responsive landing page for Red30 Tech built with Django, featuring a contact form and beautiful UI design.

## Features

- **Modern Landing Page**: Beautiful, responsive design with gradient backgrounds and smooth animations
- **Contact Form**: Functional contact form with name and email fields
- **Form Validation**: Server-side validation with user-friendly error messages
- **Success Messages**: Flash messages for successful form submissions
- **Admin Interface**: Django admin panel to view and manage contact submissions
- **Bootstrap 5**: Modern, mobile-first responsive design
- **Font Awesome Icons**: Professional iconography throughout the interface

## Tech Stack

- **Backend**: Django 5.2.4
- **Frontend**: Bootstrap 5, Font Awesome, Custom CSS
- **Database**: SQLite (default, easily configurable for production)
- **Python**: 3.13.3

## Installation & Setup

### Prerequisites
- Python 3.13+ installed
- Git (optional, for version control)

### Quick Start

1. **Clone or download the project** (if using Git):
   ```bash
   git clone <repository-url>
   cd red30-tech
   ```

2. **Create and activate virtual environment**:
   ```bash
   python3 -m venv red30_env
   source red30_env/bin/activate  # On Windows: red30_env\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (optional, for admin access):
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Open your browser** and navigate to:
   - Landing page: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Project Structure

```
red30_tech/
├── landing/                 # Main landing page app
│   ├── migrations/         # Database migrations
│   ├── templates/landing/  # HTML templates
│   ├── admin.py           # Admin configuration
│   ├── forms.py           # Django forms
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   └── urls.py            # URL routing for landing app
├── red30_tech/            # Main project configuration
│   ├── settings.py        # Django settings
│   ├── urls.py           # Main URL configuration
│   └── wsgi.py           # WSGI configuration
├── manage.py             # Django management script
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Usage

### Contact Form
- The landing page features a contact form with name and email fields
- All form submissions are stored in the database
- Success messages are displayed to users after successful submission
- Form includes client-side and server-side validation

### Admin Panel
- Access the admin panel at `/admin/`
- View and manage all contact form submissions
- Search and filter contacts by name, email, or submission date

## Customization

### Styling
- Main styles are defined in the HTML template (`landing/templates/landing/landing_page.html`)
- Color scheme uses CSS custom properties (variables) for easy theming
- Bootstrap 5 classes provide responsive grid and components

### Content
- Update company information in the template file
- Modify the features section to highlight your services
- Customize the hero section text and messaging

### Database
- For production, configure a production database in `settings.py`
- Current setup uses SQLite for development convenience

## Development

### Adding New Features
1. Create new models in `landing/models.py`
2. Run `python manage.py makemigrations` to create migrations
3. Run `python manage.py migrate` to apply changes
4. Update views, forms, and templates as needed

### Static Files
- For production, configure static file serving
- Add `STATIC_ROOT` setting for deployment
- Consider using a CDN for Bootstrap and Font Awesome

## Deployment

For production deployment:

1. **Update settings**:
   - Set `DEBUG = False`
   - Configure `ALLOWED_HOSTS`
   - Set up production database
   - Configure static file serving

2. **Environment variables**:
   - Store secret key in environment variable
   - Configure database credentials securely

3. **Web server**:
   - Use Gunicorn or uWSGI for WSGI server
   - Configure Nginx or Apache for reverse proxy
   - Set up SSL certificates

## Contact

For questions or support regarding this Django application, please use the contact form on the website or reach out to the Red30 Tech team.

---

© 2024 Red30 Tech. All rights reserved.