mkdir -p ~/.streamlit/

echo "\
[server]
headless = true
enableCORS = false
port = $PORT
enableXsrfProtection = false
" > ~/.streamlit/config.toml
python -m nltk.downloader punkt_tab