import streamlit as st
from langchain import PromptTemplate, LLMChain
from langchain.llms import HuggingFaceHub
import os

os.environ['API_KEY'] = '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'

def generate_response(input):
    
    falcon_llm = HuggingFaceHub(huggingfacehub_api_token=os.environ['API_KEY'],           
                                repo_id='tiiuae/falcon-7b-instruct',
                                model_kwargs={'temperature':0.5,'max_new_tokens':500})
    template = ''' {question}'''
    prompt = PromptTemplate(template=template,input_variable=['question'])
    falcon_chain =  LLMChain(prompt=prompt,llm=falcon_llm,verbose=True)
    op = falcon_chain.run(input)
    return op

## frontend ##

st.set_page_config(page_title="General ChatBot" )
st.write("Hey there 🙋‍♂️")
st.title("Let's have a great chat together !")
text_input = st.text_area("Feel free to ask me anything!",height=50)
st.write("")
result=[]
with st.form("ask me anything",clear_on_submit=False):
    submitted = st.form_submit_button(label="Submit")
    if submitted:
        with st.spinner("Using My Intelligence"):
            response = generate_response(text_input)
            result.append(response)
if len(result):
    st.info(response)




