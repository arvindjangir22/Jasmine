import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime

# ─── Page Configuration ───
st.set_page_config(
    page_title="Mindful Business Dashboard",
    page_icon="🧘",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Custom CSS ───
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #4A6741;
        text-align: center;
        padding: 1rem 0;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #7A8B73;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
    }
    .stMetric {
        background-color: #f0f4f0;
        border-radius: 10px;
        padding: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
</style>
""", unsafe_allow_html=True)

# ─── Header ───
st.markdown('<div class="main-header">🧘 Mindful Business Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Psychology Practice · Meditation Teaching · Yoga Retreats</div>', unsafe_allow_html=True)
st.divider()

# ─── Sidebar ───
with st.sidebar:
    st.image("https://img.icons8.com/clouds/100/meditation-guru.png", width=80)
    st.title("⚙️ Navigation")
    page = st.radio(
        "Go to",
        ["📊 Dashboard Overview", "👥 Client Management", "🏕️ Retreat Planner", "💰 Financial Summary", "🧭 Business Plan"],
        label_visibility="collapsed",
    )
    st.divider()
    st.markdown("#### 📅 Current Period")
    st.info(f"**{datetime.now().strftime('%B %Y')}**")
    st.divider()
    st.markdown("##### 💡 Quick Rates")
    st.success("Individual Client: **$180 / session**")
    st.warning("Corporate Client: **$300 / session**")


# ═══════════════════════════════════════════════
# 👥 CLIENT MANAGEMENT
# ═══════════════════════════════════════════════
if page == "👥 Client Management":
    st.header("👥 Client Management")
    st.markdown("Manage your **individual** and **corporate** client sessions and projections.")
    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🧑 Individual Clients")
        individual_rate = st.number_input("Rate per Session ($)", value=180, min_value=0, step=10, key="ind_rate")
        individual_sessions_month = st.number_input("Sessions per Month", value=20, min_value=0, step=1, key="ind_sessions")
        individual_revenue_month = individual_rate * individual_sessions_month
        st.metric("Monthly Revenue", f"${individual_revenue_month:,.0f}", delta=f"{individual_sessions_month} sessions")

    with col2:
        st.subheader("🏢 Corporate Clients")
        corporate_rate = st.number_input("Rate per Session ($)", value=300, min_value=0, step=10, key="corp_rate")
        corporate_sessions_month = st.number_input("Sessions per Month", value=8, min_value=0, step=1, key="corp_sessions")
        corporate_revenue_month = corporate_rate * corporate_sessions_month
        st.metric("Monthly Revenue", f"${corporate_revenue_month:,.0f}", delta=f"{corporate_sessions_month} sessions")

    st.divider()
    st.subheader("📈 Revenue Projections")

    total_client_revenue_month = individual_revenue_month + corporate_revenue_month

    projection_data = pd.DataFrame({
        "Period": ["Monthly", "Quarterly", "Semi-Annual", "Annual"],
        "Individual Revenue ($)": [
            individual_revenue_month,
            individual_revenue_month * 3,
            individual_revenue_month * 6,
            individual_revenue_month * 12,
        ],
        "Corporate Revenue ($)": [
            corporate_revenue_month,
            corporate_revenue_month * 3,
            corporate_revenue_month * 6,
            corporate_revenue_month * 12,
        ],
        "Total Revenue ($)": [
            total_client_revenue_month,
            total_client_revenue_month * 3,
            total_client_revenue_month * 6,
            total_client_revenue_month * 12,
        ],
    })

    st.dataframe(projection_data.style.format({
        "Individual Revenue ($)": "${:,.0f}",
        "Corporate Revenue ($)": "${:,.0f}",
        "Total Revenue ($)": "${:,.0f}",
    }), use_container_width=True, hide_index=True)

    # Bar Chart
    fig_clients = go.Figure()
    fig_clients.add_trace(go.Bar(
        name="Individual", x=projection_data["Period"],
        y=projection_data["Individual Revenue ($)"],
        marker_color="#7CB97A",
    ))
    fig_clients.add_trace(go.Bar(
        name="Corporate", x=projection_data["Period"],
        y=projection_data["Corporate Revenue ($)"],
        marker_color="#4A6741",
    ))
    fig_clients.update_layout(
        title="Client Revenue Projections",
        barmode="group", yaxis_title="Revenue ($)",
        template="plotly_white", height=420,
    )
    st.plotly_chart(fig_clients, use_container_width=True)


# ═══════════════════════════════════════════════
# 🏕️ RETREAT PLANNER
# ═══════════════════════════════════════════════
elif page == "🏕️ Retreat Planner":
    st.header("🏕️ Retreat Planner")
    st.markdown("Plan your retreat costs, set pricing, and calculate profitability dynamically.")
    st.divider()

    col_left, col_right = st.columns([3, 2])

    with col_left:
        st.subheader("💸 Retreat Cost Breakdown")
        st.markdown("Enter the estimated cost for each category:")

        c1, c2 = st.columns(2)
        with c1:
            venue_cost = st.number_input("🏠 Venue / Location ($)", value=2000, min_value=0, step=100)
            food_cost = st.number_input("🍽️ Food & Beverages ($)", value=1500, min_value=0, step=100)
            travel_cost = st.number_input("✈️ Travel & Transport ($)", value=800, min_value=0, step=100)
            staff_cost = st.number_input("👨‍🏫 Staff / Assistants ($)", value=1000, min_value=0, step=100)
        with c2:
            materials_cost = st.number_input("📦 Materials & Supplies ($)", value=500, min_value=0, step=50)
            marketing_cost = st.number_input("📣 Marketing & Ads ($)", value=600, min_value=0, step=50)
            insurance_cost = st.number_input("🛡️ Insurance ($)", value=300, min_value=0, step=50)
            misc_cost = st.number_input("🔧 Miscellaneous ($)", value=300, min_value=0, step=50)

        total_retreat_cost = (venue_cost + food_cost + travel_cost + staff_cost
                             + materials_cost + marketing_cost + insurance_cost + misc_cost)

    with col_right:
        st.subheader("🎟️ Retreat Pricing")
        num_participants = st.number_input("Expected Participants", value=20, min_value=1, step=1)
        ticket_price = st.number_input("Ticket Price per Participant ($)", value=500, min_value=0, step=25)

        retreat_revenue = num_participants * ticket_price
        retreat_profit = retreat_revenue - total_retreat_cost
        profit_margin = (retreat_profit / retreat_revenue * 100) if retreat_revenue > 0 else 0
        breakeven = int(total_retreat_cost / ticket_price) + 1 if ticket_price > 0 else 0
        cost_per_participant = total_retreat_cost / num_participants if num_participants > 0 else 0

        st.divider()
        st.metric("Total Retreat Cost", f"${total_retreat_cost:,.0f}")
        st.metric("Retreat Revenue", f"${retreat_revenue:,.0f}")
        st.metric("Retreat Profit", f"${retreat_profit:,.0f}",
                  delta=f"{profit_margin:.1f}% margin",
                  delta_color="normal" if retreat_profit >= 0 else "inverse")
        st.metric("Break-even Participants", f"{breakeven}")
        st.metric("Cost per Participant", f"${cost_per_participant:,.0f}")

    st.divider()

    col_pie, col_bar = st.columns(2)

    cost_labels = ["Venue", "Food", "Travel", "Staff", "Materials", "Marketing", "Insurance", "Misc"]
    cost_values = [venue_cost, food_cost, travel_cost, staff_cost,
                   materials_cost, marketing_cost, insurance_cost, misc_cost]

    with col_pie:
        fig_pie = px.pie(
            names=cost_labels, values=cost_values,
            title="Retreat Cost Breakdown",
            color_discrete_sequence=px.colors.sequential.Emrld,
            hole=0.4,
        )
        fig_pie.update_layout(height=420, template="plotly_white")
        st.plotly_chart(fig_pie, use_container_width=True)

    with col_bar:
        # Break-even chart
        participants_range = list(range(1, num_participants + 10))
        revenues = [p * ticket_price for p in participants_range]
        costs = [total_retreat_cost] * len(participants_range)
        fig_be = go.Figure()
        fig_be.add_trace(go.Scatter(x=participants_range, y=revenues, name="Revenue",
                                     line=dict(color="#4A6741", width=3)))
        fig_be.add_trace(go.Scatter(x=participants_range, y=costs, name="Total Cost",
                                     line=dict(color="#D94F4F", width=3, dash="dash")))
        fig_be.update_layout(title="Break-even Analysis", xaxis_title="Participants",
                             yaxis_title="Amount ($)", template="plotly_white", height=420)
        st.plotly_chart(fig_be, use_container_width=True)


# ═══════════════════════════════════════════════
# 📊 DASHBOARD OVERVIEW
# ═══════════════════════════════════════════════
elif page == "📊 Dashboard Overview":
    st.header("📊 Dashboard Overview")
    st.markdown("A consolidated view of your **entire business** — clients + retreats.")
    st.divider()

    # ── Inputs in expanders ──
    with st.expander("⚙️ Adjust Client Inputs", expanded=False):
        dc1, dc2 = st.columns(2)
        with dc1:
            d_ind_rate = st.number_input("Individual Rate ($)", value=180, min_value=0, step=10, key="d_ind_rate")
            d_ind_sess = st.number_input("Individual Sessions / Month", value=20, min_value=0, step=1, key="d_ind_sess")
        with dc2:
            d_corp_rate = st.number_input("Corporate Rate ($)", value=300, min_value=0, step=10, key="d_corp_rate")
            d_corp_sess = st.number_input("Corporate Sessions / Month", value=8, min_value=0, step=1, key="d_corp_sess")

    with st.expander("⚙️ Adjust Retreat Inputs", expanded=False):
        dr1, dr2 = st.columns(2)
        with dr1:
            d_retreat_cost = st.number_input("Total Retreat Cost ($)", value=7000, min_value=0, step=500, key="d_ret_cost")
            d_retreats_year = st.number_input("Retreats per Year", value=4, min_value=0, step=1, key="d_ret_year")
        with dr2:
            d_ret_participants = st.number_input("Avg Participants / Retreat", value=20, min_value=1, step=1, key="d_ret_part")
            d_ret_ticket = st.number_input("Ticket Price ($)", value=500, min_value=0, step=25, key="d_ret_ticket")

    with st.expander("⚙️ Monthly Business Expenses", expanded=False):
        be1, be2, be3 = st.columns(3)
        with be1:
            d_rent = st.number_input("Office / Studio Rent ($)", value=1200, min_value=0, step=100, key="d_rent")
        with be2:
            d_software = st.number_input("Software & Tools ($)", value=150, min_value=0, step=25, key="d_sw")
        with be3:
            d_other_exp = st.number_input("Other Monthly Expenses ($)", value=300, min_value=0, step=50, key="d_other")

    # ── Calculations ──
    monthly_ind_rev = d_ind_rate * d_ind_sess
    monthly_corp_rev = d_corp_rate * d_corp_sess
    monthly_client_rev = monthly_ind_rev + monthly_corp_rev
    annual_client_rev = monthly_client_rev * 12

    annual_retreat_rev = d_ret_participants * d_ret_ticket * d_retreats_year
    annual_retreat_cost = d_retreat_cost * d_retreats_year
    annual_retreat_profit = annual_retreat_rev - annual_retreat_cost

    monthly_expenses = d_rent + d_software + d_other_exp
    annual_expenses = monthly_expenses * 12

    total_annual_revenue = annual_client_rev + annual_retreat_rev
    total_annual_cost = annual_retreat_cost + annual_expenses
    net_profit = total_annual_revenue - total_annual_cost
    net_margin = (net_profit / total_annual_revenue * 100) if total_annual_revenue > 0 else 0

    # ── KPI Cards ──
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("💵 Total Annual Revenue", f"${total_annual_revenue:,.0f}")
    k2.metric("📉 Total Annual Costs", f"${total_annual_cost:,.0f}")
    k3.metric("✅ Net Profit", f"${net_profit:,.0f}",
              delta=f"{net_margin:.1f}% margin",
              delta_color="normal" if net_profit >= 0 else "inverse")
    k4.metric("📆 Avg Monthly Income", f"${net_profit / 12:,.0f}")

    st.divider()

    # ── Charts Row 1 ──
    ch1, ch2 = st.columns(2)

    with ch1:
        fig_rev = px.bar(
            x=["Individual Clients", "Corporate Clients", "Retreats"],
            y=[annual_client_rev - monthly_corp_rev * 12,
               monthly_corp_rev * 12,
               annual_retreat_rev],
            labels={"x": "Revenue Stream", "y": "Annual Revenue ($)"},
            title="Revenue by Stream (Annual)",
            color=["Individual Clients", "Corporate Clients", "Retreats"],
            color_discrete_map={
                "Individual Clients": "#7CB97A",
                "Corporate Clients": "#4A6741",
                "Retreats": "#A8D5A2",
            },
        )
        fig_rev.update_layout(template="plotly_white", height=400, showlegend=False)
        st.plotly_chart(fig_rev, use_container_width=True)

    with ch2:
        fig_cost_pie = px.pie(
            names=["Retreat Costs", "Rent", "Software & Tools", "Other Expenses"],
            values=[annual_retreat_cost, d_rent * 12, d_software * 12, d_other_exp * 12],
            title="Annual Cost Breakdown",
            hole=0.45,
            color_discrete_sequence=px.colors.sequential.Teal,
        )
        fig_cost_pie.update_layout(template="plotly_white", height=400)
        st.plotly_chart(fig_cost_pie, use_container_width=True)

    # ── Monthly Projection (12 months) ──
    st.subheader("📈 12-Month Revenue & Profit Projection")
    months = [f"Month {i}" for i in range(1, 13)]
    monthly_total_rev = [monthly_client_rev + (annual_retreat_rev / 12)] * 12
    monthly_total_cost = [monthly_expenses + (annual_retreat_cost / 12)] * 12
    monthly_profit = [r - c for r, c in zip(monthly_total_rev, monthly_total_cost)]

    fig_monthly = go.Figure()
    fig_monthly.add_trace(go.Scatter(x=months, y=monthly_total_rev, name="Revenue",
                                      fill="tozeroy", line=dict(color="#4A6741", width=3)))
    fig_monthly.add_trace(go.Scatter(x=months, y=monthly_total_cost, name="Costs",
                                      fill="tozeroy", line=dict(color="#D94F4F", width=2, dash="dot")))
    fig_monthly.add_trace(go.Scatter(x=months, y=monthly_profit, name="Profit",
                                      line=dict(color="#2E86C1", width=3)))
    fig_monthly.update_layout(template="plotly_white", height=420,
                               yaxis_title="Amount ($)", xaxis_title="Month")
    st.plotly_chart(fig_monthly, use_container_width=True)


# ═══════════════════════════════════════════════
# 💰 FINANCIAL SUMMARY
# ═══════════════════════════════════════════════
elif page == "💰 Financial Summary":
    st.header("💰 Financial Summary & Yearly Projection")
    st.markdown("Detailed profit & loss view with **growth assumptions**.")
    st.divider()

    # Inputs
    with st.expander("⚙️ Configure Financial Inputs", expanded=True):
        f1, f2, f3 = st.columns(3)
        with f1:
            st.markdown("**Client Revenue**")
            f_ind_rate = st.number_input("Individual Rate ($)", value=180, min_value=0, key="f_ind_rate")
            f_ind_sess = st.number_input("Individual Sessions / Mo", value=20, min_value=0, key="f_ind_sess")
            f_corp_rate = st.number_input("Corporate Rate ($)", value=300, min_value=0, key="f_corp_rate")
            f_corp_sess = st.number_input("Corporate Sessions / Mo", value=8, min_value=0, key="f_corp_sess")
        with f2:
            st.markdown("**Retreat Details**")
            f_ret_cost = st.number_input("Cost per Retreat ($)", value=7000, min_value=0, key="f_ret_cost")
            f_ret_year = st.number_input("Retreats / Year", value=4, min_value=0, key="f_ret_year")
            f_ret_part = st.number_input("Participants / Retreat", value=20, min_value=1, key="f_ret_part")
            f_ret_price = st.number_input("Price per Participant ($)", value=500, min_value=0, key="f_ret_price")
        with f3:
            st.markdown("**Expenses & Growth**")
            f_rent = st.number_input("Monthly Rent ($)", value=1200, min_value=0, key="f_rent")
            f_sw = st.number_input("Monthly Software ($)", value=150, min_value=0, key="f_sw")
            f_other = st.number_input("Monthly Other ($)", value=300, min_value=0, key="f_other")
            f_growth = st.slider("Annual Growth Rate (%)", 0, 50, 10, key="f_growth")

    # Calculations
    yr1_ind = f_ind_rate * f_ind_sess * 12
    yr1_corp = f_corp_rate * f_corp_sess * 12
    yr1_retreat_rev = f_ret_part * f_ret_price * f_ret_year
    yr1_retreat_cost = f_ret_cost * f_ret_year
    yr1_expenses = (f_rent + f_sw + f_other) * 12

    # Build 5-year projection
    years = ["Year 1", "Year 2", "Year 3", "Year 4", "Year 5"]
    growth = 1 + f_growth / 100

    records = []
    for i in range(5):
        g = growth ** i
        ind_rev = yr1_ind * g
        corp_rev = yr1_corp * g
        ret_rev = yr1_retreat_rev * g
        ret_cost = yr1_retreat_cost * g
        expenses = yr1_expenses * g
        total_rev = ind_rev + corp_rev + ret_rev
        total_cost = ret_cost + expenses
        profit = total_rev - total_cost
        margin = (profit / total_rev * 100) if total_rev > 0 else 0
        records.append({
            "Year": years[i],
            "Individual Revenue ($)": ind_rev,
            "Corporate Revenue ($)": corp_rev,
            "Retreat Revenue ($)": ret_rev,
            "Total Revenue ($)": total_rev,
            "Retreat Costs ($)": ret_cost,
            "Operating Expenses ($)": expenses,
            "Total Costs ($)": total_cost,
            "Net Profit ($)": profit,
            "Profit Margin (%)": margin,
        })

    df_pnl = pd.DataFrame(records)

    st.subheader("📋 5-Year Profit & Loss Projection")
    st.dataframe(
        df_pnl.style.format({
            "Individual Revenue ($)": "${:,.0f}",
            "Corporate Revenue ($)": "${:,.0f}",
            "Retreat Revenue ($)": "${:,.0f}",
            "Total Revenue ($)": "${:,.0f}",
            "Retreat Costs ($)": "${:,.0f}",
            "Operating Expenses ($)": "${:,.0f}",
            "Total Costs ($)": "${:,.0f}",
            "Net Profit ($)": "${:,.0f}",
            "Profit Margin (%)": "{:.1f}%",
        }),
        use_container_width=True, hide_index=True,
    )

    st.divider()

    c1, c2 = st.columns(2)

    with c1:
        fig_5yr = go.Figure()
        fig_5yr.add_trace(go.Bar(name="Revenue", x=years, y=df_pnl["Total Revenue ($)"],
                                  marker_color="#4A6741"))
        fig_5yr.add_trace(go.Bar(name="Costs", x=years, y=df_pnl["Total Costs ($)"],
                                  marker_color="#D94F4F"))
        fig_5yr.add_trace(go.Scatter(name="Net Profit", x=years, y=df_pnl["Net Profit ($)"],
                                      line=dict(color="#2E86C1", width=3)))
        fig_5yr.update_layout(title="5-Year Financial Outlook", barmode="group",
                               template="plotly_white", height=450, yaxis_title="Amount ($)")
        st.plotly_chart(fig_5yr, use_container_width=True)

    with c2:
        fig_margin = px.line(
            df_pnl, x="Year", y="Profit Margin (%)",
            title="Profit Margin Trend", markers=True,
        )
        fig_margin.update_traces(line=dict(color="#4A6741", width=3), marker=dict(size=10))
        fig_margin.update_layout(template="plotly_white", height=450)
        st.plotly_chart(fig_margin, use_container_width=True)

    # Summary Box
    st.divider()
    st.subheader("📝 Year 1 Summary")
    s1, s2, s3, s4 = st.columns(4)
    yr1 = records[0]
    s1.metric("Total Revenue", f"${yr1['Total Revenue ($)']:,.0f}")
    s2.metric("Total Costs", f"${yr1['Total Costs ($)']:,.0f}")
    s3.metric("Net Profit", f"${yr1['Net Profit ($)']:,.0f}")
    s4.metric("Profit Margin", f"{yr1['Profit Margin (%)']:.1f}%")

    # CSV Download
    csv = df_pnl.to_csv(index=False)
    st.download_button("📥 Download P&L as CSV", csv, "profit_and_loss.csv", "text/csv")




# ═══════════════════════════════════════════════
# 🧭 BUSINESS PLAN
# ═══════════════════════════════════════════════
elif page == "🧭 Business Plan":
    st.header("🧭 Business Plan")
    st.markdown("A structured, editable business plan for your coaching + meditation + retreats brand.")
    st.divider()

    # Prefill from Elovate.co (editable)
    default_mission = (
        "Through psycho-spiritual coaching, meditation, and energy healing, support people to transform grief, "
        "life transitions, and deeper patterns into sustainable growth and inner clarity."
    )
    default_positioning = (
        "Psycho-spiritual coaching + meditation guidance rooted in psychology, spirituality, and trauma-informed practices."
    )

    offerings_seed = [
        {"Offering": "Psycho-spiritual Coaching", "Format": "1:1", "Price": 180, "Notes": "Deep integrative space for healing, insight, inner transformation"},
        {"Offering": "Healing Meditations", "Format": "1:1", "Price": 120, "Notes": "Guided meditation + chakra healing/balancing + grounding"},
        {"Offering": "Relationship Coaching", "Format": "1:1", "Price": 180, "Notes": "Awareness, emotional clarity, boundaries, attachment & patterns"},
        {"Offering": "Workshops / Events", "Format": "Group", "Price": 55, "Notes": "Example: workshop investment"},
        {"Offering": "Workplace Wellness", "Format": "B2B", "Price": 0, "Notes": "Custom pricing; culture, burnout, wellbeing programs"},
        {"Offering": "Retreats", "Format": "Group", "Price": 500, "Notes": "Model pricing/margins in Retreat Planner"},
    ]

    t1, t2, t3, t4 = st.tabs(["🧬 Brand", "🧾 Offerings & Pricing", "📣 Marketing & Funnel", "🎯 Goals & KPIs"])

    with t1:
        st.subheader("🧬 Brand & Positioning")
        st.text_input("Brand Name", value="Elovate")
        st.text_area("Mission / Purpose", value=default_mission, height=120)
        st.text_area("Positioning Statement", value=default_positioning, height=100)

        st.markdown("**Business pillars (edit):**")
        p1, p2, p3 = st.columns(3)
        with p1:
            st.checkbox("Coaching", value=True)
        with p2:
            st.checkbox("Consulting", value=True)
        with p3:
            st.checkbox("Community", value=True)

        st.divider()
        st.subheader("👥 Ideal Client Segments")
        s1, s2 = st.columns(2)
        with s1:
            st.checkbox("Life transitions / grief / burnout", value=True)
            st.checkbox("Psycho-spiritual growth + integration", value=True)
            st.checkbox("Relationships / boundaries / attachment patterns", value=True)
        with s2:
            st.checkbox("Corporate/startups for wellness workshops", value=True)
            st.checkbox("Community events (dinners, rituals)", value=True)
            st.checkbox("Retreat participants", value=True)

        st.divider()
        st.subheader("✨ Value Proposition")
        st.markdown(
            "- Psychology + spirituality blended into practical tools
"
            "- Trauma-informed, embodied practices (somatic attunement, meditation)
"
            "- Clear containers: 1:1 coaching, healing sessions, groups, and retreats"
        )

    with t2:
        st.subheader("🧾 Offerings, Pricing & Revenue Assumptions")
        df_off = pd.DataFrame(offerings_seed)
        df_off = st.data_editor(
            df_off,
            use_container_width=True,
            hide_index=True,
            num_rows="dynamic",
            column_config={
                "Price": st.column_config.NumberColumn("Price ($)", min_value=0, step=5),
            },
        )

        st.divider()
        st.subheader("📦 Monthly Volume Assumptions")
        c1, c2, c3 = st.columns(3)
        with c1:
            m_psy = st.number_input("Psycho-spiritual Coaching sessions / month", value=12, min_value=0, step=1)
            m_med = st.number_input("Healing Meditation sessions / month", value=10, min_value=0, step=1)
        with c2:
            m_rel = st.number_input("Relationship Coaching sessions / month", value=8, min_value=0, step=1)
            m_workshop_att = st.number_input("Workshop attendees / month", value=20, min_value=0, step=1)
        with c3:
            workshop_price = st.number_input("Avg workshop ticket ($)", value=55, min_value=0, step=5)
            b2b_monthly = st.number_input("B2B revenue / month ($)", value=0, min_value=0, step=100)

        def price_of(contains, fallback):
            try:
                row = df_off[df_off["Offering"].str.contains(contains, case=False, na=False)].iloc[0]
                v = row.get("Price", fallback)
                return float(v) if pd.notna(v) else float(fallback)
            except Exception:
                return float(fallback)

        monthly_rev = (
            m_psy * price_of("Psycho", 180)
            + m_med * price_of("Medit", 120)
            + m_rel * price_of("Relationship", 180)
            + m_workshop_att * workshop_price
            + b2b_monthly
        )
        st.metric("Estimated Monthly Revenue", f"${monthly_rev:,.0f}")
        st.caption("Note: Retreat revenue/costs are modeled in the Retreat Planner tab.")

    with t3:
        st.subheader("📣 Marketing Channels & Funnel")
        left, right = st.columns(2)
        with left:
            st.markdown("**Channels to track**")
            st.multiselect(
                "",
                ["Website", "SEO", "Instagram", "YouTube", "Podcast", "Email Newsletter", "Partnerships", "Workshops", "Referrals"],
                default=["Website", "Instagram", "Partnerships", "Referrals"],
                label_visibility="collapsed",
            )
            st.text_area(
                "Core Content Themes",
                value="Rest / nervous system · relationships · grief & transitions · psycho-spiritual integration",
                height=100,
            )
        with right:
            st.markdown("**Monthly funnel metrics**")
            leads = st.number_input("Leads", value=40, min_value=0, step=5)
            discovery = st.number_input("Discovery calls", value=12, min_value=0, step=1)
            new_clients = st.number_input("New clients", value=6, min_value=0, step=1)
            conv = (new_clients / discovery * 100) if discovery else 0
            st.metric("Discovery → Client Conversion", f"{conv:.1f}%")

        st.divider()
        st.subheader("🧩 Lead-to-Revenue")
        avg_value = st.number_input("Avg monthly value per new client ($)", value=360, min_value=0, step=10)
        st.metric("Projected New Monthly Recurring Revenue", f"${(new_clients*avg_value):,.0f}")

    with t4:
        st.subheader("🎯 Goals & KPIs")
        g1, g2, g3 = st.columns(3)
        with g1:
            target_rev = st.number_input("Target Monthly Revenue ($)", value=8000, min_value=0, step=250)
        with g2:
            st.slider("Target Profit Margin (%)", 0, 80, 40)
        with g3:
            fixed_costs = st.number_input("Fixed Monthly Costs ($)", value=1200, min_value=0, step=50)

        profit = monthly_rev - fixed_costs
        margin = (profit / monthly_rev * 100) if monthly_rev else 0
        k1, k2, k3 = st.columns(3)
        k1.metric("Estimated Monthly Profit", f"${profit:,.0f}")
        k2.metric("Estimated Margin", f"{margin:.1f}%")
        k3.metric("Gap to Revenue Target", f"${(target_rev - monthly_rev):,.0f}")

        st.divider()
        st.subheader("✅ 30-60-90 Day Action Plan")
        plan = pd.DataFrame([
            {"Horizon": "30 Days", "Focus": "Clarify offers + packages", "Action": "Finalize 2-3 signature containers + pricing", "Owner": "You", "Status": "Planned"},
            {"Horizon": "60 Days", "Focus": "Content + partnerships", "Action": "Publish weekly content + 2 partner collabs", "Owner": "You", "Status": "Planned"},
            {"Horizon": "90 Days", "Focus": "Events + scalable offer", "Action": "Run 1 workshop + plan 1 retreat/mini-immersion", "Owner": "You", "Status": "Planned"},
        ])
        st.data_editor(plan, use_container_width=True, hide_index=True, num_rows="dynamic")

# ─── Footer ───
st.divider()
st.markdown(
    "<p style='text-align:center; color:#aaa; font-size:0.85rem;'>"
    "🧘 Mindful Business Dashboard · Built with ❤️ using Streamlit"
    "</p>",
    unsafe_allow_html=True,
)
