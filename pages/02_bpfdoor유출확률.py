import streamlit as st

st.title("🔐 SKT 해킹 사고 내 정보 유출 가능성 계산기")

# 사용자 입력 받기
total_servers = st.number_input("총 SKT 서버 수", min_value=1, value=100, step=1)
hacked_servers = st.number_input("해킹당한 서버 수", min_value=0, max_value=total_servers, value=23, step=1)
my_data_servers = st.number_input("내 정보가 저장된 서버 수", min_value=0, max_value=total_servers, value=5, step=1)
extraction_rate = st.slider("해킹된 서버에서 내 정보 추출 확률 (%)", min_value=0, max_value=100, value=80)

# 확률 계산
if total_servers > 0 and 0 <= hacked_servers <= total_servers and 0 <= my_data_servers <= total_servers:
    # 1) 해킹당한 서버 중 내 정보가 저장된 서버 비율
    if hacked_servers == 0:
        st.write("해킹당한 서버가 없습니다. 내 정보 유출 확률은 0%입니다.")
    else:
        prob_my_info_in_hacked_servers = my_data_servers / hacked_servers

        # 2) 내 정보가 저장된 서버가 해킹당할 확률
        prob_server_hacked = hacked_servers / total_servers

        # 3) 해킹된 서버에서 내 정보가 실제 추출될 확률
        prob_extraction = extraction_rate / 100

        # 최종 내 정보 유출 확률
        final_prob = prob_server_hacked * prob_my_info_in_hacked_servers * prob_extraction

        # 확률이 1 초과 방지
        final_prob = min(final_prob, 1.0)

        st.write(f"💡 내 정보가 해킹 데이터에 포함될 확률은 약 **{final_prob*100:.2f}%** 입니다.")

else:
    st.error("입력값을 확인해 주세요.")
