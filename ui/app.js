document.addEventListener('DOMContentLoaded', () => {
    const uploadForm = document.getElementById('upload-form');
    const roleSelect = document.getElementById('role-select');

    uploadForm.addEventListener('submit', handleUpload);
    roleSelect.addEventListener('change', updateRoleDescription);
});

const ROLE_DESCRIPTIONS = {
    "AI Engineer": "Builds and deploys scalable AI/ML systems and agents.",
    "Machine Learning Engineer": "Focuses on training, optimizing, and deploying ML models.",
    "Data Scientist": "Analyzes complex data to derive insights and build predictive models.",
    "Data Analyst": "Interprets data using statistical techniques and visualization tools.",
    "Backend Engineer": "Designs robust server-side logic, APIs, and database architectures.",
    "Full Stack Developer": "Handles both frontend interfaces and backend system logic.",
    "DevOps Engineer": "Manages infrastructure, CI/CD pipelines, and cloud deployment.",
    "Software Engineer": "Develops general-purpose software solutions with strong CS fundamentals."
};

function updateRoleDescription() {
    const role = document.getElementById('role-select').value;
    const desc = ROLE_DESCRIPTIONS[role] || "Select a role to see details.";
    const descEl = document.getElementById('role-description');

    // Fade animation effect
    descEl.style.opacity = 0;
    setTimeout(() => {
        descEl.textContent = desc;
        descEl.style.opacity = 1;
    }, 200);
}

async function handleUpload(e) {
    e.preventDefault();

    const fileInput = document.getElementById('resume-file');
    const file = fileInput.files[0];
    const role = document.getElementById('role-select').value;

    if (!file || !role) {
        alert("Please select a role and upload a resume.");
        return;
    }

    // UI Updates
    document.getElementById('upload-btn').classList.add('hidden');
    document.getElementById('loading-indicator').classList.remove('hidden');

    const formData = new FormData();
    formData.append('file', file);
    formData.append('target_role', role);

    try {
        const response = await fetch('/upload_resume', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) throw new Error("Upload failed");

        const data = await response.json();

        // Transition to Dashboard
        showDashboard(data);

    } catch (err) {
        alert("Error: " + err.message);
        document.getElementById('upload-btn').classList.remove('hidden');
        document.getElementById('loading-indicator').classList.add('hidden');
    }
}

function showDashboard(data) {
    document.getElementById('upload-screen').classList.add('hidden');
    document.getElementById('dashboard-screen').classList.remove('hidden');
    document.getElementById('header-status').classList.remove('hidden');

    // Header
    // Header
    const profile = data.profile || {};
    // current_role might be inferred or default, target_role comes from input
    document.getElementById('user-role').textContent = profile.current_role || "Candidate";
    document.getElementById('target-role').textContent = profile.target_role || "Target Role";

    // 1. Render Charts/Scores
    renderScore(data.convergence);

    // 2. Render Lists
    renderSkills(data.verified_skills);
    renderGaps(data.gaps);
    renderRoadmap(data.roadmap);

    // 3. Animate Logs
    animateLogs(data.logs);
}

function renderScore(value) {
    const score = (value || 0) * 100;
    document.getElementById('score-value').textContent = Math.round(score) + "%";
    document.getElementById('score-ring').setAttribute("stroke-dasharray", `${score}, 100`);
    const color = score > 80 ? 'var(--success)' : (score > 40 ? 'var(--warning)' : 'var(--danger)');
    document.getElementById('score-ring').style.stroke = color;
}

function renderSkills(skills) {
    const container = document.getElementById('skills-list');
    container.innerHTML = '';
    for (const [skill, level] of Object.entries(skills || {})) {
        const span = document.createElement('span');
        span.className = `tag ${level}`;
        span.textContent = `${skill} (${level})`;
        container.appendChild(span);
    }
}

function renderGaps(gaps) {
    const tbody = document.querySelector('#gaps-table tbody');
    tbody.innerHTML = '';
    (gaps || []).forEach(gap => {
        const tr = document.createElement('tr');
        tr.innerHTML = `<td>${gap.skill}</td><td class="severity-${gap.severity}">${gap.severity}</td>`;
        tbody.appendChild(tr);
    });
}

function renderRoadmap(roadmap) {
    const container = document.getElementById('roadmap-timeline');
    container.innerHTML = '';
    (roadmap || []).forEach(phase => {
        const div = document.createElement('div');
        div.className = 'timeline-item';
        div.innerHTML = `
            <div class="phase-step">${phase.phase}</div>
            <div class="phase-content">
                <h4>${phase.goal}</h4>
                <p style="color:var(--text-muted); font-size:0.8rem">Duration: ${phase.duration_months} Months</p>
                <p style="margin-top:0.5rem; font-size:0.9rem">${phase.milestones.join('<br>')}</p>
            </div>
        `;
        container.appendChild(div);
    });
}

function animateLogs(logs) {
    const list = document.getElementById('agent-timeline');
    list.innerHTML = '';
    let index = 0;

    function next() {
        if (index >= logs.length) return;
        const log = logs[index];
        const li = document.createElement('li');
        li.className = 'agent-item';
        li.innerHTML = `<strong>${log.agent}</strong><br>${log.action}`;
        list.appendChild(li);
        list.scrollTop = list.scrollHeight;
        index++;
        setTimeout(next, 500);
    }
    next();
}
