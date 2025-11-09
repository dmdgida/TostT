# Tost Tiyatrosu Menu Application

## Overview
This is a Flask-based menu management system for "Tost Tiyatrosu" restaurant. The application allows users to view menu items organized by categories, and provides admin functionality to add/remove items and categories.

## Project Structure
- `proje.py` - Main Flask application with all routes and logic
- `init_db.py` - Database initialization script
- `veri_tabani.py` - Legacy database utilities
- `templates/` - HTML templates for the web interface
- `static/uploads/` - Uploaded images for menu items and categories
- `menuu.db` - SQLite database (not version controlled)

## Technology Stack
- **Backend**: Flask (Python web framework)
- **Database**: SQLite
- **Frontend**: HTML with inline CSS
- **Production Server**: Gunicorn

## Database Schema
### Tables:
1. **kategoriler** (categories)
   - id (INTEGER PRIMARY KEY)
   - name (TEXT, UNIQUE)
   - image (TEXT)

2. **menuu** (menu items)
   - id (INTEGER PRIMARY KEY)
   - name (TEXT)
   - price (REAL)
   - category (TEXT)
   - description (TEXT)
   - image (TEXT)

## Key Routes
- `/` - Homepage showing all categories
- `/kategori/<kategori_adi>` - View items in a specific category
- `/ekle` - Add new menu items
- `/sil` - Delete menu items
- `/kategori-ekle` - Add new category (POST)
- `/kategori-sil` - Delete category (POST)

## Setup & Configuration
- Development server runs on `0.0.0.0:5000`
- Production deployment uses Gunicorn with autoscaling
- Database is automatically initialized on first run

## Recent Changes (Nov 6, 2025)
- Configured for Replit environment
- Updated Flask app to bind to 0.0.0.0:5000
- Created database initialization script
- Added .gitignore for Python projects
- Configured Gunicorn for production deployment
- Set up workflow for development server

## User Preferences
None recorded yet.

## Project Architecture
This is a traditional Flask monolith with:
- SQLite for data persistence
- Server-side rendered templates (Jinja2)
- Static file serving for images
- Simple CRUD operations for menu management
