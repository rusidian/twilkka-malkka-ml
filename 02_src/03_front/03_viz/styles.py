import streamlit as st


def inject_css() -> None:
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

        :root {
            --bg: #f0f2f5;
            --text: #111827;
            --muted: #6b7280;
            --red: #e50914;
        }

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        .stApp {
            background: #f0f2f5;
            color: var(--text);
        }

        .block-container {
            max-width: 1420px;
            padding-top: 4.8rem !important;
            padding-bottom: 2rem;
        }

        .top-navbar {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 9999;
            background: #111827;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 28px;
            height: 52px;
            border-bottom: 1px solid rgba(255,255,255,0.07);
        }

        .navbar-left {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .navbar-logo {
            color: #E50914;
            font-size: 1.4rem;
            font-weight: 900;
        }

        .navbar-title {
            color: #fff;
            font-weight: 800;
            font-size: 0.97rem;
        }

        .navbar-right {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .navbar-btn-active {
            background: #E50914;
            color: white;
            padding: 6px 16px;
            border-radius: 8px;
            font-weight: 700;
            font-size: 0.88rem;
        }

        .navbar-btn {
            color: #d1d5db;
            padding: 6px 16px;
            border: 1px solid #374151;
            border-radius: 8px;
            font-weight: 700;
            font-size: 0.88rem;
        }

        .navbar-date {
            color: #9ca3af;
            font-size: 0.83rem;
            margin: 0 4px;
        }

        .navbar-avatar {
            background: #E50914;
            color: white;
            width: 32px;
            height: 32px;
            border-radius: 50%;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            font-weight: 900;
            font-size: 0.78rem;
        }

        .card-box {
            background: #ffffff;
            border: 1px solid #e5e7eb;
            border-radius: 18px;
            padding: 22px 22px 18px 22px;
            box-shadow: 0 2px 12px rgba(0,0,0,0.06);
            height: 100%;
        }

        .st-key-card-trend,
        .st-key-card-risk-donut {
            background: #ffffff;
            border: 1px solid #e5e7eb;
            border-radius: 18px;
            padding: 22px;
            box-shadow: 0 2px 12px rgba(0,0,0,0.06);
            min-height: 450px;
        }

        .st-key-card-ott-usage,
        .st-key-card-genre-chart,
        .st-key-card-churn-drivers {
            background: #ffffff;
            border: 1px solid #e5e7eb;
            border-radius: 18px;
            padding: 22px;
            box-shadow: 0 2px 12px rgba(0,0,0,0.06);
            min-height: 580px;
        }

        .hero-wrap {
            background: linear-gradient(135deg,#141414 0%,#1f2937 100%);
            border: 1px solid rgba(229,9,20,0.25);
            border-radius: 18px;
            padding: 29px 27px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.12);
        }

        .hero-title {
            font-size: 1.6rem;
            font-weight: 900;
            color: white;
            margin-bottom: 4px;
        }

        .hero-header {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 6px;
        }

        .netflix-logo {
            height: 32px;
        }

        .hero-sub {
            color: #cbd5e1;
            font-size: 0.95rem;
            margin-bottom: 12px;
        }

        .hero-insight {
            color: #f8fafc;
            font-size: 0.9rem;
            background: rgba(255,255,255,0.06);
            border: 1px solid rgba(255,255,255,0.10);
            display: inline-block;
            padding: 7px 14px;
            border-radius: 999px;
            font-weight: 700;
        }

        .dashboard-summary-bar {
            padding: 11px 16px;
            border-radius: 12px;
            background: rgba(59,130,246,0.08);
            border: 1px solid rgba(59,130,246,0.20);
            color: #1d4ed8;
            font-size: 0.90rem;
            font-weight: 600;
            margin-bottom: 18px;
        }

        .kpi-card {
            background: #ffffff;
            border: 1px solid #e5e7eb;
            border-radius: 18px;
            padding: 24px 24px 22px 24px;
            min-height: 130px;
            box-shadow: 0 2px 12px rgba(0,0,0,0.06);
        }

        .kpi-top {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 10px;
        }

        .kpi-icon {
            width: 42px;
            height: 42px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: #fef2f2;
            font-size: 1.15rem;
        }

        .kpi-label {
            color: #6b7280;
            font-size: 0.92rem;
            margin-bottom: 6px;
            font-weight: 600;
        }

        .kpi-value {
            color: #111827;
            font-size: 2rem;
            font-weight: 900;
            line-height: 1.0;
        }

        .kpi-subtext {
            color: #6b7280;
            font-size: 0.88rem;
            margin-top: 10px;
            font-weight: 500;
        }

        .section-heading-wrap {
            margin-bottom: 16px;
        }

        .section-title {
            font-size: 1.2rem;
            font-weight: 800;
            color: #111827;
            margin-bottom: 3px;
        }

        .section-sub {
            color: #6e6f73;
            font-size: 0.9rem;
        }

        .metric-row {
            margin-bottom: 18px;
        }

        .metric-row-top {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 6px;
            font-size: 0.92rem;
        }

        .metric-label {
            color: #374151;
            font-weight: 600;
            font-size: 1.05rem;
        }

        .metric-value {
            color: #111827;
            font-weight: 800;
            font-size: 1.05rem;
        }

        .metric-desc {
            color: #6b7280;
            font-size: 0.95rem;
        }

        .bar-track {
            width: 100%;
            height: 10px;
            border-radius: 999px;
            background: #f1f5f9;
            overflow: hidden;
        }

        .bar-fill-blue {
            height: 100%;
            border-radius: 999px;
            background: linear-gradient(90deg,#3b82f6,#60a5fa);
        }

        .bar-fill-red {
            height: 100%;
            border-radius: 999px;
            background: linear-gradient(90deg,#ef4444,#f87171);
        }

        .legend-item {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 10px;
        }

        .legend-left {
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .legend-right {
            display: flex;
            align-items: center;
            gap: 10px;
            min-width: 80px;
            justify-content: flex-end;
        }

        .legend-dot {
            width: 11px;
            height: 11px;
            border-radius: 50%;
            flex-shrink: 0;
        }

        .legend-label {
            color: #374151;
            font-weight: 600;
            font-size: 0.92rem;
        }

        .legend-value {
            color: #111827;
            font-weight: 800;
            font-size: 0.92rem;
        }

        .legend-pct {
            color: #9ca3af;
            font-weight: 600;
            font-size: 0.85rem;
            min-width: 36px;
            text-align: right;
        }

        .alert-box {
            margin-top: 16px;
            background: #fffbeb;
            border: 1px solid #fcd34d;
            color: #92400e;
            border-radius: 12px;
            padding: 10px 14px;
            font-size: 0.88rem;
            font-weight: 600;
        }

        .user-card {
            background: #ffffff;
            border: 1px solid #e5e7eb;
            border-radius: 16px;
            padding: 16px 18px;
            margin-bottom: 12px;
            box-shadow: 0 1px 6px rgba(0,0,0,0.04);
        }

        .user-head {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            gap: 12px;
            margin-bottom: 12px;
            flex-wrap: wrap;
        }

        .user-head-left {
            display: flex;
            flex-direction: column;
            gap: 4px;
        }

        .user-name {
            color: #111827;
            font-size: 1.02rem;
            font-weight: 800;
        }

        .user-subline {
            color: #9ca3af;
            font-size: 0.85rem;
            font-weight: 500;
        }

        .user-pill {
            background: #fef2f2;
            color: #dc2626;
            border: 1px solid #fecaca;
            border-radius: 999px;
            padding: 5px 12px;
            font-size: 0.80rem;
            font-weight: 800;
            white-space: nowrap;
        }

        .campaign-chip-wrap {
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
            margin-bottom: 14px;
        }

        .campaign-chip {
            display: inline-flex;
            align-items: center;
            padding: 6px 10px;
            border-radius: 999px;
            background: #fff7ed;
            color: #c2410c;
            border: 1px solid #fdba74;
            font-size: 0.78rem;
            font-weight: 700;
        }

        .secondary-chip {
            background: #eff6ff;
            color: #1d4ed8;
            border: 1px solid #93c5fd;
        }

        .user-grid {
            display: grid;
            grid-template-columns: repeat(4,minmax(0,1fr));
            gap: 10px;
        }

        .user-meta {
            background: #f9fafb;
            border-radius: 12px;
            padding: 10px 12px;
            border: 1px solid #f3f4f6;
        }

        .highlight-meta {
            background: #f0f9ff;
            border: 1px solid #bae6fd;
        }

        .user-meta-label {
            color: #9ca3af;
            font-size: 0.78rem;
            margin-bottom: 4px;
            font-weight: 500;
        }

        .user-meta-value {
            color: #111827;
            font-size: 0.95rem;
            font-weight: 800;
            word-break: break-word;
        }

        div[data-baseweb="select"] > div,
        .stFileUploader > div > div {
            background: #ffffff !important;
            border: 1px solid #e5e7eb !important;
            border-radius: 12px !important;
            color: #111827 !important;
        }

        .stMultiSelect [data-baseweb="tag"] {
            background: #e50914 !important;
            color: white !important;
            border-radius: 8px !important;
        }

        .stExpander {
            background: #ffffff;
            border: 1px solid #e5e7eb;
            border-radius: 14px;
            margin-bottom: 10px;
        }

        .stPlotlyChart {
            margin-bottom: 4px;
        }

        label,
        .stMarkdown p {
            color: var(--text);
        }

        div.stButton > button {
            background-color: #1f2937;
            color: white;
            border-radius: 10px;
            border: none;
            font-weight: 700;
            transition: 0.2s ease;
        }

        div.stButton > button:hover {
            background-color: #374151;
            color: white;
        }

        div.stButton > button:focus {
            outline: none;
            box-shadow: none;
            color: white;
        }

        div.stButton > button:disabled,
        div.stButton > button[disabled],
        div.stButton > button[kind="secondary"][disabled],
        div.stButton > button[kind="primary"][disabled] {
            background: #1f2937 !important;
            color: rgba(255, 255, 255, 0.78) !important;
            border: none !important;
            opacity: 1 !important;
            cursor: not-allowed !important;
        }

        div.stButton > button:disabled p,
        div.stButton > button[disabled] p,
        div.stButton > button:disabled span,
        div.stButton > button[disabled] span {
            color: rgba(255, 255, 255, 0.78) !important;
        }

        

        /* 업로더 라벨 + 내부 안내 문구 */
.stFileUploader label,
.stFileUploader label p,
.stFileUploader > label,
.stFileUploader > label p {
    color: #111827 !important;
    opacity: 1 !important;
}

.stFileUploader small,
.stFileUploader [data-testid="stFileUploaderDropzoneInstructions"],
.stFileUploader [data-testid="stFileUploaderDropzoneInstructions"] * {
    color: #f8fafc !important;
    opacity: 1 !important;
}
        /* Browse files 버튼만 따로 지정 */
        .stFileUploader button {
            background-color: #111827 !important;
            color: #ffffff !important;
            border: 1px solid #374151 !important;
            border-radius: 10px !important;
            font-weight: 700 !important;
            opacity: 1 !important;
        }
        .stFileUploader button:disabled {
    opacity: 1 !important;
}

        .stFileUploader button:hover {
            background-color: #1f2937 !important;
            color: #ffffff !important;
        }

        .stFileUploader button span,
        .stFileUploader button p,
        .stFileUploader button div {
            color: #ffffff !important;
        }

        .landing-wrap {
            text-align: center;
            padding: 28px 0 12px 0;
        }

        .landing-badge {
            display: inline-block;
            padding: 6px 12px;
            border-radius: 999px;
            background: rgba(229,9,20,0.08);
            border: 1px solid rgba(229,9,20,0.20);
            color: #dc2626;
            font-size: 0.82rem;
            font-weight: 800;
            margin-bottom: 16px;
        }

        .landing-title {
            font-size: 2rem;
            font-weight: 900;
            color: #111827;
            margin-bottom: 8px;
        }

        .landing-sub {
            color: #6b7280;
            font-size: 1rem;
            line-height: 1.6;
            max-width: 760px;
            margin: 0 auto;
        }

        .upload-card {
            margin: 0;
            padding: 24px;
            border-radius: 20px;
            background: #ffffff;
            border: 1px solid #e5e7eb;
            box-shadow: 0 4px 16px rgba(0,0,0,0.06);
            min-height: 160px;
        }

        .upload-card-title {
            color: #111827;
            font-size: 1.25rem;
            font-weight: 900;
            margin-bottom: 6px;
        }

        .upload-card-sub {
            color: #6b7280;
            font-size: 0.92rem;
            margin-bottom: 8px;
        }

        .upload-actions {
            margin-top: 14px;
        }

        @media (max-width: 900px) {
            .user-grid {
                grid-template-columns: 1fr 1fr;
            }
        }

        @media (max-width: 640px) {
            .user-grid {
                grid-template-columns: 1fr;
            }

            .hero-title,
            .landing-title {
                font-size: 1.35rem;
            }

            .top-navbar {
                padding: 0 14px;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )