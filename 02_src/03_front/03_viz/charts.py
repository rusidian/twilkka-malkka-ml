import plotly.graph_objects as go

_CHART_BG = "rgba(0,0,0,0)"
_GRID_COLOR = "#e5e7eb"
_TICK_COLOR = "#6b7280"


def make_trend_chart(monthly_trend: dict) -> go.Figure:
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=monthly_trend["months"],
            y=monthly_trend["이탈률"],
            mode="lines+markers",
            name="평균 예측 이탈률",
            line=dict(color="#8B5CF6", width=3),
            marker=dict(size=7, color="#8B5CF6"),
        )
    )

    fig.add_trace(
        go.Scatter(
            x=monthly_trend["months"],
            y=monthly_trend["활동도"],
            mode="lines+markers",
            name="평균 최근 시청 횟수",
            line=dict(color="#3B82F6", width=3),
            marker=dict(size=6, color="#3B82F6"),
            opacity=0.9,
            yaxis="y2",
        )
    )

    fig.update_layout(
        height=430,
        margin=dict(l=10, r=10, t=10, b=10),
        paper_bgcolor="white",
        plot_bgcolor="white",
        font=dict(color=_TICK_COLOR, family="Inter, sans-serif"),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.05,
            xanchor="left",
            x=0,
            font=dict(color="#374151"),
            bgcolor="rgba(0,0,0,0)",
        ),
        xaxis=dict(
            showgrid=False,
            tickfont=dict(color=_TICK_COLOR, size=12),
            showline=False,
        ),
        yaxis=dict(
            title=dict(
                text="예측 이탈률(%)",
                font=dict(color="#fc8181"),
            ),
            showgrid=True,
            gridcolor=_GRID_COLOR,
            zeroline=False,
            tickfont=dict(color=_TICK_COLOR, size=12),
        ),
        yaxis2=dict(
            title=dict(
                text="최근 시청 횟수",
                font=dict(color="#3B82F6"),
            ),
            overlaying="y",
            side="right",
            showgrid=False,
            zeroline=False,
            tickfont=dict(color="#6B7280"),
        ),
    )
    return fig


def make_risk_donut(risk_segments: dict) -> go.Figure:
    colors = ["#FF6A1A", "#F4B323", "#2DA2DB", "#8EDC63"]

    total = sum(risk_segments["values"])

    fig = go.Figure(
        data=[
            go.Pie(
                labels=risk_segments["labels"],
                values=risk_segments["values"],
                hole=0.65,
                marker=dict(colors=colors, line=dict(color="#ffffff", width=1.5)),
                textinfo="none",
                sort=False,
            )
        ]
    )

    fig.update_layout(
        height=230,
        margin=dict(l=10, r=10, t=10, b=10),
        paper_bgcolor="rgba(0,0,0,0)",
        showlegend=False,
        annotations=[
            dict(
                text=f"<b>{total:,}</b><br><span style='font-size:13px;color:#6b7280'>총 사용자</span>",
                x=0.5,
                y=0.5,
                font=dict(size=23, color="#111827", family="Inter, sans-serif"),
                showarrow=False,
            )
        ],
    )
    return fig


def make_genre_donut(items: list[dict]) -> go.Figure:
    labels = [g["label"] for g in items]
    values = [g["value"] for g in items]
    colors = ["#FF6A1A", "#F4B323", "#2DA2DB", "#8EDC63"]

    fig = go.Figure(
        data=[
            go.Pie(
                labels=labels,
                values=values,
                hole=0.65,
                marker=dict(colors=colors, line=dict(color="#ffffff", width=1.5)),
                textinfo="none",
                sort=False,
            )
        ]
    )

    fig.update_layout(
        height=230,
        margin=dict(l=10, r=10, t=10, b=10),
        paper_bgcolor=_CHART_BG,
        plot_bgcolor=_CHART_BG,
        showlegend=False,
    )
    return fig