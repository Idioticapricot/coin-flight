# Flight Price Agent

A hardcoded flight price agent for multi-agent workflow demo. Returns flight pricing information for travel queries.

## Features

- 🛫 Flight price information
- 🤖 Built on Orca Agent SDK for Algorand integration
- 🐳 Docker containerized for easy deployment
- 🚀 GitHub Actions CI/CD pipeline

## Quick Start

### Local Development

1. **Clone and install dependencies:**
   ```bash
   git clone <repository-url>
   cd coin-flight
   pip install -r requirements.txt
   ```

2. **Run the agent:**
   ```bash
   python app.py
   ```

### Docker Deployment

1. **Build and run:**
   ```bash
   docker build -t flight-agent .
   docker run -p 8000:8000 flight-agent
   ```

2. **Or use pre-built image:**
   ```bash
   docker run -p 8000:8000 ghcr.io/idioticapricot/coin-flight:latest
   ```

## Configuration

Update the agent configuration in `app.py`:

```python
config = AgentConfig(
    agent_id="your-agent-id",
    receiver_address="YOUR_ALGO_ADDRESS", 
    price_microalgos=1_000_000,
    agent_token="your_agent_token",
    remote_server_url="http://localhost:3000/api/agent/access"
)
```

## Tech Stack

- **Agent Framework**: Orca Agent SDK
- **Runtime**: Python 3.12
- **Containerization**: Docker
- **CI/CD**: GitHub Actions

## Deployment

The agent automatically deploys to GitHub Container Registry on push to main branch. Configure your Kubernetes deployment to pull from `ghcr.io/idioticapricot/coin-flight:latest`.

## License

MIT License
