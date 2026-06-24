# API Performance Monitor

## Project Overview

API Performance Monitor is a Python-based tool that monitors the health and performance of API endpoints. It sends HTTP requests to APIs, measures response times, records status codes, and stores the results in a log file for analysis.

This project helps developers identify slow APIs, monitor uptime, and track API performance over time.

## Features

- Monitor API availability
- Measure response times
- Track HTTP status codes
- Log API performance data
- Generate performance reports
- Simple and easy-to-use interface

## Technologies Used

- Python 3
- Requests
- Pandas
- CSV
- Datetime

## Project Structure

api-performance-monitor/

├── monitor.py

├── report.py

├── config.py

├── requirements.txt

├── logs.csv

├── README.md

└── .gitignore

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/api-performance-monitor.git
cd api-performance-monitor
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the monitoring script:

```bash
python monitor.py
```

Generate a report:

```bash
python report.py
```

## Example Output

```text
API: https://jsonplaceholder.typicode.com/posts
Status Code: 200
Response Time: 0.25 seconds
Timestamp: 2026-06-24 10:30:15
```

## Log File Example

```csv
Timestamp,API_URL,Status_Code,Response_Time
2026-06-24 10:30:15,https://jsonplaceholder.typicode.com/posts,200,0.25
2026-06-24 10:31:15,https://jsonplaceholder.typicode.com/posts,200,0.21
```

## Future Improvements

- Email notifications
- Real-time dashboard
- Database integration
- Performance charts
- Multi-API monitoring

## Author
T VRUKSHA

## License

This project is licensed under the MIT License.
