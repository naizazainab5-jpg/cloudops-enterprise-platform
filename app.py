from flask import Flask, jsonify
import psutil
import platform
import os

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>CloudOps Enterprise Platform</title>

        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <style>
            * {
                box-sizing: border-box;
            }

            body {
                font-family: Arial, sans-serif;
                background: #f4f7fb;
                margin: 0;
                color: #172554;
            }

            .header {
                background: #172554;
                color: white;
                padding: 30px;
                text-align: center;
            }

            .header h1 {
                margin: 0;
                font-size: 32px;
            }

            .header p {
                margin-top: 10px;
                color: #cbd5e1;
            }

            .container {
                width: 90%;
                max-width: 1200px;
                margin: 30px auto;
            }

            .status {
                background: #dcfce7;
                border-left: 6px solid #16a34a;
                padding: 20px;
                border-radius: 8px;
                margin-bottom: 25px;
            }

            .running {
                color: #16a34a;
                font-weight: bold;
            }

            .section-title {
                margin-top: 30px;
                margin-bottom: 15px;
            }

            .cards {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
                gap: 20px;
            }

            .card {
                background: white;
                padding: 22px;
                border-radius: 12px;
                box-shadow: 0 3px 12px rgba(0,0,0,0.08);
            }

            .card h3 {
                margin-top: 0;
                color: #172554;
            }

            .metric {
                font-size: 28px;
                font-weight: bold;
                margin: 10px 0;
            }

            .api {
                background: #172554;
                color: white;
            }

            .api a {
                color: #93c5fd;
                text-decoration: none;
                display: block;
                margin: 8px 0;
            }

            .monitoring-note {
                color: #64748b;
                margin-bottom: 15px;
            }

            .footer {
                text-align: center;
                padding: 25px;
                color: #64748b;
            }
        </style>
    </head>

    <body>

        <div class="header">
            <h1>☁️ CloudOps Enterprise Platform</h1>
            <p>Cloud Infrastructure Management & Monitoring</p>
        </div>

        <div class="container">

            <div class="status">
                <h2>
                    Application Status:
                    <span class="running">🟢 RUNNING</span>
                </h2>

                <p>
                    CloudOps application is running successfully.
                </p>
            </div>


            <h2 class="section-title">☁️ Infrastructure</h2>

            <div class="cards">

                <div class="card">
                    <h3>Cloud Provider</h3>
                    <p>AWS</p>
                    <p class="running">Active</p>
                </div>

                <div class="card">
                    <h3>Compute</h3>
                    <p>Amazon EC2</p>
                    <p class="running">Running</p>
                </div>

                <div class="card">
                    <h3>Container</h3>
                    <p>Docker</p>
                    <p class="running">Running</p>
                </div>

                <div class="card">
                    <h3>Environment</h3>
                    <p>Production</p>
                    <p class="running">Active</p>
                </div>

            </div>


            <h2 class="section-title">📊 Live System Monitoring</h2>

            <p class="monitoring-note">
                Metrics automatically refresh every 5 seconds.
            </p>

            <div class="cards">

                <div class="card">
                    <h3>CPU Usage</h3>
                    <div class="metric" id="cpu">Loading...</div>
                </div>

                <div class="card">
                    <h3>Memory Usage</h3>
                    <div class="metric" id="memory">Loading...</div>
                </div>

                <div class="card">
                    <h3>Disk Usage</h3>
                    <div class="metric" id="disk">Loading...</div>
                </div>

                <div class="card">
                    <h3>Operating System</h3>
                    <div class="metric" id="system">Loading...</div>
                    <p id="updated">Last updated: Loading...</p>
                </div>

            </div>


           <h2 class="section-title">🚀 Deployment Intelligence</h2>

<div class="cards">

    <div class="card">
        <h3>Deployment Status</h3>
        <p class="running">🟢 DEPLOYED</p>
    </div>

    <div class="card">
        <h3>Environment</h3>
        <p id="environment">Production</p>
    </div>

    <div class="card">
        <h3>Application Version</h3>
        <p id="version">Loading...</p>
    </div>

    <div class="card">
        <h3>Git Commit</h3>
        <p id="commit">Loading...</p>
    </div>

    <div class="card">
        <h3>Last Deployment</h3>
        <p id="deployed-at">Loading...</p>
    </div>

    <div class="card">
        <h3>CI/CD Pipeline</h3>
        <p>GitHub Actions</p>
        <p class="running">Active</p>
    </div>

</div>
            </div>


            <h2 class="section-title">🔗 Platform APIs</h2>

            <div class="card api">

                <h3>Available Services</h3>

                <a href="/health">Health Check →</a>
                <a href="/version">Version Information →</a>
                <a href="/deployment">Deployment Information →</a>
                <a href="/api/metrics">Live Metrics API →</a>

            </div>

        </div>

        <div class="footer">
            CloudOps Enterprise Platform • AWS • Docker • GitHub Actions
        </div>
        <!-- =========================================================
     CLOUDOPS OPERATIONS & MONITORING
     ========================================================= -->

<section class="section">

    <h2>Operations & Monitoring</h2>

    <!-- System Health -->
    <div class="cards">

        <div class="card">
            <h3>System Health</h3>
            <div id="ops-health">Checking...</div>
        </div>

        <div class="card">
            <h3>CPU Usage</h3>
            <div id="ops-cpu">--%</div>
        </div>

        <div class="card">
            <h3>Memory Usage</h3>
            <div id="ops-memory">--%</div>
        </div>

        <div class="card">
            <h3>Disk Usage</h3>
            <div id="ops-disk">--%</div>
        </div>

        <div class="card">
            <h3>Application Uptime</h3>
            <div id="ops-uptime">--</div>
        </div>

    </div>

    <!-- Alerts -->
    <div class="card">
        <h3>System Alerts</h3>

        <div id="ops-alerts">
            Checking system alerts...
        </div>
    </div>

    <!-- Logs -->
    <div class="card">
        <h3>Recent Application Logs</h3>

        <div id="ops-logs">
            Loading logs...
        </div>
    </div>

</section>


        <script>
            async function updateMetrics() {
                try {
                    const response = await fetch("/api/metrics");
                    const data = await response.json();

                    document.getElementById("cpu").textContent =
                        data.cpu + "%";

                    document.getElementById("memory").textContent =
                        data.memory + "%";

                    document.getElementById("disk").textContent =
                        data.disk + "%";

                    document.getElementById("system").textContent =
                        data.system;

                    document.getElementById("updated").textContent =
    "Last updated: " + data.updated;

                } catch (error) {
                    document.getElementById("cpu").textContent = "Unavailable";
                    document.getElementById("memory").textContent = "Unavailable";
                    document.getElementById("disk").textContent = "Unavailable";
                    document.getElementById("system").textContent = "Unavailable";
                }
            }
            updateMetrics();

            setInterval(updateMetrics, 5000);
            async function updateDeployment() {
    try {
        const response = await fetch("/api/deployment");
        const data = await response.json();

        document.getElementById("environment").textContent =
            data.environment;

        document.getElementById("version").textContent =
            data.version;

        document.getElementById("commit").textContent =
            data.commit;

        document.getElementById("deployed-at").textContent =
            data.deployed_at;

    } catch (error) {
        document.getElementById("environment").textContent =
            "Unavailable";

        document.getElementById("version").textContent =
            "Unavailable";

        document.getElementById("commit").textContent =
            "Unavailable";

        document.getElementById("deployed-at").textContent =
            "Unavailable";
    }
}

updateDeployment();
// ============================================================
// CLOUDOPS PART 1 — OPERATIONS DASHBOARD
// ============================================================

async function updateOperations() {
    try {
        const response = await fetch("/api/operations");
        const data = await response.json();

        // CPU
        const cpuElement = document.getElementById("ops-cpu");
        if (cpuElement) {
            cpuElement.textContent = data.metrics.cpu + "%";
        }

        // Memory
        const memoryElement = document.getElementById("ops-memory");
        if (memoryElement) {
            memoryElement.textContent = data.metrics.memory + "%";
        }

        // Disk
        const diskElement = document.getElementById("ops-disk");
        if (diskElement) {
            diskElement.textContent = data.metrics.disk + "%";
        }

        // Uptime
        const uptimeElement = document.getElementById("ops-uptime");
        if (uptimeElement) {
            uptimeElement.textContent = data.uptime;
        }

        // Overall health
        const healthElement = document.getElementById("ops-health");

        if (healthElement) {
            if (data.status === "healthy") {
                healthElement.textContent = "🟢 Healthy";
            } else {
                healthElement.textContent = "🔴 Unhealthy";
            }
        }

        // Alerts
        const alertsElement = document.getElementById("ops-alerts");

        if (alertsElement) {
            alertsElement.innerHTML = "";

            data.alerts.forEach(alert => {
                const item = document.createElement("div");

                item.style.padding = "8px";
                item.style.marginBottom = "6px";
                item.style.borderRadius = "6px";

                if (alert.type === "healthy") {
                    item.textContent = "🟢 " + alert.message;
                } else if (alert.type === "warning") {
                    item.textContent = "🟠 " + alert.message;
                } else {
                    item.textContent = "🔴 " + alert.message;
                }

                alertsElement.appendChild(item);
            });
        }

        // Logs
        const logsElement = document.getElementById("ops-logs");

        if (logsElement) {
            logsElement.innerHTML = "";

            data.logs.slice(-10).reverse().forEach(log => {
                const item = document.createElement("div");

                item.style.padding = "5px 0";
                item.textContent =
                    `[${log.time}] ${log.level}: ${log.message}`;

                logsElement.appendChild(item);
            });
        }

    } catch (error) {
        console.error("Operations monitoring error:", error);
    }
}


// Run immediately
updateOperations();

// Refresh every 5 seconds
setInterval(updateOperations, 5000);
        </script>

    </body>
    </html>
    """


@app.route("/health")
def health():
    return {
        "status": "healthy",
        "service": "CloudOps Enterprise Platform"
    }


@app.route("/version")
def version():
    return {
        "application": "CloudOps Enterprise Platform",
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "environment": os.getenv("APP_ENV", "production"),
        "commit": os.getenv("GIT_COMMIT", "unknown")
    }


@app.route("/deployment")
def deployment():
    return {
        "status": "deployed",
        "environment": os.getenv("APP_ENV", "production"),
        "platform": "AWS EC2",
        "container": "Docker",
        "ci_cd": "GitHub Actions",
        "commit": os.getenv("GIT_COMMIT", "unknown"),
        "deployed_at": os.getenv("DEPLOYED_AT", "unknown")
    }
@app.route("/api/deployment")
def deployment_api():
    return jsonify({
        "status": "deployed",
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "environment": os.getenv("APP_ENV", "production"),
        "commit": os.getenv("GIT_COMMIT", "unknown"),
        "deployed_at": os.getenv("DEPLOYED_AT", "unknown"),
        "platform": "AWS EC2",
        "container": "Docker",
        "ci_cd": "GitHub Actions"
    })


@app.route("/api/metrics")
def metrics():
    return jsonify({
        "cpu": psutil.cpu_percent(interval=0.5),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage("/").percent,
        "system": platform.system(),
        "updated": __import__("datetime").datetime.now().strftime("%H:%M:%S")
    })

# ============================================================
# CLOUDOPS PART 1 — OPERATIONS & MONITORING
# ============================================================

import logging
import time
import platform
from collections import deque

import psutil

# Application start time
APP_START_TIME = time.time()

# Store recent application logs
recent_logs = deque(maxlen=50)


class RecentLogHandler(logging.Handler):
    def emit(self, record):
        try:
            log_entry = {
                "time": time.strftime("%H:%M:%S"),
                "level": record.levelname,
                "message": record.getMessage()
            }
            recent_logs.append(log_entry)
        except Exception:
            pass


# Configure application logging
cloudops_logger = logging.getLogger("cloudops")
cloudops_logger.setLevel(logging.INFO)

if not cloudops_logger.handlers:
    cloudops_logger.addHandler(RecentLogHandler())


def get_uptime():
    """Return application uptime in seconds."""
    return int(time.time() - APP_START_TIME)


def format_uptime(seconds):
    """Convert seconds into readable uptime."""
    days = seconds // 86400
    hours = (seconds % 86400) // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    if days > 0:
        return f"{days}d {hours}h {minutes}m"

    if hours > 0:
        return f"{hours}h {minutes}m {secs}s"

    return f"{minutes}m {secs}s"


def get_system_metrics():
    """Collect current system resource information."""
    cpu = psutil.cpu_percent(interval=0.5)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    return {
        "cpu": round(cpu, 1),
        "memory": round(memory.percent, 1),
        "disk": round(disk.percent, 1),
        "memory_used_gb": round(memory.used / (1024 ** 3), 2),
        "memory_total_gb": round(memory.total / (1024 ** 3), 2),
        "disk_used_gb": round(disk.used / (1024 ** 3), 2),
        "disk_total_gb": round(disk.total / (1024 ** 3), 2),
        "platform": platform.system(),
        "hostname": platform.node()
    }


def get_alerts(metrics):
    """Generate alerts when resource usage crosses thresholds."""
    alerts = []

    if metrics["cpu"] >= 80:
        alerts.append({
            "type": "warning",
            "service": "CPU",
            "message": f"High CPU usage: {metrics['cpu']}%"
        })

    if metrics["memory"] >= 80:
        alerts.append({
            "type": "warning",
            "service": "Memory",
            "message": f"High memory usage: {metrics['memory']}%"
        })

    if metrics["disk"] >= 80:
        alerts.append({
            "type": "warning",
            "service": "Disk",
            "message": f"High disk usage: {metrics['disk']}%"
        })

    if not alerts:
        alerts.append({
            "type": "healthy",
            "service": "System",
            "message": "All monitored resources are within normal limits."
        })

    return alerts


@app.route("/api/operations")
def operations():
    """Return complete Operations & Monitoring information."""

    try:
        metrics = get_system_metrics()
        alerts = get_alerts(metrics)

        cloudops_logger.info("Operations metrics updated")

        return {
            "status": "healthy",
            "service": "CloudOps Enterprise Platform",
            "uptime_seconds": get_uptime(),
            "uptime": format_uptime(get_uptime()),
            "metrics": metrics,
            "alerts": alerts,
            "logs": list(recent_logs)[-20:],
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }

    except Exception as e:
        cloudops_logger.error(f"Operations monitoring error: {str(e)}")

        return {
            "status": "unhealthy",
            "error": str(e),
            "uptime": format_uptime(get_uptime()),
            "alerts": [{
                "type": "error",
                "service": "Operations",
                "message": "Monitoring system encountered an error."
            }],
            "logs": list(recent_logs)[-20:]
        }, 500


@app.route("/api/system")
def system_status():
    """Return current system metrics."""
    try:
        metrics = get_system_metrics()

        return {
            "status": "healthy",
            "metrics": metrics,
            "uptime": format_uptime(get_uptime())
        }

    except Exception as e:
        return {
            "status": "unhealthy",
            "error": str(e)
        }, 500


@app.route("/api/alerts")
def alerts_status():
    """Return current system alerts."""
    try:
        metrics = get_system_metrics()

        return {
            "status": "success",
            "alerts": get_alerts(metrics)
        }

    except Exception as e:
        return {
            "status": "error",
            "alerts": [{
                "type": "error",
                "service": "Monitoring",
                "message": str(e)
            }]
        }, 500


@app.route("/api/logs")
def application_logs():
    """Return recent application logs."""

    return {
        "status": "success",
        "logs": list(recent_logs)[-20:]
    }


cloudops_logger.info("CloudOps Operations & Monitoring module initialized")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)