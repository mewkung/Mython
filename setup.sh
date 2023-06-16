mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"634230038@webmail.npru.ac.th\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml