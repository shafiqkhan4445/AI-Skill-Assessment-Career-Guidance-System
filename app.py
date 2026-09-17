import streamlit as st
import streamlit.components.v1 as components
import plotly.graph_objects as go

from recommendation import recommend_careers, CAREER_SKILL_MAP
from skill_gap import analyze_skill_gap
from roadmap import generate_roadmap


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="CareerGuide AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

    /* ========================================================
       GLOBAL DESIGN
       ======================================================== */

    :root {
        --primary: #9b8cff;
        --primary-soft: #c8c2ff;
        --secondary: #70b7ff;
        --success: #5ed6a0;
        --text: #f2f4f8;
        --muted: #7f899d;
    }

    html {
        scroll-behavior: smooth !important;
    }

    .stApp {
        background:
            radial-gradient(
                circle at 10% 5%,
                rgba(100, 82, 210, 0.15),
                transparent 25%
            ),
            radial-gradient(
                circle at 92% 12%,
                rgba(60, 130, 220, 0.08),
                transparent 24%
            ),
            #080b11;

        color: var(--text);
    }

    .block-container {
        max-width: 1320px;
        padding-top: 1.25rem;
        padding-bottom: 5rem;
    }

    #MainMenu,
    footer {
        visibility: hidden;
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    section[data-testid="stSidebar"] {
        display: none;
    }


    /* ========================================================
       TYPOGRAPHY
       ======================================================== */

    h1 {
        font-size: 68px !important;
        line-height: 0.98 !important;
        letter-spacing: -3px !important;
        font-weight: 850 !important;

        background:
            linear-gradient(
                120deg,
                #ffffff 10%,
                var(--primary-soft) 46%,
                var(--secondary) 90%
            );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    h2 {
        font-size: 32px !important;
        line-height: 1.1 !important;
        letter-spacing: -1px !important;
        font-weight: 800 !important;
    }

    h3 {
        font-weight: 700 !important;
    }

    .stCaption {
        color: var(--muted) !important;
    }


    /* ========================================================
       INPUTS
       ======================================================== */

    div[data-baseweb="input"] > div,
    div[data-baseweb="select"] > div {

        background:
            rgba(20, 24, 34, 0.82) !important;

        border:
            1px solid rgba(145, 155, 190, 0.16) !important;

        border-radius: 11px !important;
    }

    [data-baseweb="tag"] {
        border-radius: 20px !important;
    }


    /* ========================================================
       PRIMARY BUTTON
       ======================================================== */

    button[kind="primary"] {

        background:
            linear-gradient(
                135deg,
                #9b8cff,
                #70b7ff
            ) !important;

        color: #090c13 !important;

        border: none !important;

        min-height: 50px;

        border-radius: 13px !important;

        font-weight: 800 !important;

        box-shadow:
            0 12px 28px rgba(100, 110, 230, 0.20);

        transition:
            transform 0.18s ease,
            box-shadow 0.18s ease;
    }

    button[kind="primary"]:hover {

        transform: translateY(-2px);

        box-shadow:
            0 16px 34px rgba(100, 110, 230, 0.30);
    }


    /* ========================================================
       METRICS
       ======================================================== */

    [data-testid="stMetric"] {

        background: transparent !important;

        border: none !important;

        padding: 0 !important;

        box-shadow: none !important;
    }

    [data-testid="stMetricLabel"] {
        color: var(--muted) !important;
    }

    [data-testid="stMetricValue"] {
        font-size: 34px !important;
        font-weight: 800 !important;
    }


    /* ========================================================
       PROGRESS BARS
       ======================================================== */

    [data-testid="stProgressBar"] {

        background:
            rgba(255, 255, 255, 0.055);

        border-radius: 20px;

        overflow: hidden;
    }

    [data-testid="stProgressBar"] > div > div {

        background:
            linear-gradient(
                90deg,
                #9b8cff,
                #70b7ff
            ) !important;

        border-radius: 20px;
    }


    /* ========================================================
       TABS
       ======================================================== */

    button[data-baseweb="tab"] {

        font-size: 14px !important;

        font-weight: 750 !important;

        color: #7f899d !important;

        padding-left: 18px !important;

        padding-right: 18px !important;
    }

    button[data-baseweb="tab"][aria-selected="true"] {

        color: #c8c2ff !important;
    }


    /* ========================================================
       DIVIDERS
       ======================================================== */

    hr {

        border-color:
            rgba(130, 140, 170, 0.10) !important;

        margin-top: 28px !important;

        margin-bottom: 28px !important;
    }


    /* ========================================================
       ALERTS
       ======================================================== */

    div[data-testid="stAlert"] {
        border-radius: 11px;
    }


    /* ========================================================
       RESULT ANCHOR
       ======================================================== */

    .results-anchor {
        scroll-margin-top: 35px;
        height: 1px;
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.caption(
    "CAREERGUIDE AI  /  STUDENT CAREER INTELLIGENCE"
)

st.write("")

hero_left, hero_right = st.columns(
    [1.7, 0.8],
    gap="large"
)

with hero_left:

    st.caption(
        "✦ PERSONALIZED CAREER DISCOVERY"
    )

    st.title(
        "Know your skills.\n"
        "Map your future."
    )

    st.write(
        "Career guidance designed around the reality of "
        "college students — understand what you already know, "
        "discover suitable career directions, and identify "
        "what to learn next."
    )

    st.write("")

    st.caption(
        "Start below to explore your career direction ↓"
    )


with hero_right:

    st.write("")

    st.caption("DESIGNED FOR")

    st.markdown(
        "### College Students"
    )

    st.write("")

    st.caption("CORE OUTPUTS")

    st.markdown(
        "### Career • Skills • Roadmap"
    )

    st.write("")

    st.caption(
        "A student-focused system for career exploration "
        "and skill development."
    )


# ============================================================
# EXPERIENCE
# ============================================================

st.write("")
st.write("")

st.caption("THE EXPERIENCE")

st.markdown(
    """
    **01 Profile**
    &nbsp; → &nbsp;
    **02 Assess**
    &nbsp; → &nbsp;
    **03 Discover**
    &nbsp; → &nbsp;
    **04 Identify Gaps**
    &nbsp; → &nbsp;
    **05 Build Roadmap**
    """
)


# ============================================================
# PROFILE
# ============================================================

st.divider()

profile_title, profile_note = st.columns(
    [1.8, 1]
)

with profile_title:

    st.caption("01 / YOUR PROFILE")

    st.header(
        "Start with where you are."
    )

with profile_note:

    st.caption(
        "Your academic context helps frame "
        "the career guidance experience."
    )


profile_col1, profile_col2, profile_col3 = st.columns(
    3,
    gap="large"
)

with profile_col1:

    name = st.text_input(
        "Full Name",
        placeholder="e.g. Shafiq Khan"
    )

with profile_col2:

    branch = st.selectbox(
        "Branch",
        [
            "CSE",
            "ISE",
            "ECE",
            "EEE",
            "Other"
        ]
    )

with profile_col3:

    semester = st.selectbox(
        "Semester",
        [
            "1st",
            "2nd",
            "3rd",
            "4th",
            "5th",
            "6th",
            "7th",
            "8th"
        ]
    )


# ============================================================
# CURRENT SKILLS
# ============================================================

st.write("")

skill_title, skill_note = st.columns(
    [1.8, 1]
)

with skill_title:

    st.caption("02 / CURRENT SKILL PROFILE")

    st.header(
        "What can you already do?"
    )

with skill_note:

    st.caption(
        "Temporary selector for testing. "
        "This will be replaced by your teammate's "
        "assessment module."
    )


available_skills = [
    "Python",
    "SQL",
    "Excel",
    "Data Visualization",
    "HTML",
    "CSS",
    "JavaScript",
    "React",
    "Java",
    "Databases",
    "Machine Learning",
    "Statistics"
]

selected_skills = st.multiselect(
    "Technical skills",
    available_skills,
    placeholder="Search and select your current skills..."
)


# ============================================================
# GENERATE BUTTON
# ============================================================

st.write("")

_, cta_col, _ = st.columns(
    [1.25, 1, 1.25]
)

with cta_col:

    analyze = st.button(
        "✨ Generate Career Insights",
        type="primary",
        use_container_width=True
    )


# ============================================================
# ANALYZE
# ============================================================

if analyze:

    if not name:

        st.warning(
            "Please enter your name."
        )

    elif not selected_skills:

        st.warning(
            "Please select at least one skill."
        )

    else:

        user_profile = {
            "name": name,
            "branch": branch,
            "semester": semester,
            "skills": selected_skills
        }

        careers = recommend_careers(
            user_profile
        )

        st.session_state["user_profile"] = (
            user_profile
        )

        st.session_state["careers"] = (
            careers
        )

        # Tell the page to scroll after results render
        st.session_state["scroll_to_results"] = True


# ============================================================
# RESULTS
# ============================================================

if (
    "careers" in st.session_state
    and st.session_state["careers"]
):

    user_profile = st.session_state[
        "user_profile"
    ]

    careers = st.session_state[
        "careers"
    ]

    # Invisible anchor where scrolling should stop
    st.markdown(
        '<div id="career-results" class="results-anchor"></div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # RESULT INTRO
    # ========================================================

    st.divider()

    st.caption(
        "03 / YOUR CAREER DIRECTION"
    )

    st.header(
        "Here is what your profile points toward."
    )

    st.caption(
        f"{user_profile['branch']} • "
        f"{user_profile['semester']} Semester • "
        f"{len(user_profile['skills'])} current skills"
    )


    # ========================================================
    # TOP CAREER
    # ========================================================

    top_career = careers[0]

    top_gap = analyze_skill_gap(
        user_profile,
        top_career
    )

    top_matched = top_gap[
        "matched_skills"
    ]

    top_missing = top_gap[
        "missing_skills"
    ]

    top_required = (
        len(top_matched)
        + len(top_missing)
    )

    top_percentage = (
        round(
            len(top_matched)
            / top_required
            * 100
        )
        if top_required
        else 0
    )


    top_left, top_match, top_skills = st.columns(
        [1.65, 0.55, 0.55],
        gap="large"
    )

    with top_left:

        st.caption(
            "STRONGEST CAREER ALIGNMENT"
        )

        st.markdown(
            f"# {top_career}"
        )

        st.write(
            "Your current skill profile shows its strongest "
            "alignment with this career path in the current system."
        )

        st.progress(
            top_percentage / 100
        )

        st.caption(
            f"{top_percentage}% of required skills currently matched"
        )

    with top_match:

        st.caption("MATCH")

        st.markdown(
            f"# {top_percentage}%"
        )

    with top_skills:

        st.caption("SKILLS")

        st.markdown(
            f"# {len(top_matched)}/{top_required}"
        )


    # ========================================================
    # OTHER CAREER DIRECTIONS
    # ========================================================

    st.write("")
    st.write("")

    st.caption(
        "OTHER CAREER DIRECTIONS"
    )

    other_careers = []
    other_percentages = []

    for career in careers:

        if career == top_career:
            continue

        required = set(
            CAREER_SKILL_MAP[career]
        )

        current = set(
            s.lower()
            for s in user_profile["skills"]
        )

        matched = required.intersection(
            current
        )

        percentage = round(
            len(matched)
            / len(required)
            * 100
        )

        other_careers.append(
            career
        )

        other_percentages.append(
            percentage
        )


    if other_careers:

        career_chart = go.Figure()

        career_chart.add_trace(
            go.Bar(
                x=other_percentages,
                y=other_careers,
                orientation="h",
                marker=dict(
                    color="#70b7ff"
                ),
                text=[
                    f"{x}%"
                    for x in other_percentages
                ],
                textposition="outside",
                cliponaxis=False
            )
        )

        career_chart.update_layout(
            height=max(
                220,
                130 * len(other_careers)
            ),
            xaxis=dict(
                range=[
                    0,
                    100
                ],
                visible=False
            ),
            yaxis=dict(
                title=""
            ),
            margin=dict(
                l=10,
                r=60,
                t=10,
                b=10
            ),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(
                color="#dce2ed"
            ),
            showlegend=False
        )

        st.plotly_chart(
            career_chart,
            use_container_width=True,
            config={
                "displayModeBar": False
            }
        )


    # ========================================================
    # CAREER SELECTOR
    # ========================================================

    st.write("")

    selected_career = st.selectbox(
        "Explore a career in detail",
        careers
    )


    # ========================================================
    # SELECTED CAREER ANALYSIS
    # ========================================================

    skill_gap = analyze_skill_gap(
        user_profile,
        selected_career
    )

    matched_skills = skill_gap[
        "matched_skills"
    ]

    missing_skills = skill_gap[
        "missing_skills"
    ]

    total_required = (
        len(matched_skills)
        + len(missing_skills)
    )

    match_percentage = (
        round(
            len(matched_skills)
            / total_required
            * 100
        )
        if total_required
        else 0
    )


    # ========================================================
    # SUMMARY METRICS
    # ========================================================

    st.divider()

    metric1, metric2, metric3, metric4 = st.columns(
        4
    )

    with metric1:

        st.metric(
            "Career Match",
            f"{match_percentage}%"
        )

    with metric2:

        st.metric(
            "Matched",
            len(matched_skills)
        )

    with metric3:

        st.metric(
            "To Develop",
            len(missing_skills)
        )

    with metric4:

        st.metric(
            "Required",
            total_required
        )


    # ========================================================
    # RESULT TABS
    # ========================================================

    st.write("")

    overview_tab, skills_tab, roadmap_tab = st.tabs(
        [
            "Overview",
            "Skill Intelligence",
            "Roadmap"
        ]
    )


    # ========================================================
    # OVERVIEW TAB
    # ========================================================

    with overview_tab:

        chart_left, chart_right = st.columns(
            [1.1, 0.95],
            gap="large"
        )


        # ----------------------------------------------------
        # DONUT
        # ----------------------------------------------------

        with chart_left:

            st.caption(
                "SKILL COVERAGE"
            )

            donut = go.Figure(
                data=[
                    go.Pie(
                        labels=[
                            "Matched",
                            "To Develop"
                        ],
                        values=[
                            len(matched_skills),
                            len(missing_skills)
                        ],
                        hole=0.76,
                        textinfo="percent",
                        marker=dict(
                            colors=[
                                "#9b8cff",
                                "#252b39"
                            ]
                        ),
                        hovertemplate=
                        "%{label}: %{value}"
                        "<extra></extra>"
                    )
                ]
            )

            donut.update_layout(
                height=390,
                margin=dict(
                    l=5,
                    r=5,
                    t=5,
                    b=5
                ),
                showlegend=True,
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font=dict(
                    color="#dce2ed"
                ),
                legend=dict(
                    orientation="h",
                    y=-0.03
                )
            )

            st.plotly_chart(
                donut,
                use_container_width=True,
                config={
                    "displayModeBar": False
                }
            )


        # ----------------------------------------------------
        # PROFILE
        # ----------------------------------------------------

        with chart_right:

            st.caption(
                "YOUR PROFILE"
            )

            st.markdown(
                f"## {user_profile['name']}"
            )

            st.caption(
                f"{user_profile['branch']} • "
                f"{user_profile['semester']} Semester"
            )

            st.write("")

            st.caption(
                "CURRENT CAREER PATH"
            )

            st.markdown(
                f"### {selected_career}"
            )

            st.write("")

            st.caption(
                "MATCH"
            )

            st.markdown(
                f"# {match_percentage}%"
            )

            st.progress(
                match_percentage / 100
            )


        # ----------------------------------------------------
        # RADAR CHART
        # ----------------------------------------------------

        st.divider()

        st.caption(
            "SKILL PROFILE"
        )

        required_skills = list(
            CAREER_SKILL_MAP[
                selected_career
            ]
        )

        normalized = [
            s.lower()
            for s in user_profile["skills"]
        ]

        radar_values = []

        for skill in required_skills:

            if skill.lower() in normalized:

                radar_values.append(
                    100
                )

            else:

                radar_values.append(
                    15
                )


        radar = go.Figure()

        radar.add_trace(
            go.Scatterpolar(
                r=radar_values,
                theta=required_skills,
                fill="toself",
                line=dict(
                    color="#9b8cff",
                    width=2
                ),
                fillcolor=
                "rgba(155,140,255,0.18)"
            )
        )

        radar.update_layout(
            height=470,
            polar=dict(
                bgcolor="rgba(0,0,0,0)",
                radialaxis=dict(
                    visible=True,
                    range=[
                        0,
                        100
                    ],
                    gridcolor=
                    "rgba(150,160,190,0.12)"
                ),
                angularaxis=dict(
                    gridcolor=
                    "rgba(150,160,190,0.12)"
                )
            ),
            paper_bgcolor="rgba(0,0,0,0)",
            font=dict(
                color="#dce2ed"
            ),
            margin=dict(
                l=30,
                r=30,
                t=20,
                b=20
            ),
            showlegend=False
        )

        st.plotly_chart(
            radar,
            use_container_width=True,
            config={
                "displayModeBar": False
            }
        )


    # ========================================================
    # SKILL INTELLIGENCE TAB
    # ========================================================

    with skills_tab:

        strength_col, gap_col = st.columns(
            [1, 1],
            gap="large"
        )


        with strength_col:

            st.caption(
                "YOU ALREADY HAVE"
            )

            if matched_skills:

                for skill in sorted(
                    matched_skills
                ):

                    st.markdown(
                        f"### ✓ {skill.title()}"
                    )

                    st.progress(
                        1.0
                    )

            else:

                st.info(
                    "No matched skills yet."
                )


        with gap_col:

            st.caption(
                "YOUR NEXT SKILLS"
            )

            if missing_skills:

                for skill in sorted(
                    missing_skills
                ):

                    st.markdown(
                        f"### ＋ {skill.title()}"
                    )

                    st.progress(
                        0.18
                    )

            else:

                st.success(
                    "No major skill gaps identified."
                )


        st.divider()

        st.caption(
            "REQUIRED SKILL COVERAGE"
        )

        coverage_values = []

        for skill in required_skills:

            if skill.lower() in normalized:

                coverage_values.append(
                    100
                )

            else:

                coverage_values.append(
                    0
                )


        bar = go.Figure()

        bar.add_trace(
            go.Bar(
                x=coverage_values,
                y=required_skills,
                orientation="h",
                marker=dict(
                    color=[
                        "#9b8cff"
                        if x == 100
                        else "#252b39"
                        for x in coverage_values
                    ]
                )
            )
        )

        bar.update_layout(
            height=400,
            xaxis=dict(
                range=[
                    0,
                    100
                ],
                title="Coverage"
            ),
            yaxis=dict(
                title=""
            ),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(
                color="#dce2ed"
            ),
            margin=dict(
                l=20,
                r=20,
                t=20,
                b=40
            )
        )

        st.plotly_chart(
            bar,
            use_container_width=True,
            config={
                "displayModeBar": False
            }
        )


    # ========================================================
    # ROADMAP TAB
    # ========================================================

    with roadmap_tab:

        st.caption(
            "04 / PERSONALIZED LEARNING ROADMAP"
        )

        st.header(
            "What should you learn next?"
        )

        st.caption(
            "A learning sequence generated from "
            "your identified skill gaps."
        )

        roadmap = generate_roadmap(
            skill_gap
        )


        if roadmap["roadmap_steps"]:

            for i, step in enumerate(
                roadmap["roadmap_steps"],
                start=1
            ):

                number_col, content_col = st.columns(
                    [0.12, 0.88]
                )

                with number_col:

                    st.markdown(
                        f"# {i:02d}"
                    )

                with content_col:

                    st.caption(
                        f"STEP {i:02d}"
                    )

                    st.markdown(
                        f"## {step['skill'].title()}"
                    )

                    learn_col, build_col = st.columns(
                        2
                    )

                    with learn_col:

                        st.caption(
                            "LEARN"
                        )

                        st.write(
                            step["resources"]
                        )

                    with build_col:

                        st.caption(
                            "BUILD"
                        )

                        st.write(
                            step["project"]
                        )

                st.divider()

        else:

            st.success(
                "🎉 You currently have all the required "
                "skills for this career."
            )


# ============================================================
# NO RESULTS
# ============================================================

elif "careers" in st.session_state:

    st.warning(
        "No matching careers were found. "
        "Try selecting additional skills."
    )


# ============================================================
# SMOOTH SCROLL AFTER GENERATION
# ============================================================

if st.session_state.get(
    "scroll_to_results",
    False
):

    components.html(
        """
        <script>
            setTimeout(function() {
                window.parent.location.hash =
                    "career-results";
            }, 100);
        </script>
        """,
        height=1
    )

    st.session_state[
        "scroll_to_results"
    ] = False


# ============================================================
# FOOTER
# ============================================================

st.write("")
st.divider()

st.caption(
    "CAREERGUIDE AI • AI-Based Personalized Career "
    "Guidance System with Skill Gap Analysis for Students"
)