from flask import Flask
import psutil
import platform
system = platform.system()

app = Flask(__name__)


@app.route("/")
def home():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    system = psutil.sys.platform
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>CloudOps Enterprise Platform</title>

        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f7fb;
                margin: 0;
                padding: 0;
            }

            .header {
                background-color: #172554;
                color: white;
                padding: 25px;
                text-align: center;
            }

            .container {
                width: 85%;
                margin: 30px auto;
            }

            .status {
                background-color: #dcfce7;
                border-left: 6px solid #16a34a;
                padding: 20px;
                margin-bottom: 25px;
            }

            .cards {
                display: flex;
                gap: 20px;
                flex-wrap: wrap;
            }

            .card {
                background-color: white;
                padding: 20px;
                flex: 1;
                min-width: 200px;
                border-radius: 10px;
                box-shadow: 0 3px 10px rgba(0,0,0,0.1);
            }

            .card h3 {
                margin-top: 0;
            }

            .running {
                color: #16a34a;
                font-weight: bold;
            }
        </style>
    </head>

    <body>

        <div class="header">
            <h1>☁️ CloudOps Enterprise Platform</h1>
            <p>Cloud Infrastructure Management Dashboard</p>
        </div>

        <div class="container">

            <div class="status">
                <h2>Application Status: <span class="running">🟢 RUNNING</span></h2>
                <p>The CloudOps application is currently running successfully.</p>
            </div>

            <div class="cards">

               <div class="card">
                <h3>📊 Monitoring</h3>
                <p>CPU Usage: """ + str(cpu) + """%</p>
                <p>Memory Usage: """ + str(memory) + """%</p>
                <p>Disk Usage: """ + str(disk) + """%</p>
                <p>System: """ + system + """</p>
            </div>

                <div class="card">
                    <h3>🚀 Deployment</h3>
                    <p>Environment: Development</p>
                    <p>Status: <span class="running">Active</span></p>
                </div>

                <div class="card">
                    <h3>📊 Monitoring</h3>
                    <p>Monitoring: Enabled</p>
                    <p>Status: <span class="running">Healthy</span></p>
                </div>

            </div>

        </div>

    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)