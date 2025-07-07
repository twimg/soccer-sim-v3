import streamlit as st
import pandas as pd
import random

# タイトル
st.set_page_config(page_title="サッカークラブ運営 v3", layout="wide")
st.title("⚽ サッカークラブ運営シミュレーション v3")

# チーム初期データ
players = [
    {"名前": "木村 隼人", "ポジション": "DF", "年齢": 27, "国籍": "日本", "能力": 66, "年俸": 1200},
    {"名前": "白石 翼", "ポジション": "MF", "年齢": 23, "国籍": "日本", "能力": 70, "年俸": 1800},
    {"名前": "アントン・ペレス", "ポジション": "FW", "年齢": 25, "国籍": "スペイン", "能力": 74, "年俸": 3000},
    {"名前": "チャン・ギュソン", "ポジション": "MF", "年齢": 22, "国籍": "韓国", "能力": 68, "年俸": 1000},
    {"名前": "ロドリゴ・セウバ", "ポジション": "DF", "年齢": 29, "国籍": "ブラジル", "能力": 72, "年俸": 2500},
    {"名前": "佐藤 一樹", "ポジション": "GK", "年齢": 24, "国籍": "日本", "能力": 65, "年俸": 1500},
]

df = pd.DataFrame(players)

# サイドバー：戦術選択
st.sidebar.header("📋 戦術選択")
tactic = st.sidebar.selectbox("戦術タイプを選んでください", ["攻撃的", "バランス", "守備的"])

# 戦術補正
tactic_bonus = {"攻撃的": 5, "バランス": 3, "守備的": 1}

# 戦力計算
team_power = df["能力"].mean() + tactic_bonus[tactic]

# 年俸表示
total_salary = df["年俸"].sum()

# メイン表示
st.subheader("📊 選手一覧")
st.dataframe(df, use_container_width=True)

st.markdown("---")

# 試合シミュレーション
st.subheader("🆚 試合シミュレーション")

if st.button("試合開始！"):
    opponent_power = random.randint(60, 80)
    result = "引き分け"
    score = "1 - 1"

    if team_power > opponent_power + 3:
        result = "勝利！"
        score = "2 - 0"
    elif team_power < opponent_power - 3:
        result = "敗北..."
        score = "0 - 2"

    st.write(f"戦術: **{tactic}**（補正 +{tactic_bonus[tactic]}）")
    st.write(f"自チーム戦力: **{round(team_power,1)}**")
    st.write(f"相手戦力: **{opponent_power}**")
    st.success(f"試合結果：**{result}**　スコア：**{score}**")

st.markdown("---")
st.info(f"💰 総年俸: {total_salary} 万円")
