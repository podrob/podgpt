# PodGPT


This experimental project aims to create a localized chatbot. The bot is designed to answer questions from a stored collection of files in PDF, TXT, DOC, and DOCX formats. 

The project utilizes FAISS for similarity search and Falcon7b LLM for language modeling from [Hugging Face](https://huggingface.co/). Code is written in Python, using the [Langchain](https://python.langchain.com/docs/get_started/introduction) framework. [Poetry](https://python-poetry.org/) for dependancy management and [Streamlit](https://streamlit.io/) for it's UI.


## Environment variables
In order to run the chatbot, you need a valid API key for [Hugging Face](https://huggingface.co/). To generate one, sign-in to Hugging Face, or create an account if you don't already have one. Navigate to your profile 'Access Tokens' and generate a new token with 'read' access.

Create a new file `./podgpt/.env` and paste in your API token here. There is an `.env.example` file there already for you to use as a template.


## Run via Docker

```bash
# copy code locally
git clone https://github.com/podrob/podgpt
cd podgpt
``````

```bash
# build image
docker build -t podgpt .
```

```bash
# run container via docker-compose
docker-compose up
```


## Running locally

### Prerequisites
Before getting started, ensure that you have the following installed on your system:

**Python 3.x**: You can install it on macOS using Homebrew. Open Terminal and run:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

brew install python
```

**Poetry**: To install Poetry, run the following command in your terminal:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Installation
Clone the repository:

```bash
git clone https://github.com/podrob/podgpt
cd podgpt
``````

Install dependencies using Poetry:

```bash
poetry install
```
This will create a virtual environment and install all the required packages.


### Running the Project
To run the project locally, follow these steps:

Activate the virtual environment created by Poetry:

```bash
poetry shell
```

Run the Streamline server:

```bash
streamlit run podgpt/Home.py
```

Access the chatbot at http://localhost:8501 in your web browser.

#### Additional Notes
The project uses FAISS (Facebook AI Similarity Search))for efficient similarity search via embeddings. 

Falcon7b LLM is used for language modeling. The project has the capacity to inject in alternative LLMs via the use of an abc Abstract Base Class in `podgpt/components/llm.py`

#### Contributors
Rob McBryde (@podrob)

#### License
This project is licensed under the MIT License - see the LICENSE.md file for details.