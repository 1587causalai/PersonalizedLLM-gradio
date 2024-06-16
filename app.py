import gradio as gr
import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoModel

# clone the model from OpenXLab
base_path = './PersonalizedLLM'
os.system(f'git clone https://code.openxlab.org.cn/causalgpt/PersonalizedLLM.git {base_path}')
os.system(f'cd {base_path} && git lfs pull')

tokenizer = AutoTokenizer.from_pretrained(base_path, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(base_path, trust_remote_code=True, torch_dtype=torch.float16).cuda()


def chat(message, history):
    for response, history in model.stream_chat(tokenizer, message, history, max_length=2048, top_p=0.7, temperature=1):
        yield response


gr.ChatInterface(chat,
                 title="Personalized LLM Research Assistant",
                 description="""
                 一个定制化的问答机器人,专注于为学者提供个性化大语言模型领域的专业知识和有价值的参考资料。
                 """,
                 ).queue(1).launch()
