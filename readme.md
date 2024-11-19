## Book Cutter

In order to use [NotebookLLM](https://notebooklm.google/) for a better experience (means passing sections rather than the total book to LLM for a better podcast), this project cuts the PDF by sections.

### Features

- Cuts PDF files into sections for better processing with LLM.
- You can run this cutter locally with only 1b model supported by ollama.


### Installation

1. Install the ollama
> refer to [https://ollama.com/](https://ollama.com/)

2. Install other dependencies:

```bash
pip install -r requirements.txt
```

### Usage

1. launch the ollama and llama 3.2 1b model by:

```shell
ollama run llama3.2:1b
```

2. follow the step-by-step instructions in 
`preprocess.ipynb`
