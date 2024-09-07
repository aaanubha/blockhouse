# blockhouse

# Candlestick and Chart Dashboard

This repository contains a project with a **Django backend** and a **Next.js frontend**. The frontend is a dashboard that includes various charts (Candlestick, Line, Bar, and Pie charts) with data fetched from the Django backend API.

## File Structure

```bash
/project-root
   /backend    # Django backend
      /backend  # Django project
      /charts   # Django app for chart APIs
      /env      # Python virtual environment for Django
      manage.py
   /frontend    # Next.js frontend
      /components  # Chart components
         LineChart.js
         BarChart.js
         PieChart.js
         CandlestickChart.js
      /pages  # Next.js pages
         index.js  # Dashboard page
      package.json
      node_modules
   get-pip.py    # Script to install pip (optional)


## How to run

## Backend

cd backend
python3 -m venv env
source env/bin/activate  # On Mac/Linux
pip install -r requirements.txt
python3 manage.py runserver


## Frontend
cd frontend
npm install
npm run dev

