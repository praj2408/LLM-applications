import streamlit as st
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain.agents.agent_types import AgentType

from dotenv import load_dotenv
import os
from langchain_openai import OpenAI


def main():
    
    load_dotenv()
    st.title("Ask your CSV")
    
    user_csv = st.file_uploader("Upload your csv file", type="csv")
    
    if user_csv is not None:
        user_question = st.text_input("Ask a question about your csv: ")
        
        llm = OpenAI(temperature=0 )
        agent = create_csv_agent(llm, user_csv, verbose=True, agent_type=AgentType.OPENAI_FUNCTIONS)
        
        
        if user_question is not None and user_question != "":
            response = agent.run(user_question)
            st.write(response)
            
            

    
    
    
if __name__=="__main__":
    main()