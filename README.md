# MCP

A space for learning about and experimenting with Model Context Protocl.

Some of the code is based on code from the book *AI Agents with MCP*. The book repo is [ai_agents_mcp_examples](https://github.com/kylestratis/ai_agents_mcp_examples).

## Initial setup

The project was created with uv and initial packages added:

```
uv add python-dotenv
uv add openai
```

## Environment variables

To use Azure OpenAI, set the following in .env:

```
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_ENDPOINT="https://<YOUR_PROJECT_RESOURCE>.openai.azure.com/openai/v1"
AZURE_OPENAI_DEPLOYMENT_NAME="gpt-5.4-mini"
```

