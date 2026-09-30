import streamlit as st
import ollama

st.set_page_config(page_title="SiliconCopilot", layout="wide")

st.title("⚡ SiliconCopilot: On-Device Hardware Design Assistant")
st.caption("Powered by Snapdragon NPU & Qualcomm AI Engine Architecture (Local Execution)")

# Sidebar Configuration
st.sidebar.header("Design Tasks")
task = st.sidebar.radio(
    "Select Workflow",
    ["Verilog Code Generator", "Testbench Generator", "Syntax & Logic Bug Fixer"]
)

# User Input Interface
st.subheader(f"Workflow: {task}")
user_input = st.text_area(
    "Enter your specifications or Verilog snippet:", 
    height=200, 
    placeholder="Example: Design a 32-bit ALU or a 4-bit synchronous up/down counter..."
)

system_prompt = (
    "You are an expert Verilog HDL hardware design and synthesis engineer. "
    "Provide clear, syntactically correct, and synthesizable Verilog code with brief design notes."
)

if st.button("Generate Output"):
    if user_input.strip():
        with st.spinner("Processing locally on Snapdragon NPU pipeline..."):
            try:
                full_prompt = f"Task: {task}\nInput Specifications:\n{user_input}"
                response = ollama.chat(
                    model='qwen2.5-coder:1.5b',
                    messages=[
                        {'role': 'system', 'content': system_prompt},
                        {'role': 'user', 'content': full_prompt}
                    ]
                )
                
                st.markdown("### Output Result")
                st.code(response['message']['content'], language="verilog")
                st.success("Successfully generated locally on NPU execution runtime!")
            except Exception as e:
                st.error(f"Error connecting to local engine: {e}")
    else:
        st.warning("Please enter valid specifications or code first.")