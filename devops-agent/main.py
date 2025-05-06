```python
from crewai import Task

deploy_task = Task(
description="Provision Azure resources with Terraform, push code to GitHub, and trigger CI/CD pipeline",
    expected_output="Running app deployed to Azure App Service",
    agent=devops_agent
)

