import streamlit as st
import streamlit.components.v1 as components
import plotly.graph_objects as go

from assessment import SKILL_LABELS, get_adaptive_questions, get_difficulty, calculate_skill_scores
from recommendation import recommend_careers, get_career_match_details
from skill_gap import analyze_skill_gap
from roadmap import generate_roadmap

st.set_page_config(
    page_title="CareerGuide AI",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

if "assessment_complete" not in st.session_state:
    st.session_state["assessment_complete"] = False
if "scroll_to_results" not in st.session_state:
    st.session_state["scroll_to_results"] = False
if "assessment_stage" not in st.session_state:
    st.session_state["assessment_stage"] = 1
if "self_ratings" not in st.session_state:
    st.session_state["self_ratings"] = {}
if "student_info" not in st.session_state:
    st.session_state["student_info"] = {}

st.markdown("""
<style>
:root{--bg:#070912;--text:#f7f8ff;--muted:#9aa5bd;--purple:#a78bfa;--cyan:#22d3ee;--pink:#f472b6;--green:#34d399;--amber:#fbbf24}
html{scroll-behavior:smooth!important}
.stApp{background:radial-gradient(circle at 8% 2%,rgba(139,92,246,.23),transparent 24%),radial-gradient(circle at 92% 6%,rgba(34,211,238,.15),transparent 21%),radial-gradient(circle at 52% 52%,rgba(244,114,182,.06),transparent 26%),linear-gradient(180deg,#070912,#090b16 55%,#06070d);color:var(--text)}
.stApp:before{content:"";position:fixed;inset:0;pointer-events:none;opacity:.25;background-image:linear-gradient(rgba(255,255,255,.018) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.018) 1px,transparent 1px);background-size:42px 42px;mask-image:linear-gradient(to bottom,black,transparent 80%)}
.block-container{max-width:1380px;padding:28px 34px 70px}
#MainMenu,footer{visibility:hidden}[data-testid="stHeader"]{background:transparent}section[data-testid="stSidebar"]{display:none}
h1,h2,h3{color:var(--text)!important}h1{font-size:clamp(48px,6vw,84px)!important;line-height:.94!important;letter-spacing:-4px!important;font-weight:900!important;background:linear-gradient(115deg,#fff 10%,#d7ccff 42%,#8be9ff 72%,#ff9ed0);-webkit-background-clip:text;-webkit-text-fill-color:transparent}h2{font-size:34px!important;letter-spacing:-1.4px!important;font-weight:850!important}
.section-kicker{color:#8e9ab5;font-size:11px;letter-spacing:.17em;font-weight:850;text-transform:uppercase;margin-bottom:7px}
.hero-card{position:relative;overflow:hidden;padding:38px;border:1px solid rgba(255,255,255,.09);border-radius:28px;background:radial-gradient(circle at 80% 10%,rgba(34,211,238,.16),transparent 23%),radial-gradient(circle at 12% 0%,rgba(167,139,250,.18),transparent 25%),linear-gradient(135deg,rgba(18,22,39,.94),rgba(9,12,22,.92));box-shadow:0 30px 100px rgba(0,0,0,.36)}
.eyebrow{display:inline-flex;padding:7px 11px;border-radius:999px;background:rgba(167,139,250,.11);border:1px solid rgba(167,139,250,.22);color:#ddd5ff;font-size:11px;letter-spacing:.13em;font-weight:800}.mini-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:24px}.mini-card{padding:15px 16px;border-radius:18px;background:rgba(255,255,255,.035);border:1px solid rgba(255,255,255,.065)}.mini-kicker{font-size:10px;color:#77839b;letter-spacing:.13em;font-weight:800}.mini-value{margin-top:7px;font-size:16px;font-weight:800;color:#eef1ff}
.glass-panel{background:linear-gradient(135deg,rgba(18,22,39,.78),rgba(11,14,25,.80));border:1px solid rgba(255,255,255,.08);border-radius:22px;padding:20px;box-shadow:0 20px 70px rgba(0,0,0,.18)}
div[data-testid="stForm"]{background:linear-gradient(135deg,rgba(18,22,39,.78),rgba(11,14,25,.80))!important;border:1px solid rgba(255,255,255,.08)!important;border-radius:22px!important;padding:20px!important}
div[data-baseweb="input"]>div,div[data-baseweb="select"]>div{background:rgba(19,23,40,.82)!important;border:1px solid rgba(255,255,255,.09)!important;border-radius:13px!important}
button[kind="primary"]{min-height:54px!important;border:1px solid rgba(255,255,255,.10)!important;border-radius:15px!important;background:linear-gradient(110deg,#8b5cf6,#a78bfa 34%,#22d3ee)!important;color:#090b12!important;font-weight:900!important;box-shadow:0 16px 45px rgba(139,92,246,.24)!important}button[kind="primary"]:hover{transform:translateY(-2px)!important}
[data-testid="stMetric"]{background:linear-gradient(135deg,rgba(255,255,255,.038),rgba(255,255,255,.015))!important;border:1px solid rgba(255,255,255,.065)!important;border-radius:17px!important;padding:14px 16px!important}[data-testid="stMetricValue"]{color:#f7f8ff!important;font-weight:900!important}[data-testid="stMetricLabel"]{color:#8995af!important}
[data-testid="stProgressBar"]{background:rgba(255,255,255,.06)!important;border-radius:999px!important;overflow:hidden!important}[data-testid="stProgressBar"]>div>div{background:linear-gradient(90deg,#8b5cf6,#22d3ee,#f472b6)!important;border-radius:999px!important}
button[data-baseweb="tab"]{font-weight:850!important;color:#79849e!important}button[data-baseweb="tab"][aria-selected="true"]{color:#ddd7ff!important}
.score-hero{padding:30px;border-radius:24px;border:1px solid rgba(255,255,255,.08);background:radial-gradient(circle at 85% 20%,rgba(34,211,238,.12),transparent 24%),linear-gradient(135deg,rgba(30,25,57,.88),rgba(13,17,30,.92))}.score-big{font-size:76px;font-weight:900;letter-spacing:-4px;background:linear-gradient(120deg,#fff,#c7bbff,#7de9ff);-webkit-background-clip:text;-webkit-text-fill-color:transparent;line-height:1;margin:8px 0}.career-card{padding:19px;border-radius:18px;border:1px solid rgba(255,255,255,.07);background:rgba(255,255,255,.028);min-height:116px}.career-rank{color:#818da7;font-size:11px;font-weight:850;letter-spacing:.12em}.career-name{font-size:19px;font-weight:850;color:#f4f6ff;margin-top:5px}.career-score{font-size:13px;font-weight:850;color:#b7aaff}.roadmap-box{padding:15px;border-radius:15px;background:rgba(255,255,255,.026);border:1px solid rgba(255,255,255,.06);min-height:112px}.roadmap-kicker{font-size:10px;color:#76829b;letter-spacing:.13em;font-weight:850}.roadmap-text{color:#c0c7d9;font-size:13px;line-height:1.55;margin-top:6px}.chip{display:inline-flex;padding:6px 10px;border-radius:999px;font-size:10px;font-weight:850;letter-spacing:.08em;text-transform:uppercase;background:rgba(255,255,255,.045);border:1px solid rgba(255,255,255,.07)}.priority-high{color:#ff91b8}.priority-medium{color:#ffd37b}.priority-low{color:#84e7c4}.priority-complete{color:#8eeaff}.muted-small{color:#7e8aa6;font-size:12px}.results-anchor{scroll-margin-top:35px;height:1px}.resource-panel{margin-top:12px;padding:14px 16px;border-radius:16px;background:linear-gradient(135deg,rgba(167,139,250,.055),rgba(34,211,238,.035));border:1px solid rgba(255,255,255,.065)}.resource-link{display:flex;align-items:center;justify-content:space-between;gap:12px;text-decoration:none!important;padding:11px 13px;border-radius:12px;background:rgba(255,255,255,.028);border:1px solid rgba(255,255,255,.06);color:#eef1ff!important;font-size:13px;font-weight:800;transition:.2s ease}.resource-link:hover{transform:translateY(-2px);background:rgba(255,255,255,.06);border-color:rgba(167,139,250,.26)}.resource-sub{font-size:10px;color:#7f8ba5;font-weight:700;letter-spacing:.08em;text-transform:uppercase}.resource-arrow{color:#8be9ff;font-size:16px}
@media(max-width:900px){.block-container{padding:20px 16px 55px}.hero-card{padding:24px}.mini-grid{grid-template-columns:1fr}}
</style>
""", unsafe_allow_html=True)


def priority_class(priority):
    return {"High":"priority-high","Medium":"priority-medium","Low":"priority-low","Complete":"priority-complete"}.get(priority, "")


st.markdown("""
<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:24px;">
<div style="font-size:13px;font-weight:850;letter-spacing:.13em;color:#ddd8ff;">
<span style="display:inline-block;width:9px;height:9px;border-radius:50%;margin-right:9px;background:linear-gradient(135deg,#a78bfa,#22d3ee,#f472b6);box-shadow:0 0 22px rgba(167,139,250,.7);"></span>CAREERGUIDE AI</div>
<div style="color:#626d85;font-size:10px;letter-spacing:.1em;">STUDENT CAREER INTELLIGENCE</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero-card">
<div class="eyebrow">✦ PERSONALIZED CAREER DISCOVERY</div>
<div style="margin-top:18px;font-size:clamp(48px,6vw,82px);font-weight:900;line-height:.94;letter-spacing:-4px;background:linear-gradient(115deg,#fff 10%,#d7ccff 44%,#8be9ff 72%,#ff9ed0);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">Know your skills.<br>Map your future.</div>
<div style="max-width:780px;font-size:17px;line-height:1.7;color:#adb6cd;margin-top:18px;">A student-focused career guidance system that combines self-assessment with objective knowledge checks, then turns the resulting skill profile into explainable career matches, skill gaps and a practical learning roadmap.</div>
<div class="mini-grid">
<div class="mini-card"><div class="mini-kicker">01 / PROFILE</div><div class="mini-value">Student context</div></div>
<div class="mini-card"><div class="mini-kicker">02 / ASSESS</div><div class="mini-value">Self + objective evidence</div></div>
<div class="mini-card"><div class="mini-kicker">03 / GUIDE</div><div class="mini-value">Career → gaps → roadmap</div></div>
</div></div>
""", unsafe_allow_html=True)

st.write("")
st.markdown("<div class='section-kicker'>THE EXPERIENCE</div><div style='font-size:15px;color:#9aa4bd;'>01 Profile &nbsp;→&nbsp; 02 Assess &nbsp;→&nbsp; 03 Discover &nbsp;→&nbsp; 04 Identify Gaps &nbsp;→&nbsp; 05 Build Roadmap</div>", unsafe_allow_html=True)
st.divider()

st.markdown("<div class='section-kicker'>01 / STUDENT PROFILE</div>", unsafe_allow_html=True)

# ---------------------------------------------------------------
# STAGE 1: PROFILE + SELF-ASSESSMENT
# The objective questions are intentionally hidden until the
# student submits these confidence ratings.
# ---------------------------------------------------------------
if not st.session_state.get("assessment_complete", False) and st.session_state.get("assessment_stage", 1) == 1:
    st.header("Start with where you are.")

    with st.form("student_profile_form"):
        col1, col2, col3 = st.columns(3, gap="large")
        with col1:
            name = st.text_input("Full Name", value=st.session_state["student_info"].get("name", ""), placeholder="e.g. Shafiq Khan")
        with col2:
            branch_options = ["CSE", "ISE", "ECE", "EEE", "Other"]
            saved_branch = st.session_state["student_info"].get("branch", "CSE")
            branch = st.selectbox("Branch", branch_options, index=branch_options.index(saved_branch) if saved_branch in branch_options else 0)
        with col3:
            semester_options = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th"]
            saved_semester = st.session_state["student_info"].get("semester", "7th")
            semester = st.selectbox("Semester", semester_options, index=semester_options.index(saved_semester) if saved_semester in semester_options else 6)

        st.write("")
        st.markdown("<div class='section-kicker'>02 / SELF-ASSESSMENT</div>", unsafe_allow_html=True)
        st.header("How confident are you in each skill?")
        st.caption("Choose 1–5. Your rating determines the difficulty of the objective questions you receive next.")

        self_ratings = {}
        skill_items = list(SKILL_LABELS.items())
        for start_idx in range(0, len(skill_items), 3):
            cols = st.columns(3, gap="large")
            for col, (skill, label) in zip(cols, skill_items[start_idx:start_idx+3]):
                with col:
                    previous = int(st.session_state["self_ratings"].get(skill, 3))
                    self_ratings[skill] = st.select_slider(
                        label,
                        options=[1, 2, 3, 4, 5],
                        value=previous,
                        key=f"self_{skill.replace(' ','_')}"
                    )

        st.write("")
        st.markdown(
            "<div style='padding:15px 17px;border-radius:16px;background:rgba(167,139,250,.07);border:1px solid rgba(167,139,250,.16);color:#b7bfd3;font-size:13px;'>"
            "<b style='color:#f2f4ff;'>Adaptive assessment:</b> low confidence gives beginner questions, a mid-level rating gives intermediate questions, a rating of 4 gives advanced questions, and a rating of 5 gives expert-level questions."
            "</div>",
            unsafe_allow_html=True
        )
        st.write("")

        _, button_col, _ = st.columns([1.25, 1, 1.25])
        with button_col:
            continue_to_quiz = st.form_submit_button(
                "Continue to Knowledge Check →",
                type="primary",
                use_container_width=True
            )

    if continue_to_quiz:
        if not name.strip():
            st.warning("Please enter your name before continuing.")
        else:
            st.session_state["student_info"] = {
                "name": name.strip(),
                "branch": branch,
                "semester": semester,
            }
            st.session_state["self_ratings"] = self_ratings
            st.session_state["assessment_stage"] = 2
            st.rerun()


# ---------------------------------------------------------------
# STAGE 2: ADAPTIVE OBJECTIVE ASSESSMENT
# Questions are generated/selected only after stage 1 is submitted.
# ---------------------------------------------------------------
if not st.session_state.get("assessment_complete", False) and st.session_state.get("assessment_stage", 1) == 2:
    st.divider()
    st.markdown("<div class='section-kicker'>03 / ADAPTIVE OBJECTIVE KNOWLEDGE CHECK</div>", unsafe_allow_html=True)
    st.header("Your questions are ready.")
    st.caption("The system created a 5-question set for every skill using the confidence ratings you submitted.")

    difficulty_summary = []
    for skill in SKILL_LABELS:
        rating = int(st.session_state["self_ratings"].get(skill, 3))
        difficulty = get_difficulty(rating)
        difficulty_summary.append((skill, rating, difficulty))

    st.markdown(
        "<div style='display:flex;gap:10px;flex-wrap:wrap;margin:8px 0 18px;'>"
        "<span class='chip'>1–2 • BEGINNER</span>"
        "<span class='chip'>3 • INTERMEDIATE</span>"
        "<span class='chip'>4 • ADVANCED</span>"
        "<span class='chip'>5 • EXPERT</span>"
        "<span class='chip'>5 QUESTIONS / SKILL</span>"
        "</div>",
        unsafe_allow_html=True
    )

    summary_cols = st.columns(3, gap="medium")
    for idx, (skill, rating, difficulty) in enumerate(difficulty_summary):
        with summary_cols[idx % 3]:
            st.markdown(
                f"<div class='mini-card' style='margin-bottom:10px;'>"
                f"<div class='mini-kicker'>{SKILL_LABELS[skill].upper()}</div>"
                f"<div class='mini-value'>Confidence {rating}/5 • {difficulty.title()}</div>"
                f"</div>",
                unsafe_allow_html=True
            )

    if st.button("← Change confidence ratings", key="change_confidence"):
        st.session_state["assessment_stage"] = 1
        st.session_state["assessment_complete"] = False
        st.rerun()

    adaptive_questions = get_adaptive_questions(st.session_state["self_ratings"], questions_per_skill=5)
    quiz_answers = {skill: [] for skill in SKILL_LABELS}
    question_number_by_skill = {skill: 0 for skill in SKILL_LABELS}

    with st.form("adaptive_knowledge_form"):
        for q_start in range(0, len(adaptive_questions), 2):
            cols = st.columns(2, gap="large")
            for col, question in zip(cols, adaptive_questions[q_start:q_start+2]):
                skill = question["skill"]
                question_number_by_skill[skill] += 1
                q_num = question_number_by_skill[skill]
                difficulty_label = question["difficulty"].upper()
                with col:
                    st.markdown(
                        f"<div style='padding:14px 16px 8px;border-radius:16px 16px 0 0;background:rgba(255,255,255,.026);border:1px solid rgba(255,255,255,.055);border-bottom:none;'>"
                        f"<div style='display:flex;justify-content:space-between;gap:10px;align-items:center;'>"
                        f"<div style='color:#7f8ba5;font-size:10px;font-weight:850;letter-spacing:.13em;'>{SKILL_LABELS[skill].upper()} • Q{q_num}/5</div>"
                        f"<div class='chip'>{difficulty_label}</div></div>"
                        f"<div style='color:#f1f3fb;font-size:15px;font-weight:800;margin-top:8px;'>{question['question']}</div></div>",
                        unsafe_allow_html=True
                    )
                    answer = st.radio(
                        "Answer",
                        question["options"],
                        key=f"quiz_{skill.replace(' ','_')}_{q_num}",
                        index=None,
                        label_visibility="collapsed"
                    )
                    quiz_answers[skill].append((answer, question))

        st.write("")
        _, button_col, _ = st.columns([1.25, 1, 1.25])
        with button_col:
            generate_insights = st.form_submit_button(
                "✦ Generate Career Insights",
                type="primary",
                use_container_width=True
            )

    if generate_insights:
        if any(len(items) != 5 or any(answer is None for answer, _ in items) for items in quiz_answers.values()):
            st.warning("Please answer all 5 objective questions for every skill before generating results.")
        else:
            student = st.session_state["student_info"]
            skill_results = calculate_skill_scores(st.session_state["self_ratings"], quiz_answers)
            skill_scores = {skill: result["score"] for skill, result in skill_results.items()}
            demonstrated_skills = [skill for skill, score in skill_scores.items() if score >= 60]
            user_profile = {
                "name": student["name"],
                "branch": student["branch"],
                "semester": student["semester"],
                "skills": demonstrated_skills,
                "skill_scores": skill_scores,
                "skill_results": skill_results,
            }
            careers = recommend_careers(user_profile, top_n=3)
            st.session_state["user_profile"] = user_profile
            st.session_state["careers"] = careers
            st.session_state["assessment_complete"] = True
            st.session_state["scroll_to_results"] = True
            st.rerun()


if st.session_state.get("assessment_complete", False) and st.session_state.get("careers"):
    user_profile = st.session_state["user_profile"]
    careers = st.session_state["careers"]

    st.markdown('<div id="career-results" class="results-anchor"></div>', unsafe_allow_html=True)
    st.divider()
    st.markdown("<div class='section-kicker'>04 / YOUR CAREER INTELLIGENCE</div>", unsafe_allow_html=True)
    st.header("Here is what your assessment points toward.")

    demonstrated = sum(1 for score in user_profile["skill_scores"].values() if score >= 60)
    all_scores = list(user_profile["skill_scores"].values())
    average_score = round(sum(all_scores) / len(all_scores)) if all_scores else 0
    st.caption(f"{user_profile['branch']} • {user_profile['semester']} Semester • {demonstrated} demonstrated skills • {average_score}% average skill score")

    top_career = careers[0]
    top_details = get_career_match_details(user_profile, top_career)

    left, right = st.columns([1.35, .65], gap="large")
    with left:
        st.markdown(f"<div class='score-hero'><div class='section-kicker'>STRONGEST CAREER ALIGNMENT</div><div style='font-size:17px;color:#96a0b8;margin-top:4px;'>{top_career}</div><div class='score-big'>{top_details['match_score']}%</div><div style='font-size:16px;font-weight:800;color:#eef1ff;'>Readiness match</div><div style='font-size:13px;line-height:1.6;color:#9ba6bd;margin-top:8px;'>{top_details['description']}</div></div>", unsafe_allow_html=True)

    with right:
        ready = len(top_details["matched_skills"])
        total = len(top_details["required_skills"])
        a, b = st.columns(2)
        with a:
            st.metric("Ready skills", f"{ready}/{total}")
        with b:
            st.metric("To develop", total - ready)
        st.write("")
        st.markdown("<div class='glass-panel'><div class='section-kicker'>WHY THIS MATCH?</div><div style='color:#c2c9da;font-size:13px;line-height:1.65;'>Each required skill contributes to the career readiness score. The underlying skill scores combine perceived confidence with objective knowledge evidence.</div></div>", unsafe_allow_html=True)

    st.write("")
    st.markdown("<div class='section-kicker'>CAREER DIRECTIONS</div>", unsafe_allow_html=True)
    career_cols = st.columns(len(careers), gap="medium")
    for idx, (col, career) in enumerate(zip(career_cols, careers), start=1):
        details = get_career_match_details(user_profile, career)
        with col:
            st.markdown(f"<div class='career-card'><div class='career-rank'>0{idx} / CAREER PATH</div><div class='career-name'>{career}</div><div style='margin-top:10px;'><span class='career-score'>{details['match_score']}% match</span></div></div>", unsafe_allow_html=True)

    st.write("")
    selected_career = st.selectbox("Explore a career in detail", careers)
    selected_details = get_career_match_details(user_profile, selected_career)
    skill_gap = analyze_skill_gap(user_profile, selected_career)

    # Protect against an old imported skill_gap module during a hot reload.
    if "skill_rows" not in skill_gap:
        skill_gap["skill_rows"] = selected_details["skill_rows"]
    if "matched_skills" not in skill_gap:
        skill_gap["matched_skills"] = [row["skill"] for row in skill_gap["skill_rows"] if row["current_score"] >= row["required_score"]]
    if "missing_skills" not in skill_gap:
        skill_gap["missing_skills"] = [row["skill"] for row in skill_gap["skill_rows"] if row["current_score"] < row["required_score"]]
    if "coverage" not in skill_gap:
        skill_gap["coverage"] = selected_details["match_score"]

    st.write("")
    metric1, metric2, metric3, metric4 = st.columns(4, gap="medium")
    with metric1:
        st.metric("Career Match", f"{selected_details['match_score']}%")
    with metric2:
        st.metric("Ready", len(skill_gap["matched_skills"]))
    with metric3:
        st.metric("To Develop", len(skill_gap["missing_skills"]))
    with metric4:
        skill_coverage = skill_gap.get("coverage", selected_details["match_score"])
        st.metric("Skill Coverage", f"{skill_coverage}%")

    overview_tab, skills_tab, roadmap_tab = st.tabs(["Overview", "Skill Intelligence", "Roadmap"])

    with overview_tab:
        chart_col, profile_col = st.columns([1.15, .85], gap="large")
        with chart_col:
            st.markdown("<div class='section-kicker'>CURRENT VS TARGET</div>", unsafe_allow_html=True)
            rows = skill_gap["skill_rows"]
            labels = [row["skill"].title() for row in rows]
            current_scores = [row["current_score"] for row in rows]
            target_scores = [row["required_score"] for row in rows]
            chart = go.Figure()
            chart.add_trace(go.Bar(y=labels, x=current_scores, orientation="h", name="Current", marker=dict(color="#a78bfa")))
            chart.add_trace(go.Bar(y=labels, x=target_scores, orientation="h", name="Target", marker=dict(color="rgba(255,255,255,.10)")))
            chart.update_layout(barmode="overlay", height=max(330, 72 * len(rows)), margin=dict(l=10,r=30,t=10,b=20), xaxis=dict(range=[0,100], title="Score", gridcolor="rgba(255,255,255,.05)"), yaxis=dict(autorange="reversed"), paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font=dict(color="#dce2ed"), legend=dict(orientation="h", y=1.08, x=0))
            st.plotly_chart(chart, use_container_width=True, config={"displayModeBar":False})

        with profile_col:
            st.markdown("<div class='section-kicker'>PROFILE SNAPSHOT</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='glass-panel'><div class='muted-small'>STUDENT</div><div style='font-size:25px;font-weight:900;color:#f4f6ff;margin-top:5px;'>{user_profile['name']}</div><div style='color:#9aa4bd;margin-top:5px;'>{user_profile['branch']} • {user_profile['semester']} Semester</div><hr><div class='muted-small'>SELECTED CAREER</div><div style='font-size:22px;font-weight:850;color:#dcd8ff;margin-top:5px;'>{selected_career}</div></div>", unsafe_allow_html=True)
            st.write("")
            st.markdown("<div class='section-kicker'>READY NOW</div>", unsafe_allow_html=True)
            if skill_gap["matched_skills"]:
                for skill in skill_gap["matched_skills"]:
                    score = user_profile["skill_scores"].get(skill, 0)
                    st.markdown(f"<div style='display:flex;justify-content:space-between;padding:11px 0;border-bottom:1px solid rgba(255,255,255,.06);'><span style='font-weight:750;color:#eaf8f3;'>✓ {skill.title()}</span><span style='color:#75e2be;font-weight:850;'>{score}%</span></div>", unsafe_allow_html=True)
            else:
                st.info("No required skill has reached the target yet.")

    with skills_tab:
        st.markdown("<div class='section-kicker'>SKILL INTELLIGENCE</div>", unsafe_allow_html=True)
        st.header("What you know vs what the career needs.")
        st.caption("Prototype target level: 70%. Larger gaps are automatically prioritised.")
        for row in skill_gap["skill_rows"]:
            priority = row["priority"]
            css_class = priority_class(priority)
            st.markdown(f"<div style='display:flex;justify-content:space-between;align-items:end;margin-top:18px;'><div><div style='font-size:17px;font-weight:850;color:#f3f5ff;'>{row['skill'].title()}</div><div class='muted-small'>Current {row['current_score']}% • Target {row['required_score']}% • Gap {row['gap']} points</div></div><div class='chip {css_class}'>{priority}</div></div>", unsafe_allow_html=True)
            st.progress(min(row["current_score"] / 100, 1.0))
        st.write("")
        st.markdown("<div class='glass-panel'><div class='section-kicker'>INTERPRETATION</div><div style='color:#c1c8da;line-height:1.65;font-size:13px;'>Instead of only saying that a skill is present or absent, the system shows the student's current score, target level, gap and development priority.</div></div>", unsafe_allow_html=True)

    with roadmap_tab:
        st.markdown("<div class='section-kicker'>05 / PERSONALIZED LEARNING ROADMAP</div>", unsafe_allow_html=True)
        st.header("What should you learn next?")
        st.caption("Each step is generated from the selected career's skill gaps.")
        roadmap = generate_roadmap(skill_gap)
        if roadmap["roadmap_steps"]:
            for index, step in enumerate(roadmap["roadmap_steps"], start=1):
                css_class = priority_class(step["priority"])
                st.markdown(f"<div style='display:flex;gap:18px;padding:18px 0 10px;border-bottom:1px solid rgba(255,255,255,.06);'><div style='font-size:32px;font-weight:900;color:#303653;min-width:58px;'>{index:02d}</div><div><div class='chip {css_class}'>{step['priority']} PRIORITY</div><div style='font-size:24px;font-weight:850;color:#f6f7ff;margin-top:9px;'>{step['skill'].title()}</div><div class='muted-small'>Current {step['current_score']}% • Target {step['required_score']}% • Gap {step['gap']} points</div></div></div>", unsafe_allow_html=True)
                c1, c2, c3 = st.columns(3, gap="medium")
                with c1:
                    st.markdown(f"<div class='roadmap-box'><div class='roadmap-kicker'>LEARN</div><div class='roadmap-text'>{step['learn']}</div></div>", unsafe_allow_html=True)
                with c2:
                    st.markdown(f"<div class='roadmap-box'><div class='roadmap-kicker'>PRACTICE</div><div class='roadmap-text'>{step['practice']}</div></div>", unsafe_allow_html=True)
                with c3:
                    st.markdown(f"<div class='roadmap-box'><div class='roadmap-kicker'>BUILD</div><div class='roadmap-text'>{step['build']}</div></div>", unsafe_allow_html=True)

                # Direct learning resources: one curated reference plus a YouTube learning search.
                learn_url = step.get('learn_url', '')
                learn_label = step.get('learn_label', 'Start learning')
                video_url = step.get('video_url', '')
                st.markdown(
                    f"<div class='resource-panel'><div class='resource-sub'>START LEARNING</div>"
                    f"<div style='display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:8px;'>"
                    f"<a class='resource-link' href='{learn_url}' target='_blank' rel='noopener noreferrer'><span>📖 {learn_label}</span><span class='resource-arrow'>↗</span></a>"
                    f"<a class='resource-link' href='{video_url}' target='_blank' rel='noopener noreferrer'><span>▶ YouTube lessons</span><span class='resource-arrow'>↗</span></a>"
                    f"</div></div>",
                    unsafe_allow_html=True,
                )
        else:
            st.success("🎉 You currently meet the prototype target for every required skill in this career.")


if st.session_state.get("scroll_to_results", False):
    components.html("""
    <script>
    setTimeout(function(){
        const target = window.parent.document.getElementById('career-results');
        if(target){target.scrollIntoView({behavior:'smooth', block:'start'});}
    }, 250);
    </script>
    """, height=1)
    st.session_state["scroll_to_results"] = False

st.write("")
st.divider()
st.markdown("<div style='padding:8px 0 0;color:#626d85;font-size:11px;letter-spacing:.08em;'>CAREERGUIDE AI • PERSONALIZED CAREER GUIDANCE WITH SKILL GAP ANALYSIS</div>", unsafe_allow_html=True)
