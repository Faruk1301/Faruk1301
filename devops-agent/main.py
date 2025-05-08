import os
import requests
from crewai import Agent, Task, Crew
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Define an LLM wrapper using Groq API
class GroqLLM:
    def __init__(self, model="mixtral-8x7b-32768"):
        self.model = model

    def chat(self, prompt):
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "You are an expert Azure DevOps Engineer skilled in Terraform, GitHub Actions, and CI/CD."},
                {"role": "user", "content": prompt}
            ]
        }

        response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)
        return response.json()['choices'][0]['message']['content']

# Create Groq LLM instance
llm = GroqLLM()

# Define the DevOps Agent
devops_agent = Agent(
    role="Azure DevOps Engineer",
    goal="Help build and deploy DevOps projects using Terraform and CI/CD pipelines",
    backstory="You are an expert in Azure DevOps and Terraform.",
    allow_delegation=False,
    verbose=True,
    llm=llm
)

# Define the task
task = Task(
    description="Provision Azure infrastructure with Terraform, push to GitHub, and set up CI/CD pipeline.",
    expected_output="A complete CI/CD-enabled Terraform project pushed to GitHub.",
    agent=devops_agent
)

# Assemble the crew
crew = Crew(
    agents=[devops_agent],
    tasks=[task],
    verbose=True
)

# Run the agent and generate code
if __name__ == "__main__":
    prompt = """
    Create the following DevOps setup:
    1. A `main.tf` file to deploy an Azure App Service Plan and two Web Apps (dev and staging).
    2. An `azure-pipelines.yml` file with multi-stage CI/CD that builds and deploys a Flask `app.py`.
    3. A simple `app.py` that returns different text based on whether it's Dev or Staging.
    """

    print("🤖 Generating files using your DevOps AI agent...\n")
    output = llm.chat(prompt)

    # Save to output file
    with open("generated_output.txt", "w") as f:
        f.write(output)

    print("✅ Files generated! Check 'generated_output.txt'")


