
# AI Bug Triage System

An intelligent DevOps tool that uses Google AI to automatically classify bugs, suggest fixes, and integrate with GitHub repositories.

## Features

**AI-Powered Classification**
- Automatic severity assessment (Critical, High, Medium, Low)
- Category detection (UI, Backend, Database, Security, etc.)
- Priority scoring and effort estimation

**Smart Fix Suggestions**
- AI-generated fix recommendations
- Code examples and implementation steps
- Risk assessment and time estimates

**GitHub Integration**
- Import issues from GitHub repositories
- Sync bug data for model training
- Automatic issue classification

**Analytics & Insights**
- Bug resolution statistics
- Team performance metrics
- AI accuracy tracking

## Quick Start

### Prerequisites
- Python 3.9+
- Google AI API key
- Docker (optional)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ai-bug-triage
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:5000`

### Docker Deployment

```bash
# Build and run with Docker Compose
docker-compose up -d
```

## API Endpoints

### Analyze Bug
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

### GitHub Sync
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

## Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GOOGLE_AI_API_KEY` | Google AI API key | Yes |
| `GITHUB_TOKEN` | GitHub personal access token | No |
| `DATABASE_URL` | Database connection string | No |
| `DEBUG` | Enable debug mode | No |

### Model Training

The system automatically learns from resolved bugs to improve accuracy:

```http
POST /api/train-model
```

## Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Flask API     │    │   Google AI     │
│   (HTML/JS)     │◄──►│   (Python)      │◄──►│   (Gemini)      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                              │
                              ▼
                       ┌─────────────────┐    ┌─────────────────┐
                       │   SQLite DB     │    │   ChromaDB      │
                       │   (Metadata)    │    │   (Vectors)     │
                       └─────────────────┘    └─────────────────┘
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## License

MIT License - see LICENSE file for details.

## Support

For issues and questions:
- Create a GitHub issue
- Check the documentation
- Review the API examples

---

Built with love for DevOps teams
