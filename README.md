#  AI Bug Triage System

Welcome to the **AI Bug Triage System**! This intelligent DevOps tool uses Google AI to automatically classify bugs, suggest fixes, and integrate seamlessly with your GitHub repositories—making issue management smarter and faster.

##  Features

* **AI-Powered Bug Classification**
   * Automatically assesses severity (Critical, High, Medium, Low)
   * Detects bug categories (UI, Backend, Database, Security, etc.)
   * Scores priority and estimates effort

* **Smart Fix Suggestions**
   * AI-generated recommendations and code samples
   * Step-by-step implementation guidance
   * Risk assessment and time estimates

* **GitHub Integration**
   * Import/sync issues from your repositories
   * Enables automatic issue classification and model training

* **Analytics & Insights**
   * Bug resolution statistics
   * Team performance metrics
   * AI accuracy tracking

##  Quick Start

### Prerequisites

* Python 3.9+
* Google AI API key
* Docker (optional, for containerized deployment)

### Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/yourusername/ai-bug-triage
   cd ai-in-devops
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your API keys
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

   Open your browser and go to `http://localhost:5000`

### Docker Deployment

```bash
docker-compose up -d
```

##  API Endpoints

### Analyze a Bug

```http
POST /api/analyze-bug
Content-Type: application/json

{
  "title": "Login page crashes on mobile",
  "description": "When users try to login on mobile devices...",
  "environment": "iOS Safari 14.0",
  "component": "frontend"
}
```

### Sync with GitHub

```http
POST /api/github-sync
Content-Type: application/json

{
  "repo_url": "https://github.com/owner/repository"
}
```

### Get Statistics

```http
GET /api/stats
```

### Trigger Model Training

```http
POST /api/train-model
```

##  Configuration

### Key Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GOOGLE_AI_API_KEY` | Google AI API key | Yes |
| `GITHUB_TOKEN` | Your GitHub personal token | No |
| `DATABASE_URL` | Database connection string | No |
| `DEBUG` | Enable debug mode | No |

##  Architecture

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│ Frontend    │    │ Flask API   │    │ Google AI   │
│ (HTML/JS)   │<-->│ (Python)    │<-->│ (Gemini)    │
└─────────────┘    └─────────────┘    └─────────────┘
       │            ▼
┌─────────────┐    ┌─────────────┐
│ SQLite DB   │    │ ChromaDB    │
│ (Metadata)  │    │ (Vectors)   │
└─────────────┘    └─────────────┘
```

## Contributing

1. Fork this repository
2. Create a new feature branch
3. Make your changes (add tests if needed)
4. Submit a pull request

## License

MIT License – see the `LICENSE` file for more info.

## Support & Questions

* Create an issue on GitHub
* Check the documentation and API examples
* PRs and suggestions welcome!

Built with love for DevOps teams.
