# ICSE Chemistry Question Generator

A web application that generates chemistry questions for ICSE Class 7 students.

## Features

- Generates multiple types of questions (MCQ, short answer, long answer)
- Questions are generated dynamically from the knowledge base
- Dark mode interface with modern design
- Supports up to 50 questions at once

## Local Development

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python src/app.py
   ```

## Deployment on Render

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Set the following configuration:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn src.app:app`
4. Deploy!

The application will be available at your Render URL.

## Project Structure

- `src/` - Source code
  - `app.py` - Flask application
  - `knowledge_base/` - Chemistry knowledge base
- `templates/` - HTML templates
- `requirements.txt` - Python dependencies
- `Procfile` - Deployment configuration 