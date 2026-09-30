from flask import Flask, jsonify
import psutil
import platform

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
                </div>

            </div>


            <h2 class="section-title">🚀 Deployment</h2>

            <div class="cards">

                <div class="card">
                    <h3>Deployment Status</h3>
                    <p class="running">🟢 Deployed</p>
                </div>

                <div class="card">
                    <h3>CI/CD</h3>
                    <p>GitHub Actions</p>
                    <p class="running">Active</p>
                </div>

                <div class="card">
                    <h3>Application Version</h3>
                    <p>1.0.0</p>
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

                } catch (error) {
                    document.getElementById("cpu").textContent = "Unavailable";
                    document.getElementById("memory").textContent = "Unavailable";
                    document.getElementById("disk").textContent = "Unavailable";
                    document.getElementById("system").textContent = "Unavailable";
                }
            }

            updateMetrics();

            setInterval(updateMetrics, 5000);
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
        "version": "1.0.0",
        "environment": "production"
    }


@app.route("/deployment")
def deployment():
    return {
        "status": "deployed",
        "environment": "production",
        "platform": "AWS EC2",
        "container": "Docker",
        "ci_cd": "GitHub Actions"
    }


@app.route("/api/metrics")
def metrics():
    return jsonify({
        "cpu": psutil.cpu_percent(interval=0.5),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage("/").percent,
        "system": platform.system()
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)