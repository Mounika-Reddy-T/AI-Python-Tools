import streamlit as st
import requests
import pandas as pd
from datetime import datetime

# Configuration
API_URL = "http://localhost:8000/evaluate"

# Page setup
st.set_page_config(page_title="AI Prompt Evaluation Tool", page_icon="🤖")
st.title("🤖 AI Prompt Evaluation Tool")
st.write("Test AI responses and get automatic evaluation scores")

# Input section
question = st.text_input("Enter your question:", placeholder="What is the capital of France?")

# Evaluation button
if st.button("🚀 Generate & Evaluate", type="primary"):
    if not question.strip():
        st.error("Please enter a question")
    else:
        with st.spinner("Processing..."):
            try:
                response = requests.post(API_URL, json={"question": question})
                
                if response.status_code == 200:
                    data = response.json()
                    
                    # Display results
                    st.success("✅ Evaluation Complete!")
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric("Score", f"{data['score']}/1")
                    with col2:
                        st.metric("Evaluation", data['evaluation'])
                    
                    st.subheader("Results")
                    st.write(f"**Question:** {data['question']}")
                    st.write(f"**Answer:** {data['answer']}")
                    
                    # Save to CSV
                    df = pd.DataFrame([{
                        "Question": data["question"],
                        "Answer": data["answer"],
                        "Evaluation": data["evaluation"],
                        "Score": data["score"]
                    }])
                    
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = f"evaluation_{timestamp}.csv"
                    df.to_csv(filename, index=False)
                    
                    st.info(f"💾 Results saved to {filename}")
                    
                    # Download button
                    csv = df.to_csv(index=False)
                    st.download_button(
                        "📥 Download CSV",
                        csv,
                        filename,
                        "text/csv",
                        key="download-csv"
                    )
                    
                else:
                    st.error(f"❌ API Error: {response.status_code}")
                    st.error(response.text)
                    
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

# Footer
st.markdown("---")
st.markdown("*Powered by OpenRouter API*")