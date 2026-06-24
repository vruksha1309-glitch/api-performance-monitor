# API Performance Monitor

A professional web-based system to continuously track API endpoints, record performance metrics, detect failures, and generate analytical reports — built as a final-year mini project.

---

## Tech Stack

| Layer       | Technology          |
|-------------|---------------------|
| Backend     | Python 3.11+ / Flask |
| Scheduler   | APScheduler         |
| HTTP Client | Requests            |
| Database    | SQLite              |
| Frontend    | HTML5 / CSS3 / JS   |
| Charts      | Chart.js 4          |
| PDF Reports | ReportLab           |
| Dashboard   | Grafana (optional)  |

---

## Quick Start

```bash
# 1. Clone / extract the project
cd api_performance_monitor

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run
python run.py
```

Open **http://localhost:5000** — login with `admin` / `admin123`.

---

## Project Structure

```
api_performance_monitor/
├── run.py                          # Entry point
├── requirements.txt
├── app/
│   ├── __init__.py                 # App factory
│   ├── config.py                   # Configuration
│   ├── database.py                 # DB init & helpers
│   ├── auth/
│   │   └── routes.py               # Login / logout / change-password
│   ├── dashboard/
│   │   └── routes.py               # Stats & chart JSON APIs
│   ├── monitoring/
│   │   ├── routes.py               # API CRUD & manual test
│   │   └── scheduler.py            # APScheduler background pings
│   ├── reports/
│   │   └── routes.py               # CSV & PDF export
│   └── alerts/
│       └── routes.py               # Active alerts & failure history
├── templates/
│   ├── base.html
│   ├── auth/   login.html  change_password.html
│   ├── dashboard/  index.html
│   ├── monitoring/ index.html  add.html  edit.html  logs.html
│   ├── alerts/     index.html
│   └── reports/    index.html
├── static/
│   ├── css/style.css
│   └── js/  main.js  dashboard.js  monitoring.js  alerts.js  reports.js
├── database/
│   └── monitor.db                  # Auto-created on first run
├── scripts/
│   └── schema.sql                  # Standalone SQL schema
├── grafana/
│   └── GRAFANA_SETUP.md
├── tests/
│   └── test_app.py                 # pytest test suite
└── docs/
    └── ARCHITECTURE.md
```

---

## Features

### User Authentication
- SHA-256 password hashing
- Flask session management
- Route-level `@login_required` decorator

### API Management
- Add / Edit / Delete / Toggle (enable/disable) endpoints
- Manual one-click test with instant results
- Per-API log history (last 100 results)

### Automatic Monitoring
- APScheduler pings every API at its configured interval
- Measures response time (ms), HTTP status code, availability
- New APIs are detected automatically every 30 s without restart

### Analytics Dashboard
- 6 live stat cards: total APIs, active, avg RT, total reqs, failures, uptime %
- Response-time line chart (24 h, per API)
- Daily request volume bar chart (7 d)
- Per-API availability doughnut chart
- Live activity table (last 20 results)

### Alert System
- Detects downed APIs (last log = unavailable)
- Slow-response alerts (configurable threshold, default 2 s)
- Low-uptime alerts (configurable threshold, default 95 %)
- Alert count badge in sidebar, auto-refreshes every 30 s

### Reporting
- CSV export (all logs, date-range filtered, per-API filter)
- PDF export via ReportLab (summary + detail table)
- Per-API uptime summary table
- Report history log

### Grafana Integration
- See `grafana/GRAFANA_SETUP.md` for data source + panel query setup

---

## Configuration

Edit `app/config.py`:

| Setting                    | Default | Description                         |
|----------------------------|---------|-------------------------------------|
| `DEFAULT_MONITOR_INTERVAL` | 60 s    | Fallback interval for new APIs      |
| `REQUEST_TIMEOUT`          | 10 s    | Per-request timeout                 |
| `RESPONSE_TIME_THRESHOLD`  | 2000 ms | Alert if response time exceeds this |
| `UPTIME_THRESHOLD`         | 95.0 %  | Alert if 24 h uptime drops below    |

---

## Running Tests

```bash
pip install pytest
pytest tests/ -v
```

---

## System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                      Browser (Client)                   │
│        HTML + Chart.js + JS fetch() polling             │
└──────────────────────┬──────────────────────────────────┘
                       │ HTTP
┌──────────────────────▼──────────────────────────────────┐
│                  Flask Web Server                        │
│   ┌──────────┐ ┌────────────┐ ┌─────────┐ ┌─────────┐  │
│   │  auth BP │ │dashboard BP│ │monitor  │ │reports  │  │
│   └──────────┘ └────────────┘ │   BP    │ │   BP    │  │
│                               └────┬────┘ └─────────┘  │
│   ┌──────────────────────────────┐ │                    │
│   │   APScheduler (background)   │ │ CRUD               │
│   │   pings active APIs every N s│ │                    │
│   └─────────────────┬────────────┘ │                    │
└─────────────────────┼──────────────┼────────────────────┘
                      │ INSERT       │ SELECT/INSERT/UPDATE
          ┌───────────▼──────────────▼──────────┐
          │            SQLite DB                 │
          │  users | apis | monitoring_logs      │
          │         | reports                    │
          └──────────────────┬──────────────────┘
                             │ SQL (optional)
                     ┌───────▼──────┐
                     │    Grafana   │
                     │  dashboards  │
                     └──────────────┘
```

---

## Database Schema

```
users            apis                monitoring_logs      reports
────────         ────────────────    ───────────────────  ───────────
id (PK)          id (PK)             id (PK)              id (PK)
username         api_name            api_id (FK→apis)     report_name
password         endpoint_url        response_time        report_type
role             monitoring_interval status_code          file_path
created_at       status              availability         generated_at
                 created_at          error_message
                                     monitored_at
```

---

## Future Enhancements

1. **Email / SMS Alerts** — SMTP or Twilio integration when an API goes down
2. **Multi-user Roles** — viewer-only accounts alongside admin
3. **WebSocket Live Feed** — push monitoring results to dashboard in real time
4. **SLA Tracking** — monthly uptime percentage targets per API
5. **Response Body Validation** — assert expected JSON keys or values
6. **Rate-limit Detection** — detect HTTP 429 patterns
7. **Docker Compose Setup** — one-command deployment with Grafana container
8. **Prometheus Exporter** — expose `/metrics` endpoint for Prometheus scraping
9. **AI Anomaly Detection** — flag unusual response-time spikes
10. **Mobile App** — React Native client consuming the existing JSON APIs

---

## License

MIT — free to use for educational and commercial purposes.
