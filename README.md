
# Research Co-Pilot

## Purpose
The Research Co-Pilot is a multi-agent system designed to automate the process of mining, parsing, summarizing, synthesizing, and surveying research papers on a given topic. It leverages the MOYA framework and OpenAI LLMs to generate structured mini-surveys from arXiv or user-provided PDFs.

## Project Organization

```
research_copilot/
├── agents/
│   ├── pdf_miner_agent.py         # Downloads PDFs from arXiv
│   ├── pdf_parser_agent.py        # Extracts text from PDFs
│   ├── summarizer_agent.py        # Summarizes paper text using LLM
│   ├── synthesizer_agent.py       # Synthesizes cross-paper insights
│   ├── survey_writer_agent.py     # Generates the final mini-survey
│   └── __init__.py
├── memory/
│   ├── ephemeral_memory_setup.py  # EphemeralMemory configuration
│   └── __init__.py
├── orchestrator.py                # Orchestrates the multi-agent workflow
├── main.py                        # CLI entrypoint
├── requirements.txt               # Project dependencies
├── mini_survey.txt                # Output: generated mini-survey
└── README.md                      # Project documentation
```

## File Details

- **agents/pdf_miner_agent.py**: Mines and downloads PDFs from arXiv for a given topic.
- **agents/pdf_parser_agent.py**: Extracts text from PDF files using pdfplumber.
- **agents/summarizer_agent.py**: Uses OpenAI LLM to summarize each paper in a structured format.
- **agents/synthesizer_agent.py**: Synthesizes insights and research gaps across all summaries.
- **agents/survey_writer_agent.py**: Generates a concise mini-survey with inline citations.
- **memory/ephemeral_memory_setup.py**: Sets up shared memory for agent communication.
- **orchestrator.py**: Coordinates the workflow between all agents.
- **main.py**: Command-line interface for running the full pipeline.
- **requirements.txt**: Lists all required Python packages.
- **mini_survey.txt**: Output file containing the generated mini-survey.

## Installation

1. **Clone the repository** (if not already):
	```sh
	git clone <your-repo-url>
	cd research_copilot
	```

2. **Clone or download the MOYA framework**

	> **Note:** This project depends on the MOYA framework. Please clone or download the MOYA repository at the same directory level as this project (i.e., both `research_copilot` and `moya` should be in the same parent folder) before installing requirements.

	```sh
	git clone https://github.com/montycloud/moya.git
	# Ensure the folder structure is:
	# parent_folder/
	# ├── moya/
	# └── research_copilot/
	```

3. **(Recommended) Create and activate a virtual environment:**
	```sh
	python3 -m venv .venv
	source .venv/bin/activate
	```

4. **Install dependencies:**
	```sh
	pip install -r requirements.txt
	```

5. **Set your OpenAI API key:**
	```sh
	export OPENAI_API_KEY=your-api-key-here
	```

## CLI Usage

Run the CLI to generate a mini-survey from arXiv:

```sh
python main.py --topic "Artificial General Intelligence"
```

Or, to process your own PDFs:

```sh
python main.py --pdf-folder pdfs_downloaded/
```

**Options:**

- `--topic <topic>`: Research topic to mine papers for (downloads from arXiv)
- `--pdf-folder <folder>`: Folder containing PDF files to process
- `--output <file>`: Output file for the mini-survey (default: mini_survey.txt)
- `--openai-api-key <key>`: OpenAI API key (or set OPENAI_API_KEY env var)

The generated mini-survey will be saved to the specified output file.

## Example

```sh
python main.py --topic "Sustainable AI"
```

## License
See LICENSE file for details.
