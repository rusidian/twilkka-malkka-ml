from pathlib import Path
import sys

import streamlit as st


PROJECT_ROOT = Path(__file__).resolve().parent
FRONT_ROOT = PROJECT_ROOT / "02_src" / "03_front"
DATA_PREPROCESS_ROOT = PROJECT_ROOT / "02_src" / "01_data" / "01_preprocessing"

PATHS_TO_ADD = [
    FRONT_ROOT / "00_ui",
    FRONT_ROOT / "01_views",
    FRONT_ROOT / "02_state",
    FRONT_ROOT / "03_viz",
    FRONT_ROOT / "04_services",
    DATA_PREPROCESS_ROOT,
]

for path in PATHS_TO_ADD:
    path_str = str(path)
    if path_str not in sys.path:
        sys.path.insert(0, path_str)

from state import init_state
from dashboard_view import render_dashboard_view
from home_view import render_home_view
from styles import inject_css


def main() -> None:
    st.set_page_config(
        page_title="Netflix 고객 이탈 예측 서비스",
        page_icon="🎬",
        layout="wide",
        initial_sidebar_state="collapsed",
    )

    inject_css()
    init_state()

    if st.session_state.current_view == "home":
        render_home_view()
    else:
        render_dashboard_view()


if __name__ == "__main__":
    main()