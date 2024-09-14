import streamlit as st

def main():
    st.title("クラウド関連ニュースまとめ")

    # AWS の最新情報
    site_title = "AWS の最新情報"
    site_url = "https://aws.amazon.com/jp/new/?whats-new-content-all.sort-by=item.additionalFields.postDateTime&whats-new-content-all.sort-order=desc&awsf.whats-new-categories=*all"

    st.header(site_title)
    st.write(f"URL: [{site_url}]({site_url})")

    # 黒線で区切る
    st.markdown("---")

    # Classmethod 開発ブログ
    classmethod_title = "クラスメソッド DevelopersIO"
    classmethod_url = "https://dev.classmethod.jp/"

    st.header(classmethod_title)
    st.write(f"URL: [{classmethod_url}]({classmethod_url})")

    # 黒線で区切る
    st.markdown("---")

if __name__ == "__main__":
    main()