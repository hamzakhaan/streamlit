import openai
import json
import requests
import streamlit as st

# API keys should be stored securely, not hard-coded in the script
openai.api_key = "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"
coinmarketcap_api_key = "85bc404f-6f5b-49fd-9c68-13f4ffa7ec63"

# Rest of the code remains the same...

# Define the CoinMarketCap API endpoint and query parameters
url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
querystring = {
    "start": "1",  # Start with the first cryptocurrency
    "limit": "10",  # Number of cryptocurrencies to fetch
    "convert": "USD"  # Convert prices to USD
}

# Define the request headers with the CoinMarketCap API key
headers = {
    "X-CMC_PRO_API_KEY": coinmarketcap_api_key
}

# Rest of the code remains the same...

if st.button('Analyze'):
    with st.spinner('Getting Cryptocurrency Prices...'):
        cryptoPrices = GetCryptocurrencyPrices()
        st.success('Done!')
    with st.spinner('Analyzing Cryptocurrency Prices...'):
        chatGPTPrompt = f"""You are an expert crypto trader with more than 10 years of experience, 
                    I will provide you with a list of cryptocurrency prices for the last 7 days
                    can you provide me with a technical analysis
                    of the cryptocurrency market based on these prices. here is what I want: 
                    Price Overview, 
                    Moving Averages, 
                    Relative Strength Index (RSI),
                    Moving Average Convergence Divergence (MACD),
                    Advice and Suggestion,
                    Do I buy or sell?
                    Please be as detailed as much as you can, and explain in a way any beginner can understand. and make sure to use headings
                    Here is the price list: {cryptoPrices}"""

        analysis = BasicGeneration(chatGPTPrompt)
        st.text_area("Analysis", analysis,
                     height=500)
        st.success('Done!')