# Project Log

## 04-06-2026

### Milestone 1 - GoodWe API Connected

Achievements:
- Created first Python virtual environment on Ubuntu
- Installed pygoodwe package
- Connected successfully to GoodWe SEMS API
- Retrieved live inverter telemetry
- Retrieved battery voltage data (379.7V)

Evidence:
See docs/screenshots/04-06-2026-first-goodwepull-success.png

Lessons Learned:
- Ubuntu 24.04 uses externally managed Python environments
- Virtual environments isolate project dependencies
- Third-party APIs can be integrated through Python libraries

Next Steps:
- Extract solar generation
- Extract battery state of charge
- Store telemetry in SQLite
- Build Grafana dashboard
