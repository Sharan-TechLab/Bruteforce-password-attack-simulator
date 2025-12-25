# Advanced Brute Force Attack Simulator

This project simulates advanced brute force attacks on login systems
for educational and cybersecurity learning purposes.

## Features
- Password list attack simulation
- Attempt limiting and account lockout
- Time delay to simulate real attacks
- Password hashing (SHA-256)
- IP tracking and logging
- URL-based attack simulation
- Hydra-like automation script
- Digital UI with logs display
- Multi-threaded attack simulation
- Risk level detection (LOW/MEDIUM/HIGH)
- Security monitoring dashboard
- User-agent randomization
- Proxy rotation simulation

## New Advanced Features
- **Real IP Tracking**: Simulates IP addresses for each attempt
- **Live Website Testing**: Simulate attacks on target URLs
- **Automation Tools**: Python script mimicking Hydra for brute force
- **Logging**: Detailed logs of all attempts with timestamps
- **User Data**: Basic user simulation (expandable)
- **Multi-threading**: Concurrent attack simulation
- **Risk Assessment**: Dynamic risk level calculation
- **Dashboard**: Real-time monitoring of security metrics
- **Defensive Mechanisms**: Progressive delays and lockouts

## Usage
1. Run the Flask app: `python app.py`
2. Access the login simulator at `http://localhost:5000/`
3. Use the attack simulator at `http://localhost:5000/attack`
4. View the security dashboard at `http://localhost:5000/dashboard`
5. Run the Hydra simulation: `python hydra_script.py <url> <username> password.txt`

## Educational Goals
- Understand authentication security mechanisms
- Learn about brute force attack patterns
- Explore defensive strategies like rate limiting and monitoring
- Study risk assessment in cybersecurity

## Disclaimer
This project is for educational purposes only. Do not use for illegal activities.

To run this file in terminal execute py app.py
