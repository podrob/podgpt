import os

from dotenv import load_dotenv
from langchain.llms import HuggingFaceHub

from components.llm.llm import Llm

REPO_ID = "tiiuae/falcon-7b-instruct"
MAX_NEW_TOKENS = 200

class Falcon7BLlm(Llm):
    def __init__(self):
        # self.llm = HuggingFaceInference({
        #     model: REPO_ID,
        #     apiKey: os.environ.get("HUGGINGFACE_API_TOKEN")
        # })

        self.llm = HuggingFaceHub(
            repo_id=REPO_ID,
            huggingfacehub_api_token=os.environ.get("HUGGINGFACE_API_TOKEN"),
            model_kwargs={
                "temperature": 0.1,
                "max_new_tokens":MAX_NEW_TOKENS,
            },
        )

    def get(self):
        return self.llm