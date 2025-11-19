// Wait for DOM to load
document.addEventListener('DOMContentLoaded', function () {
  // elements
  const sections = document.querySelectorAll('.section');
  const darkToggle = document.getElementById('darkToggle');
  const muteToggle = document.getElementById('muteToggle') || null;
  const startAttackBtn = document.getElementById('startAttack');
  const stopAttackBtn = document.getElementById('stopAttack');
  const alertSound = document.getElementById('alertSound');
  const clickSound = document.getElementById('clickSound');
  const simPanel = document.getElementById('simPanel');
  const logs = document.getElementById('logs');
  const installResult = document.getElementById('installResult');

  // small helper: play click
  function playClick(){ if (!isMuted()) clickSound.play().catch(()=>{}); }
  function playAlert(){ if (!isMuted()) alertSound.play().catch(()=>{}); }

  // theme
  function isDark() { return document.body.classList.contains('dark'); }
  function isMuted() { return localStorage.getItem('muted') === 'true'; }

  // Initialize theme
  if (localStorage.getItem('theme') === 'dark') {
    document.body.classList.add('dark');
    darkToggle.textContent = '☀️';
  } else {
    darkToggle.textContent = '🌙';
  }

  // Initialize mute
  if (isMuted()) {
    document.getElementById('muteToggle').checked = true;
    muteToggle && (document.getElementById('muteToggle').parentElement.querySelector('label')?.classList.add('muted'));
  }

  // Section switching (global function used in HTML)
  window.showSection = function(id) {
    playClick();
    sections.forEach(s => s.classList.remove('active'));
    const el = document.getElementById(id);
    if (el) el.classList.add('active');
  };

  // Toggle detail boxes (global function used in HTML)
  window.toggleDetails = function(id) {
    playClick();
    const el = document.getElementById(id);
    if (!el) return;
    el.style.display = (el.style.display === 'block') ? 'none' : 'block';
  };

  // MFA Demo
  window.showMfaDemo = function(){
    playClick();
    const consoleEl = document.getElementById('mfaConsole');
    consoleEl.classList.remove('hidden');
    consoleEl.innerHTML = ''; // clear
    const steps = [
      'Badge tapped: ID=EMP-4379',
      'Face sensor: match confidence 98%',
      'LDAP validation: user active',
      'Door unlocked, event logged to SIEM'
    ];
    let i = 0;
    const t = setInterval(()=>{
      if (i >= steps.length) { clearInterval(t); return; }
      const p = document.createElement('div');
      p.textContent = `[MFA] ${steps[i]}`;
      consoleEl.appendChild(p);
      i++;
    },700);
  };

  // Install simulation
  window.simulateInstall = function(){
    playClick();
    installResult.innerHTML = 'Running install simulation...';
    const steps = [
      '1) Plan network segmentation & VLANs',
      '2) Physically place cameras & sensors',
      '3) Connect PoE cameras to NVR and VLAN',
      '4) Configure SIEM log ingestion (Splunk rules)',
      '5) Perform acceptance tests'
    ];
    installResult.innerHTML = '';
    let idx = 0;
    const id = setInterval(()=>{
      if (idx >= steps.length){ clearInterval(id); installResult.innerHTML += '<div style="margin-top:8px;color:green;font-weight:700">Simulation complete ✅</div>'; return; }
      const d = document.createElement('div');
      d.textContent = steps[idx];
      installResult.appendChild(d);
      idx++;
    },800);
  };

  // Logs helper (for cyber section and sim)
  function pushLog(text){
    const d = document.createElement('div');
    const ts = new Date().toLocaleTimeString();
    d.textContent = `[${ts}] ${text}`;
    logs && logs.prepend(d);
  }

  // Attack simulation
  if (startAttackBtn) {
    startAttackBtn.addEventListener('click', ()=> {
      playAlert();
      simPanel.classList.remove('hidden');
      // animated reveal of stages + logs
      const stages = [
        {id:'stage1', text:'Suspicious outgoing traffic from 203.0.113.11'},
        {id:'stage2', text:'IDS signature match: possible camera exploit'},
        {id:'stage3', text:'SIEM correlates multiple camera alerts'},
        {id:'stage4', text:'Firewall rule auto-created to block IP'},
        {id:'stage5', text:'SOC notified via pagers; containment initiated'}
      ];
      let i = 0;
      // hide all stages initially
      stages.forEach(s=>{ const el = document.getElementById(s.id); if (el) el.style.opacity = 0.2; });
      const seq = setInterval(()=>{
        if (i >= stages.length) { clearInterval(seq); return; }
        const s = stages[i];
        const el = document.getElementById(s.id);
        if (el) {
          el.style.opacity = 1;
          el.style.transform = 'translateX(0)';
        }
        pushLog(s.text);
        i++;
      },900);
    });
  }

  if (stopAttackBtn) {
    stopAttackBtn.addEventListener('click', ()=> {
      playClick();
      // reset sim panel & stages opacity
      simPanel.classList.add('hidden');
      ['stage1','stage2','stage3','stage4','stage5'].forEach(id=>{
        const el = document.getElementById(id);
        if (el){ el.style.opacity = 0.2; el.style.transform = 'translateX(-10px)'; }
      });
      logs && pushLog('Simulation reset by user.');
      alertSound.pause(); alertSound.currentTime = 0;
    });
  }

  // Dark mode toggle
  darkToggle.addEventListener('click', ()=>{
    playClick();
    document.body.classList.toggle('dark');
    localStorage.setItem('theme', document.body.classList.contains('dark') ? 'dark' : 'light');
    darkToggle.textContent = document.body.classList.contains('dark') ? '☀️' : '🌙';
  });

  // Mute toggle
  const muteCheckbox = document.getElementById('toggleMute');
  if (muteCheckbox) {
    muteCheckbox.addEventListener('change', (e)=>{
      const muted = e.target.checked;
      localStorage.setItem('muted', muted ? 'true' : 'false');
      if (muted) { alertSound.pause(); alertSound.currentTime = 0; }
    });
  }

  // Also ensure pressing any main nav plays click
  document.querySelectorAll('.main-nav button').forEach(b=>{
    b.addEventListener('click', ()=>playClick());
  });

}); // DOMContentLoaded end
