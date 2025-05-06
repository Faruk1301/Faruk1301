python
from crewai import Agent

devops_agent = Agent(
    role="DevOps Engineer",
    goal="Automate the deployment of a Python web app to Azure using Terraform and GitHub Actions",
    backstory="An expert in cloud infrastructure and CI/CD with deep Azure experience.",
    tools=[]  # Add shell, terraform, or file writer tools if needed
)

