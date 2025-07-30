# Finance Analyzer & ML Categorization 📊

A personal finance management application that combines my passion for **machine learning** and **Django's versatility** to create an intelligent transaction tracking system.

## What It Is 💡

This is a full-stack financial transaction manager that automatically categorizes your expenses using machine learning. I built this project because I love how Django's flexibility allows you to seamlessly integrate ML models with web applications, creating truly intelligent user experiences.

The app learns from transaction descriptions to predict categories, making personal finance management effortless. You can add transactions manually, import CSV files, and get beautiful analytics - all while the ML model works behind the scenes to keep everything organized.

## Why I Built This 🎯

I'm passionate about **machine learning** and fascinated by **Django's versatility**. This project perfectly showcases both:

- **Django's Power**: The framework's "batteries included" philosophy made it easy to build a robust API, handle file uploads, integrate ML models, and manage data relationships
- **ML Integration**: I wanted to demonstrate how seamlessly Python's ML ecosystem (scikit-learn) integrates with Django to create intelligent web applications
- **Real-World Application**: Personal finance is something everyone can relate to, and adding ML-powered categorization makes it genuinely useful

Django's flexibility allowed me to structure this as a clean API that serves both the React frontend and could easily support mobile apps or other clients in the future.

## Tech Stack 🛠️

### Backend (Django REST Framework)
- **Django 4.2+** - My favorite web framework for its versatility and rapid development
- **Django REST Framework** - Clean, powerful API development
- **scikit-learn** - Machine learning for transaction categorization
- **pandas** - Data processing and CSV handling
- **SQLite** - Simple database for development (easily scalable to PostgreSQL)

### Frontend (React TypeScript)
- **React 19+** with **TypeScript** - Modern, type-safe frontend development
- **Tailwind CSS** - Utility-first styling for rapid UI development
- **Radix UI** - Accessible, customizable component primitives
- **Recharts** - Beautiful data visualizations
- **Axios** - Clean API communication

### Machine Learning Features 🤖
- **Automatic Categorization**: TF-IDF vectorization + Logistic Regression to categorize transactions
- **Training Pipeline**: Easy model retraining with new data
- **Categories**: Food & Dining, Transportation, Shopping, Entertainment, and more

## Quick Start 🚀

**Backend:**
```bash
cd bookkeeping-backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

**Frontend:**
```bash
cd bookkeeping-frontend
npm install
npm start
```

**Train ML Model:**
```bash
cd bookkeeping-backend
python ml/train_model.py
```

## Key Features ✨

- 📝 **Smart Transaction Entry** - Add transactions with ML-powered category suggestions
- 📁 **CSV Import** - Bulk import your existing transaction data
- 📈 **Analytics Dashboard** - Monthly summaries and interactive charts
- 🎯 **Auto-Categorization** - ML model learns from descriptions to categorize expenses
- 📱 **Responsive Design** - Works beautifully on desktop and mobile


**Built with ❤️ - Uzma**
