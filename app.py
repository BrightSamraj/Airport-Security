import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Airport Security Architecture", layout="wide")

# HTML + CSS + JS combined as one giant component
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />

  <title>Airport Security Architecture — Interactive Demo</title>

  <!-- Styles -->
  <style>
    :root{
      --bg:#f4f8ff; --card:#ffffff; --text:#0b1a2b; --muted:#556;
      --accent:#0b63ff; --danger:#d9534f; --glass: rgba(255,255,255,0.7);
    }
    body.dark { --bg:#0b1220; --card:#0f1720; --text:#e6eef8; --muted:#9aa; --glass: rgba(0,0,0,0.5); }

    body{
      margin:0; font-family:Inter, system-ui;
      background:var(--bg); color:var(--text); transition:0.3s;
    }

    /* Top controls */
    .top-controls{
      position:fixed; right:20px; top:20px; z-index:200; display:flex; gap:8px;
    }
    .control-btn{
      background:var(--card); border:1px solid rgba(0,0,0,0.06);
      padding:8px; border-radius:8px; cursor:pointer;
    }

    /* Hero */
    .hero{
      padding:32px; text-align:center;
      background:linear-gradient(90deg,#0b63ff,#00bcd4);
      color:white;
    }
    .subtitle{ opacity:0.9 }

    /* Navigation */
    .main-nav{
      display:flex; gap:10px; flex-wrap:wrap; justify-content:center;
      background:var(--card); padding:12px; position:sticky; top:0; z-index:100;
      box-shadow:0 4px 20px rgba(0,0,0,0.08);
    }
    .main-nav button{
      background:transparent; padding:8px 12px; border-radius:6px; cursor:pointer;
      border:1px solid rgba(0,0,0,0.08); color:var(--text);
    }

    /* Sections */
    .content{ max-width:1200px; margin:auto; padding:20px;}
    .section{ display:none; }
    .section.active{ display:block; }

    .wide-card{
      background:var(--card); border-radius:12px;
      box-shadow:0 8px 30px rgba(0,0,0,0.08); overflow:hidden;
    }
    .wide-card img{ width:100%; height:320px; object-fit:cover; }
    .wide-card-caption{ padding:12px; font-weight:600; color:var(--muted); }

    .card-grid{ display:flex; flex-wrap:wrap; gap:16px; }
    .device-card{
      width:300px; background:var(--card);
      border-radius:12px; box-shadow:0 10px 25px rgba(0,0,0,0.05);
      padding:12px; transition:0.2s;
    }
    .device-card:hover{ transform:translateY(-5px); }
    .device-card img{ width:100%; height:170px; object-fit:cover; border-radius:8px; }

    .detail-box{
      display:none; background:var(--glass);
      padding:10px; border-radius:8px; margin-top:8px;
    }
    .detail-box img{ width:100%; margin-top:8px; border-radius:8px; }

    .diagram img{ width:100%; border-radius:12px }

    .console, .sim-panel, .install-result{
      background:var(--card); padding:12px; border-radius:10px; margin-top:12px;
      box-shadow:0 4px 12px rgba(0,0,0,0.08);
    }

    /* Attack **/
    .sim-stage{
      opacity:0.3; transform:translateX(-10px);
      background:var(--card); border-left:6px solid var(--danger);
      padding:8px; border-radius:6px; margin:10px 0; font-weight:600;
    }
    .sim-panel{ border:2px solid var(--danger); }

    /* Hidden */
    .hidden{ display:none; }
  </style>
</head>

<body>

  <!-- TOP BUTTONS -->
  <div class="top-controls">
    <button id="darkToggle" class="control-btn">🌙</button>
    <button id="muteToggle" class="control-btn">🔊</button>
  </div>

  <!-- HERO -->
  <header class="hero">
    <h1>🛫 Airport Security Architecture</h1>
    <p class="subtitle">Interactive simulation • Devices • Workflow • Threat Detection</p>
  </header>

  <!-- NAVIGATION -->
  <nav class="main-nav">
    <button onclick="showSection('home')">Home</button>
    <button onclick="showSection('architecture')">Architecture</button>
    <button onclick="showSection('perimeter')">Perimeter</button>
    <button onclick="showSection('access')">Access Control</button>
    <button onclick="showSection('screening')">Screening</button>
    <button onclick="showSection('baggage')">Baggage</button>
    <button onclick="showSection('cyber')">Cyber Ops</button>
    <button onclick="showSection('ai')">AI & IoT</button>
    <button onclick="showSection('vendors')">Vendors</button>
    <button onclick="showSection('install')">Install Flow</button>
    <button onclick="showSection('attackSim')">🚨 Attack Simulation</button>
  </nav>

  <main class="content">

    <!-- HOME -->
    <section id="home" class="section active">
      <h2>Welcome 👋</h2>
      <p>This interactive demo shows modern airport multilayered security systems.</p>
      <div class="wide-card">
        <img src="https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?auto=format&w=1400&q=80"/>
        <div class="wide-card-caption">Defense-in-Depth: Protecting Airports End-to-End</div>
      </div>
    </section>

    <!-- ARCHITECTURE -->
    <section id="architecture" class="section">
      <h2>Architecture Blueprint</h2>
      <div class="diagram">
        <img src="https://i.imgur.com/SwXdNpl.png" />
      </div>
    </section>

    <!-- PERIMETER -->
    <section id="perimeter" class="section">
      <h2>Perimeter & Entry Security</h2>

      <div class="card-grid">

        <!-- Camera -->
        <div class="device-card">
          <img src="https://images.unsplash.com/photo-1581091870625-6f5b8f9de7e2?auto=format&w=800&q=80">
          <h3>PTZ IP Camera</h3>
          <button onclick="toggleDetails('ptz')">Details</button>
          <div id="ptz" class="detail-box">
            <p><b>How it works:</b> Auto tracking + AI motion detection.</p>
            <p><b>Install:</b> PoE → NVR → SIEM.</p>
          </div>
        </div>

        <!-- Fiber Sensor -->
        <div class="device-card">
          <img src="https://images.unsplash.com/photo-1518091043644-c1d4457512c6?auto=format&w=800&q=80">
          <h3>Fiber Fence Sensor</h3>
          <button onclick="toggleDetails('fiber')">Details</button>
          <div id="fiber" class="detail-box">
            <p>Detects vibration, cutting & climbing attempts.</p>
          </div>
        </div>

        <!-- Barriers -->
        <div class="device-card">
          <img src="https://images.unsplash.com/photo-1549924231-f129b911e442?auto=format&w=800&q=80">
          <h3>Vehicle Barrier + LPR</h3>
          <button onclick="toggleDetails('lpr')">Details</button>
          <div id="lpr" class="detail-box">
            <p>Reads license plates & controls barrier access.</p>
          </div>
        </div>

      </div>
    </section>

    <!-- ACCESS CONTROL -->
    <section id="access" class="section">
      <h2>Access Control</h2>

      <button onclick="runMfa()">Run MFA Demo</button>
      <div id="mfaConsole" class="console hidden"></div>
    </section>

    <!-- SCREENING -->
    <section id="screening" class="section">
      <h2>Passenger Screening</h2>

      <div class="card-grid">
        <div class="device-card">
          <img src="https://images.unsplash.com/photo-1566150907522-1f3c9fc44e0e?auto=format&w=800&q=80">
          <h3>Body Scanner</h3>
        </div>
        <div class="device-card">
          <img src="https://images.unsplash.com/photo-1526772662000-3f88f10405ff?auto=format&w=800&q=80">
          <h3>CT Bag Scanner</h3>
        </div>
      </div>
    </section>

    <!-- BAGGAGE -->
    <section id="baggage" class="section">
      <h2>Baggage Screening</h2>
      <div class="wide-card">
        <img src="https://images.unsplash.com/photo-1568667256549-0945f9a0cb0f?auto=format&w=1400&q=80"/>
      </div>
    </section>

    <!-- CYBER -->
    <section id="cyber" class="section">
      <h2>Cyber Command Center</h2>

      <div id="logs" class="console" style="height:220px; overflow:auto;"></div>
    </section>

    <!-- AI -->
    <section id="ai" class="section">
      <h2>AI & IoT Layer</h2>

      <div class="card-grid">
        <div class="device-card">
          <img src="https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&w=800&q=80">
          <h3>AI Video Analytics</h3>
        </div>

        <div class="device-card">
          <img src="https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&w=800&q=80">
          <h3>IoT Sensors</h3>
        </div>
      </div>
    </section>

    <!-- VENDORS -->
    <section id="vendors" class="section">
      <h2>Vendor Matrix</h2>
      <ul>
        <li>Hikvision — AI Cameras</li>
        <li>Honeywell — Perimeter & BMS</li>
        <li>Smiths Detection — Screening</li>
        <li>Splunk — SIEM</li>
        <li>Fortinet — Firewalls</li>
      </ul>
    </section>

    <!-- INSTALL FLOW -->
    <section id="install" class="section">
      <h2>Install Flow Simulation</h2>
      <button onclick="runInstall()">Run Install Flow</button>
      <div id="installResult" class="install-result"></div>
    </section>

    <!-- ATTACK SIMULATION -->
    <section id="attackSim" class="section">
      <h2>🚨 Attack → Detection Simulation</h2>

      <button id="attackBtn" style="background:#d9534f; padding:8px; border-radius:6px; color:white;">Launch Attack</button>
      <button id="resetBtn" style="margin-left:10px">Reset</button>

      <div id="simPanel" class="sim-panel hidden">
        <div id="stage1" class="sim-stage">1) Suspicious Activity from Unknown IP</div>
        <div id="stage2" class="sim-stage">2) IDS Triggered (Snort)</div>
        <div id="stage3" class="sim-stage">3) SIEM Correlation (Splunk)</div>
        <div id="stage4" class="sim-stage">4) Firewall Block Applied</div>
        <div id="stage5" class="sim-stage">5) SOC Team Notified</div>
      </div>
    </section>

  </main>

  <!-- AUDIO -->
  <audio id="alertSound" src="https://actions.google.com/sounds/v1/alarms/alarm_clock.ogg"></audio>
  <audio id="clickSound" src="https://actions.google.com/sounds/v1/buttons/button_push.ogg"></audio>

  <!-- JS -->
  <script>
    function showSection(id){
      document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));
      document.getElementById(id).classList.add('active');
    }

    function toggleDetails(id){
      const el = document.getElementById(id);
      el.style.display = (el.style.display === 'block') ? 'none' : 'block';
    }

    function isMuted(){ return localStorage.getItem('muted') === 'true'; }
    function playClick(){ if(!isMuted()) document.getElementById('clickSound').play(); }
    function playAlert(){ if(!isMuted()) document.getElementById('alertSound').play(); }

    document.getElementById('darkToggle').onclick = () => {
      document.body.classList.toggle('dark');
      localStorage.setItem('theme', document.body.classList.contains('dark') ? 'dark' : 'light');
    };

    document.getElementById('muteToggle').onclick = () => {
      localStorage.setItem('muted', isMuted() ? 'false' : 'true');
      playClick();
    };

    // MFA Demo
    function runMfa(){
      playClick();
      const c = document.getElementById('mfaConsole');
      c.classList.remove('hidden');
      c.innerHTML = '';
      const steps = [
        "RFID Badge Detected",
        "Face Recognized (98% match)",
        "LDAP Authentication Success",
        "Door Unlocked & Logged"
      ];
      let i = 0;
      const id = setInterval(()=>{
        if(i>=steps.length){clearInterval(id); return;}
        c.innerHTML += "<div>"+steps[i]+"</div>";
        i++;
      },700);
    }

    // Install Flow
    function runInstall(){
      playClick();
      const out = document.getElementById('installResult');
      out.innerHTML = "";
      const steps = [
        "VLAN Setup Completed",
        "Cameras Connected to PoE Switch",
        "NVR Configured",
        "SIEM Log Parsing Enabled",
        "System Integration Completed"
      ];
      let i=0;
      const t = setInterval(()=>{
        if(i>=steps.length){clearInterval(t); return;}
        out.innerHTML += "<div>"+steps[i]+"</div>";
        i++;
      },700);
    }

    // Attack Simulation
    const attackBtn = document.getElementById("attackBtn");
    const resetBtn = document.getElementById("resetBtn");
    const simPanel = document.getElementById("simPanel");

    attackBtn.onclick = () => {
      playAlert();
      simPanel.classList.remove('hidden');
      ["stage1","stage2","stage3","stage4","stage5"].forEach((id,i)=>{
        setTimeout(()=>{
          document.getElementById(id).style.opacity = 1;
        }, 900*i);
      });
    };

    resetBtn.onclick = () => {
      playClick();
      simPanel.classList.add("hidden");
      ["stage1","stage2","stage3","stage4","stage5"].forEach(id=>{
        document.getElementById(id).style.opacity = 0.3;
      });
    };
  </script>

</body>
</html>
"""

# Streamlit renders the entire HTML app
components.html(html_code, height=3000, scrolling=True)
