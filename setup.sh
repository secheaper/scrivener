mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
[theme]\n\
primaryColor="\#f63366"\\n
backgroundColor="\#ffffff"\\n
secondaryBackgroundColor="\#f0f2f6"\\n
textColor="\#262730"\\n
font="\sans serif"\\n
" > ~/.streamlit/config.toml