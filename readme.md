# Webpage Question Answering Tool

## Description
This tool allows users to extract answers to questions from the content of specified webpages. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for testing purposes.

### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.10+
- pip (Python package installer)

### Installation

1. **Clone the Repository**

    Start by cloning the repository to your local machine:

    ```bash
    git clone https://github.com/your-username/website_qa.git
    cd your-repository-name
    ```

2. **Install Required Libraries**

    Install all dependencies listed in the `requirements.txt` file using pip:

    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up Environment Variables**

    You need to set up the OpenAI API key as an environment variable. Replace `your_openai_api_key_here` with your actual API key.

    - Open the env file:
      ```
      OPENAI_API_KEY="<your_openai_api_key_here>"
      ```


### Usage

There are two ways to use this tool: through API calls or using a built-in UI.

#### A. API Calls

1. **Run the Application**

    Start the Flask server by running:

    ```bash
    python app.py
    ```

2. **Making API Calls**

    - **Windows using PowerShell**:
      ```powershell

      $response = Invoke-RestMethod -Uri "http://127.0.0.1:5000/answer" -Method Post -ContentType "application/json" -Body ( @{ url="https://example.com"; question="What is Gen AI?" } | ConvertTo-Json )

      $response

      OR (Breakdown of steps)

      $body = @{
          url = "https://example.com"
          question = "What is Gen AI?"
      }

      $jsonBody = $body | ConvertTo-Json

      $response = Invoke-RestMethod -Uri "http://127.0.0.1:5000/answer" -Method Post -ContentType "application/json" -Body $jsonBody

      $response
      ```

    - **macOS and Linux using cURL**:
      ```bash
      curl -X POST http://127.0.0.1:5000/answer -H "Content-Type: application/json" -d '{"url":"https://example.com", "question":"What is the main topic?"}'
      ```

#### B. Using the UI

1. **Run the UI**

    If you have a UI setup with Streamlit or similar, start it by running:

    ```bash
    streamlit run ui.py
    ```

2. **Interactive Interface**

    Open your web browser and navigate to `http://localhost:8501` (or whichever port Streamlit uses). Enter the URL and click on "Process URL
    and enter your question in the provided field and click on "Ask Question" to get answers.


