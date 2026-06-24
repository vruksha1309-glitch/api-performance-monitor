"""
API Performance Monitor - Main Entry Point
==========================================
Run this file to start the Flask application.
Usage: python run.py
"""

from app import create_app
from app.monitoring.scheduler import start_scheduler

app = create_app()

if __name__ == '__main__':
    # Start the background monitoring scheduler
    start_scheduler(app)
    
    print("=" * 60)
    print("  API Performance Monitor")
    print("  Running at: http://localhost:5000")
    print("  Default Admin: admin / admin123")
    print("=" * 60)
    
    app.run(debug=True, host='0.0.0.0', port=5000, use_reloader=False)
