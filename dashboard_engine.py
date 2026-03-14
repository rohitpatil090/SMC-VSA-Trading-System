
import pandas as pd
from datetime import datetime, timezone

def generate_dashboard(data):
    html_content = f'''
    <html>
    <head>
        <title>SMC-VSA Analysis Dashboard</title>
        <style>
            body {{ font-family: Arial, sans-serif; background: #121212; color: white; padding: 20px; }}
            .card {{ background: #1e1e1e; border: 1px solid #333; padding: 15px; margin-bottom: 10px; border-radius: 8px; }}
            .high {{ border-left: 5px solid #00ff00; }}
            .header {{ font-size: 24px; color: #00d2ff; }}
            .meta {{ font-size: 12px; color: #888; }}
        </style>
    </head>
    <body>
        <div class="header">Institutional Command Center Analysis</div>
        <div class="meta">Report Generated: {datetime.now(timezone.utc)}</div>
        <hr>
    '''
    for _, row in data.iterrows():
        html_content += f'''
        <div class="card high">
            <h3>Symbol: {row['name']}</h3>
            <p><b>Relative Volume:</b> {row['relative_volume_10d_calc']:.2f}</p>
            <p><b>Potential Setup:</b> Analysis based on SMC/VSA architecture...</p>
        </div>
        '''
    html_content += "</body></html>"
    with open("report.html", "w") as f:
        f.write(html_content)
    print("✨ Beautiful HTML Dashboard generated: report.html")

# Scanner Logic...
