"""
Ontology & Counterfactual Reasoning Demo - Streamlit Page
Demonstrates structured knowledge and "what if" analysis
"""

import streamlit as st
import plotly.graph_objects as go
from openai import OpenAI
import json

# =============================================================================
# ONTOLOGY DEFINITION
# =============================================================================

ONTOLOGY = {
    "assets": {
        "Customer Data": {
            "description": "Personal and financial information of customers",
            "criticality": "High",
            "examples": ["PII", "Credit card numbers", "Account credentials"]
        },
        "Internal Systems": {
            "description": "Core business applications and databases",
            "criticality": "High", 
            "examples": ["ERP", "CRM", "HR systems"]
        },
        "Network Infrastructure": {
            "description": "Routers, switches, and connectivity",
            "criticality": "Medium",
            "examples": ["Firewalls", "VPN gateways", "DNS servers"]
        }
    },
    
    "threats": {
        "Ransomware": {
            "description": "Malware that encrypts data and demands payment",
            "targets": ["Customer Data", "Internal Systems"],
            "likelihood": "High",
            "impact": "Severe"
        },
        "Phishing": {
            "description": "Social engineering to steal credentials",
            "targets": ["Customer Data", "Internal Systems"],
            "likelihood": "High",
            "impact": "Moderate"
        },
        "Insider Threat": {
            "description": "Malicious or negligent employee actions",
            "targets": ["Customer Data", "Internal Systems"],
            "likelihood": "Medium",
            "impact": "Severe"
        },
        "DDoS Attack": {
            "description": "Distributed denial of service disrupting availability",
            "targets": ["Network Infrastructure", "Internal Systems"],
            "likelihood": "Medium",
            "impact": "Moderate"
        }
    },
    
    "controls": {
        "Multi-Factor Authentication": {
            "description": "Requires multiple forms of identity verification",
            "mitigates": ["Phishing", "Insider Threat"],
            "effectiveness": "High",
            "status": "Active"
        },
        "Endpoint Detection & Response": {
            "description": "Monitors and responds to threats on devices",
            "mitigates": ["Ransomware", "Insider Threat"],
            "effectiveness": "High",
            "status": "Active"
        },
        "Network Firewall": {
            "description": "Filters traffic between network segments",
            "mitigates": ["Ransomware", "DDoS Attack"],
            "effectiveness": "Medium",
            "status": "Active"
        },
        "Security Awareness Training": {
            "description": "Educates employees on security best practices",
            "mitigates": ["Phishing", "Insider Threat"],
            "effectiveness": "Medium",
            "status": "Active"
        },
        "Offline Backups": {
            "description": "Air-gapped copies of critical data",
            "mitigates": ["Ransomware"],
            "effectiveness": "High",
            "status": "Active"
        }
    }
}

RELATIONSHIPS = [
    ("Ransomware", "Customer Data", "targets"),
    ("Ransomware", "Internal Systems", "targets"),
    ("Phishing", "Customer Data", "targets"),
    ("Phishing", "Internal Systems", "targets"),
    ("Insider Threat", "Customer Data", "targets"),
    ("Insider Threat", "Internal Systems", "targets"),
    ("DDoS Attack", "Network Infrastructure", "targets"),
    ("DDoS Attack", "Internal Systems", "targets"),
    ("Multi-Factor Authentication", "Phishing", "mitigates"),
    ("Multi-Factor Authentication", "Insider Threat", "mitigates"),
    ("Endpoint Detection & Response", "Ransomware", "mitigates"),
    ("Endpoint Detection & Response", "Insider Threat", "mitigates"),
    ("Network Firewall", "Ransomware", "mitigates"),
    ("Network Firewall", "DDoS Attack", "mitigates"),
    ("Security Awareness Training", "Phishing", "mitigates"),
    ("Security Awareness Training", "Insider Threat", "mitigates"),
    ("Offline Backups", "Ransomware", "mitigates"),
]

# Demo responses with deliberate errors
DEMO_RESPONSES = {
    "Multi-Factor Authentication": {
        "response": """## Impact Analysis: Disabling Multi-Factor Authentication

**IMMEDIATE RISK INCREASE:**
Disabling MFA significantly increases vulnerability to Phishing attacks, as stolen credentials can now be used directly without a second verification step. This also affects Ransomware risk since attackers often use compromised credentials as an initial access vector.

**CASCADING EFFECTS:**
Without MFA, a successful phishing attack could lead to:
- Unauthorized access to Customer Data and Internal Systems
- Lateral movement across the network
- Potential DDoS amplification through compromised accounts

**COMPENSATING MEASURES:**
- Implement stricter email filtering
- Increase monitoring of authentication logs
- Consider conditional access policies

**RISK RATING: HIGH** - MFA is a critical control.""",
        "errors": ["Hallucination: Mentions Ransomware (no direct relationship)", "Hallucination: Mentions DDoS (no relationship)"]
    },
    "Endpoint Detection & Response": {
        "response": """## Impact Analysis: Disabling Endpoint Detection & Response

**IMMEDIATE RISK INCREASE:**
Without EDR, the organization loses visibility into endpoint-level threats. Ransomware attacks become significantly more dangerous as malicious processes can execute undetected.

**CASCADING EFFECTS:**
- Malware can spread laterally without triggering alerts
- Internal Systems become primary targets
- Customer Data at risk of exfiltration

**COMPENSATING MEASURES:**
- Increase network-level monitoring
- Implement application whitelisting
- More frequent backup verification

**RISK RATING: CRITICAL** - EDR is essential for threat detection.""",
        "errors": ["Omission: Did not mention Insider Threat (EDR also mitigates this)"]
    },
    "Network Firewall": {
        "response": """## Impact Analysis: Disabling Network Firewall

**IMMEDIATE RISK INCREASE:**
Without the firewall, the network perimeter is exposed. DDoS attacks can overwhelm systems more easily. Phishing payloads can communicate with command-and-control servers without restriction. Insider threats become harder to contain.

**CASCADING EFFECTS:**
- External attackers gain easier access to Network Infrastructure
- Ransomware can more easily spread across network segments
- All assets become more exposed

**COMPENSATING MEASURES:**
- Implement host-based firewalls
- Segment critical systems
- Increase IDS/IPS monitoring

**RISK RATING: HIGH** - Firewall is a fundamental control.""",
        "errors": ["Hallucination: Mentions Phishing (firewall doesn't mitigate phishing)", "Hallucination: Mentions Insider Threat (no relationship)"]
    },
    "Security Awareness Training": {
        "response": """## Impact Analysis: Disabling Security Awareness Training

**IMMEDIATE RISK INCREASE:**
Without ongoing training, employees become more susceptible to Phishing attacks. Social engineering success rates typically increase 30-40% without regular awareness programs.

**CASCADING EFFECTS:**
- Credential theft leads to Internal Systems compromise
- Customer Data becomes accessible to attackers
- Increased risk of accidental data exposure

**COMPENSATING MEASURES:**
- Technical controls like email filtering become more critical
- Implement stricter access controls
- Consider phishing simulation tools

**RISK RATING: MEDIUM-HIGH** - Training is a key human-layer defense.""",
        "errors": ["Omission: Did not mention Insider Threat (training also mitigates negligent insider behavior)"]
    },
    "Offline Backups": {
        "response": """## Impact Analysis: Disabling Offline Backups

**IMMEDIATE RISK INCREASE:**
Without offline backups, Ransomware attacks become catastrophic. The organization loses its recovery option, making ransom payment more likely. DDoS attacks could also cause permanent data loss if systems are corrupted.

**CASCADING EFFECTS:**
- Customer Data could be permanently lost in an attack
- Recovery time extends from hours to potentially never
- Business continuity is severely compromised

**COMPENSATING MEASURES:**
- Implement cloud-based backup (though less secure than air-gapped)
- Increase ransomware prevention controls
- Consider cyber insurance

**RISK RATING: CRITICAL** - Backups are the last line of defense.""",
        "errors": ["Hallucination: Mentions DDoS (backups don't mitigate DDoS)"]
    }
}


# =============================================================================
# VISUALIZATION FUNCTIONS
# =============================================================================

def create_ontology_graph(disabled_control=None):
    """Create an interactive network visualization with hierarchical layout"""
    
    pos = {}
    
    controls = list(ONTOLOGY["controls"].keys())
    for i, ctrl in enumerate(controls):
        pos[ctrl] = (0, len(controls) - 1 - i)
    
    threats = list(ONTOLOGY["threats"].keys())
    offset = (len(controls) - len(threats)) / 2
    for i, threat in enumerate(threats):
        pos[threat] = (1.5, len(threats) - 1 - i + offset)
    
    assets = list(ONTOLOGY["assets"].keys())
    offset = (len(controls) - len(assets)) / 2
    for i, asset in enumerate(assets):
        pos[asset] = (3, len(assets) - 1 - i + offset)
    
    node_types = {}
    for asset in assets:
        node_types[asset] = "asset"
    for threat in threats:
        node_types[threat] = "threat"
    for control in controls:
        node_types[control] = "disabled" if control == disabled_control else "control"
    
    edge_traces = []
    
    for source, target, rel_type in RELATIONSHIPS:
        x0, y0 = pos[source]
        x1, y1 = pos[target]
        
        is_disabled_edge = (source == disabled_control or target == disabled_control)
        
        if is_disabled_edge:
            color = "#cccccc"
            dash = "dash"
        elif rel_type == "targets":
            color = "#e74c3c"
            dash = "solid"
        else:
            color = "#27ae60"
            dash = "solid"
        
        edge_traces.append(go.Scatter(
            x=[x0, x1, None],
            y=[y0, y1, None],
            mode='lines',
            line=dict(width=2, color=color, dash=dash),
            hoverinfo='none',
            showlegend=False
        ))
    
    node_colors = {
        "asset": "#3498db",
        "threat": "#e74c3c",
        "control": "#27ae60",
        "disabled": "#95a5a6"
    }
    
    fig = go.Figure()
    
    for trace in edge_traces:
        fig.add_trace(trace)
    
    for node_type, color in node_colors.items():
        nodes_of_type = [n for n, t in node_types.items() if t == node_type]
        if not nodes_of_type:
            continue
            
        x_vals = [pos[n][0] for n in nodes_of_type]
        y_vals = [pos[n][1] for n in nodes_of_type]
        
        text_positions = []
        for n in nodes_of_type:
            if pos[n][0] == 0:
                text_positions.append("middle left")
            elif pos[n][0] == 3:
                text_positions.append("middle right")
            else:
                text_positions.append("top center")
        
        fig.add_trace(go.Scatter(
            x=x_vals,
            y=y_vals,
            mode='markers+text',
            marker=dict(
                size=35 if node_type == "disabled" else 28,
                color=color,
                line=dict(width=2, color='white')
            ),
            text=nodes_of_type,
            textposition=text_positions,
            textfont=dict(size=11),
            hoverinfo='text',
            hovertext=[f"{n}<br>{node_type.upper()}" for n in nodes_of_type],
            showlegend=False
        ))
    
    fig.add_annotation(x=0, y=len(controls) + 0.5, text="CONTROLS", 
                       showarrow=False, font=dict(size=14, color="#27ae60", family="Arial Black"))
    fig.add_annotation(x=1.5, y=len(controls) + 0.5, text="THREATS", 
                       showarrow=False, font=dict(size=14, color="#e74c3c", family="Arial Black"))
    fig.add_annotation(x=3, y=len(controls) + 0.5, text="ASSETS", 
                       showarrow=False, font=dict(size=14, color="#3498db", family="Arial Black"))
    
    fig.update_layout(
        title="",
        showlegend=False,
        hovermode='closest',
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-1.5, 4.5]),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-1, len(controls) + 1.5]),
        height=500,
        margin=dict(l=20, r=20, t=20, b=20),
        plot_bgcolor='rgba(0,0,0,0)'
    )
    
    return fig


def get_risk_summary(disabled_control=None):
    """Calculate which threats are unmitigated"""
    threat_coverage = {}
    
    for threat in ONTOLOGY["threats"]:
        mitigating_controls = []
        for control, details in ONTOLOGY["controls"].items():
            if threat in details["mitigates"] and control != disabled_control:
                mitigating_controls.append(control)
        
        threat_coverage[threat] = {
            "controls": mitigating_controls,
            "mitigated": len(mitigating_controls) > 0,
            "coverage_count": len(mitigating_controls)
        }
    
    return threat_coverage


def get_expected_impacts(disabled_control):
    """Extract what the ontology EXPECTS when a control is disabled"""
    ctrl_details = ONTOLOGY["controls"][disabled_control]
    threats_affected = ctrl_details["mitigates"]
    
    assets_at_risk = set()
    for threat in threats_affected:
        for asset in ONTOLOGY["threats"][threat]["targets"]:
            assets_at_risk.add(asset)
    
    remaining_coverage = {}
    for threat in threats_affected:
        other_controls = []
        for ctrl, details in ONTOLOGY["controls"].items():
            if ctrl != disabled_control and threat in details["mitigates"]:
                other_controls.append(ctrl)
        remaining_coverage[threat] = other_controls
    
    unrelated_threats = [t for t in ONTOLOGY["threats"] if t not in threats_affected]
    
    return {
        "threats_should_mention": threats_affected,
        "assets_should_mention": list(assets_at_risk),
        "remaining_controls": remaining_coverage,
        "threats_should_not_mention": unrelated_threats,
        "control_effectiveness": ctrl_details["effectiveness"]
    }


def validate_llm_response(response_text, expected_impacts):
    """Check LLM response against ontology expectations"""
    response_lower = response_text.lower()
    
    results = {
        "threats_mentioned": [],
        "threats_missed": [],
        "threats_hallucinated": [],
        "assets_mentioned": [],
        "assets_missed": [],
        "validation_score": 0,
        "issues": []
    }
    
    for threat in expected_impacts["threats_should_mention"]:
        if threat.lower() in response_lower:
            results["threats_mentioned"].append(threat)
        else:
            results["threats_missed"].append(threat)
            results["issues"].append(f"OMISSION: Should have mentioned '{threat}' but didn't")
    
    for threat in expected_impacts["threats_should_not_mention"]:
        threat_lower = threat.lower()
        if threat_lower in response_lower:
            risk_phrases = ["increase", "exposed", "vulnerable", "risk", "affected", "impact"]
            pos = response_lower.find(threat_lower)
            context = response_lower[max(0, pos-50):pos+len(threat_lower)+50]
            if any(phrase in context for phrase in risk_phrases):
                results["threats_hallucinated"].append(threat)
                results["issues"].append(f"HALLUCINATION: Mentioned '{threat}' as affected, but ontology shows no relationship")
    
    for asset in expected_impacts["assets_should_mention"]:
        if asset.lower() in response_lower:
            results["assets_mentioned"].append(asset)
        else:
            results["assets_missed"].append(asset)
            results["issues"].append(f"OMISSION: Should have mentioned '{asset}' at risk but didn't")
    
    total_expected = len(expected_impacts["threats_should_mention"]) + len(expected_impacts["assets_should_mention"])
    total_correct = len(results["threats_mentioned"]) + len(results["assets_mentioned"])
    total_errors = len(results["threats_hallucinated"])
    
    if total_expected > 0:
        results["validation_score"] = max(0, (total_correct - total_errors) / total_expected * 100)
    
    return results


def run_counterfactual_analysis(client, disabled_control):
    """Use OpenAI to reason about impact of disabling a control"""
    control_info = ONTOLOGY["controls"][disabled_control]
    threats_affected = control_info["mitigates"]
    
    assets_at_risk = set()
    for threat in threats_affected:
        for asset in ONTOLOGY["threats"][threat]["targets"]:
            assets_at_risk.add(asset)
    
    remaining_coverage = {}
    for threat in threats_affected:
        other_controls = []
        for ctrl, details in ONTOLOGY["controls"].items():
            if ctrl != disabled_control and threat in details["mitigates"]:
                other_controls.append(ctrl)
        remaining_coverage[threat] = other_controls
    
    system_prompt = """You are a cybersecurity risk analyst. Given information about a control being disabled, 
analyze the cascading impacts on the organization's security posture. Be specific and actionable.
Structure your response with clear sections but keep it concise (under 300 words)."""

    user_prompt = f"""A security control has been disabled. Analyze the impact.

DISABLED CONTROL: {disabled_control}
- Description: {control_info['description']}
- Effectiveness: {control_info['effectiveness']}
- Threats it mitigates: {', '.join(threats_affected)}

THREATS NOW LESS PROTECTED:
{json.dumps({t: {'remaining_controls': remaining_coverage[t], 'target_assets': ONTOLOGY['threats'][t]['targets']} for t in threats_affected}, indent=2)}

ASSETS POTENTIALLY AT RISK: {', '.join(assets_at_risk)}

Provide:
1. IMMEDIATE RISK INCREASE - What specific attack scenarios become more likely?
2. CASCADING EFFECTS - How could a successful attack spread through the organization?
3. COMPENSATING MEASURES - What should be done immediately to reduce exposure?
4. RISK RATING CHANGE - Qualitative assessment (Low→Medium→High→Critical)"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7,
        max_tokens=500
    )
    
    return response.choices[0].message.content


def run_challenge_analysis(client, disabled_control):
    """Prompt designed to encourage hallucinations"""
    control_info = ONTOLOGY["controls"][disabled_control]
    
    system_prompt = """You are a cybersecurity risk analyst. Analyze the impact of disabling a security control.
Be comprehensive and consider ALL possible ways this could affect the organization's security.
Think broadly about interconnected risks - security is a holistic system where everything connects."""

    user_prompt = f"""Analyze what happens when we disable: {disabled_control}

This control is described as: {control_info['description']}

Consider:
- How might this affect ALL types of cyber threats (ransomware, phishing, insider threats, DDoS)?
- What assets could be impacted directly or indirectly?
- Are there any hidden dependencies or unexpected consequences?
- How might attackers exploit this gap in creative ways?

Be thorough and consider second and third-order effects. Don't limit yourself to obvious impacts."""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.9,
        max_tokens=600
    )
    
    return response.choices[0].message.content


# =============================================================================
# PAGE CONTENT
# =============================================================================

st.title("🧠 Ontology & Counterfactual Reasoning")
st.markdown("*Exploring structured knowledge and 'what if' analysis for risk assessment*")

# Get API key from session state (set in Home.py)
api_key = st.session_state.get('openai_api_key', '')

# Sidebar
with st.sidebar:
    st.header("ℹ️ Legend")
    st.markdown("""
    **Node Colors:**
    - 🔵 Blue = Assets
    - 🔴 Red = Threats  
    - 🟢 Green = Controls
    - ⚫ Gray = Disabled
    
    **Line Colors:**
    - Red = Threat targets Asset
    - Green = Control mitigates Threat
    """)
    
    if not api_key:
        st.warning("⚠️ Enter API key on Home page for AI features")

# Main tabs
tab1, tab2, tab3, tab4 = st.tabs(["📊 Ontology Explorer", "🔮 Counterfactual Analysis", "✅ LLM Validation", "📚 Concepts"])

# TAB 1: ONTOLOGY EXPLORER
with tab1:
    st.header("Cybersecurity Risk Ontology")
    st.markdown("An ontology defines **concepts** and their **relationships**.")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        fig = create_ontology_graph()
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Explore Components")
        
        component_type = st.selectbox("Select type:", ["Assets", "Threats", "Controls"])
        
        if component_type == "Assets":
            for name, details in ONTOLOGY["assets"].items():
                with st.expander(f"🔵 {name}"):
                    st.write(f"**Description:** {details['description']}")
                    st.write(f"**Criticality:** {details['criticality']}")
        elif component_type == "Threats":
            for name, details in ONTOLOGY["threats"].items():
                with st.expander(f"🔴 {name}"):
                    st.write(f"**Description:** {details['description']}")
                    st.write(f"**Targets:** {', '.join(details['targets'])}")
        else:
            for name, details in ONTOLOGY["controls"].items():
                with st.expander(f"🟢 {name}"):
                    st.write(f"**Description:** {details['description']}")
                    st.write(f"**Mitigates:** {', '.join(details['mitigates'])}")
    
    st.subheader("Threat-Control Coverage Matrix")
    import pandas as pd
    
    threats = list(ONTOLOGY["threats"].keys())
    controls = list(ONTOLOGY["controls"].keys())
    
    matrix_data = []
    for threat in threats:
        row = []
        for control in controls:
            if threat in ONTOLOGY["controls"][control]["mitigates"]:
                row.append("✓")
            else:
                row.append("")
        matrix_data.append(row)
    
    matrix_df = pd.DataFrame(matrix_data, index=threats, columns=controls)
    st.dataframe(matrix_df, use_container_width=True)

# TAB 2: COUNTERFACTUAL ANALYSIS
with tab2:
    st.header("Counterfactual Analysis")
    st.markdown("**'What if'** we disabled a security control?")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("1️⃣ Select Scenario")
        
        disabled_control = st.selectbox(
            "Which control should we disable?",
            options=list(ONTOLOGY["controls"].keys()),
            key="cf_control"
        )
        
        ctrl_details = ONTOLOGY["controls"][disabled_control]
        st.info(f"**{disabled_control}**\n\n{ctrl_details['description']}\n\n*Mitigates: {', '.join(ctrl_details['mitigates'])}*")
        
        st.subheader("2️⃣ Impact on Threat Coverage")
        
        baseline = get_risk_summary()
        counterfactual = get_risk_summary(disabled_control)
        
        for threat in ONTOLOGY["threats"]:
            baseline_count = baseline[threat]["coverage_count"]
            cf_count = counterfactual[threat]["coverage_count"]
            
            if cf_count < baseline_count:
                st.metric(threat, f"{cf_count} controls", f"{cf_count - baseline_count}", delta_color="inverse")
            else:
                st.metric(threat, f"{cf_count} controls", "No change")
    
    with col2:
        st.subheader("3️⃣ Visual Impact")
        fig = create_ontology_graph(disabled_control)
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    if st.button("🔮 Run AI Analysis", type="primary", use_container_width=True):
        if not api_key:
            st.error("Please enter your OpenAI API key on the Home page.")
        else:
            try:
                client = OpenAI(api_key=api_key)
                with st.spinner("Analyzing..."):
                    analysis = run_counterfactual_analysis(client, disabled_control)
                st.subheader("📋 AI Impact Analysis")
                st.markdown(analysis)
            except Exception as e:
                st.error(f"Error: {str(e)}")

# TAB 3: LLM VALIDATION
with tab3:
    st.header("LLM Output Validation")
    st.markdown("**Use the ontology as ground truth to verify AI reasoning.**")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("1️⃣ Setup Test")
        
        validation_control = st.selectbox(
            "Select control to test:",
            options=list(ONTOLOGY["controls"].keys()),
            key="val_control"
        )
        
        test_mode = st.radio(
            "Test Mode:",
            options=["Standard", "Challenge", "Demo (Pre-built Errors)"],
            horizontal=True
        )
        
        if test_mode == "Challenge":
            st.warning("⚡ **Challenge Mode:** Encourages hallucinations")
        elif test_mode == "Demo (Pre-built Errors)":
            st.info("🎭 **Demo Mode:** Pre-written responses with known errors")
        
        expected = get_expected_impacts(validation_control)
        
        st.subheader("2️⃣ Ontology Expectations")
        
        st.markdown("**Should mention these threats:**")
        for threat in expected["threats_should_mention"]:
            remaining = expected["remaining_controls"].get(threat, [])
            if remaining:
                st.write(f"- ✓ {threat}")
            else:
                st.write(f"- ⚠️ {threat} *(no backup!)*")
        
        st.markdown("**Should mention these assets:**")
        for asset in expected["assets_should_mention"]:
            st.write(f"- ✓ {asset}")
        
        st.markdown("**Should NOT mention:**")
        for threat in expected["threats_should_not_mention"]:
            st.write(f"- ✗ {threat}")
    
    with col2:
        st.subheader("3️⃣ Run Test")
        
        if test_mode == "Demo (Pre-built Errors)":
            demo_data = DEMO_RESPONSES.get(validation_control, {})
            if demo_data:
                st.markdown("**Known errors:**")
                for err in demo_data.get("errors", []):
                    st.caption(f"• {err}")
        
        button_label = "🎭 Run Demo" if test_mode == "Demo (Pre-built Errors)" else "🧪 Test LLM"
        
        if st.button(button_label, type="primary", use_container_width=True):
            if test_mode == "Demo (Pre-built Errors)":
                demo_data = DEMO_RESPONSES.get(validation_control, {})
                if demo_data:
                    st.session_state['val_response'] = demo_data["response"]
                    st.session_state['val_results'] = validate_llm_response(demo_data["response"], expected)
                    st.session_state['val_expected'] = expected
            elif not api_key:
                st.error("Enter API key on Home page.")
            else:
                try:
                    client = OpenAI(api_key=api_key)
                    with st.spinner("Running..."):
                        if test_mode == "Challenge":
                            response = run_challenge_analysis(client, validation_control)
                        else:
                            response = run_counterfactual_analysis(client, validation_control)
                    st.session_state['val_response'] = response
                    st.session_state['val_results'] = validate_llm_response(response, expected)
                    st.session_state['val_expected'] = expected
                except Exception as e:
                    st.error(f"Error: {str(e)}")
        
        if 'val_response' in st.session_state:
            with st.expander("View LLM Response"):
                st.markdown(st.session_state['val_response'])
    
    if 'val_results' in st.session_state:
        st.markdown("---")
        st.subheader("4️⃣ Validation Results")
        
        results = st.session_state['val_results']
        exp = st.session_state['val_expected']
        
        score = results["validation_score"]
        
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Score", f"{score:.0f}%")
        c2.metric("Threats OK", f"{len(results['threats_mentioned'])}/{len(exp['threats_should_mention'])}")
        c3.metric("Assets OK", f"{len(results['assets_mentioned'])}/{len(exp['assets_should_mention'])}")
        c4.metric("Hallucinations", len(results['threats_hallucinated']))
        
        c1, c2, c3 = st.columns(3)
        
        with c1:
            st.markdown("**✅ Correct**")
            for t in results["threats_mentioned"]:
                st.success(t)
            for a in results["assets_mentioned"]:
                st.success(a)
        
        with c2:
            st.markdown("**⚠️ Missed**")
            for t in results["threats_missed"]:
                st.warning(t)
            for a in results["assets_missed"]:
                st.warning(a)
        
        with c3:
            st.markdown("**❌ Hallucinated**")
            if results["threats_hallucinated"]:
                for t in results["threats_hallucinated"]:
                    st.error(t)
            else:
                st.write("None detected")

# TAB 4: CONCEPTS
with tab4:
    st.header("Understanding the Concepts")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🗂️ What is an Ontology?")
        st.markdown("""
        An **ontology** defines:
        
        **Concepts** — Assets, Threats, Controls
        
        **Relationships** — "MFA mitigates Phishing"
        
        **Properties** — Criticality, Effectiveness
        
        ---
        
        **Why use with AI?**
        - Structured context beats messy text
        - Consistent terminology
        - Enables logical reasoning
        - Auditable conclusions
        """)
    
    with col2:
        st.subheader("🔮 What are Counterfactuals?")
        st.markdown("""
        Ask: *"What if things were different?"*
        
        **Process:**
        1. Baseline — current state
        2. Change — disable a control
        3. Trace — effects through system
        4. Compare — what changed?
        
        ---
        
        **Why it matters:**
        - Prioritize controls
        - Justify investments
        - Plan for failures
        - Test scenarios safely
        """)
    
    st.markdown("---")
    st.markdown("""
    **Combined:** The ontology provides *structure*, the counterfactual provides *scenarios*, 
    and the AI provides *reasoning*. Together they enable sophisticated risk analysis.
    """)
