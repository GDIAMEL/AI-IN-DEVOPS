
# github_integration.py - GitHub Issues Integration
import requests
from typing import List, Dict
import json
from datetime import datetime

class GitHubIntegration:
    def __init__(self, token: str = None):
        self.token = token
        self.headers = {
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'Bug-Triage-Tool'
        }

        if token:
            self.headers['Authorization'] = f'token {token}'

    def fetch_issues(self, repo_url: str, state: str = 'all', labels: str = '') -> List[Dict]:
        """Fetch issues from GitHub repository"""
        try:
            # Parse repository URL
            repo_path = self._parse_repo_url(repo_url)
            if not repo_path:
                raise ValueError("Invalid GitHub repository URL")

            # Build API URL
            api_url = f"https://api.github.com/repos/{repo_path}/issues"
            params = {
                'state': state,
                'per_page': 100,
                'sort': 'created',
                'direction': 'desc'
            }

            if labels:
                params['labels'] = labels

            response = requests.get(api_url, headers=self.headers, params=params)
            response.raise_for_status()

            issues = response.json()

            # Filter out pull requests (GitHub treats PRs as issues)
            bug_issues = []
            for issue in issues:
                if 'pull_request' not in issue:
                    bug_issues.append({
                        'id': issue['id'],
                        'number': issue['number'],
                        'title': issue['title'],
                        'body': issue['body'],
                        'state': issue['state'],
                        'labels': [label['name'] for label in issue['labels']],
                        'created_at': issue['created_at'],
                        'updated_at': issue['updated_at'],
                        'assignees': [assignee['login'] for assignee in issue['assignees']],
                        'url': issue['html_url']
                    })

            return bug_issues

        except Exception as e:
            print(f"Error fetching GitHub issues: {e}")
            return []

    def _parse_repo_url(self, repo_url: str) -> str:
        """Parse GitHub repository URL to extract owner/repo"""
        if 'github.com/' in repo_url:
            parts = repo_url.split('github.com/')[-1].split('/')
            if len(parts) >= 2:
                return f"{parts[0]}/{parts[1]}"
        return ""

    def create_issue(self, repo_path: str, title: str, body: str, labels: List[str] = None) -> Dict:
        """Create a new GitHub issue"""
        if not self.token:
            raise ValueError("GitHub token required to create issues")

        api_url = f"https://api.github.com/repos/{repo_path}/issues"
        data = {
            'title': title,
            'body': body
        }

        if labels:
            data['labels'] = labels

        response = requests.post(api_url, headers=self.headers, json=data)
        response.raise_for_status()

        return response.json()

    def update_issue(self, repo_path: str, issue_number: int, **kwargs) -> Dict:
        """Update an existing GitHub issue"""
        if not self.token:
            raise ValueError("GitHub token required to update issues")

        api_url = f"https://api.github.com/repos/{repo_path}/issues/{issue_number}"

        response = requests.patch(api_url, headers=self.headers, json=kwargs)
        response.raise_for_status()

        return response.json()

    def add_comment(self, repo_path: str, issue_number: int, comment: str) -> Dict:
        """Add a comment to an issue"""
        if not self.token:
            raise ValueError("GitHub token required to add comments")

        api_url = f"https://api.github.com/repos/{repo_path}/issues/{issue_number}/comments"
        data = {'body': comment}

        response = requests.post(api_url, headers=self.headers, json=data)
        response.raise_for_status()

        return response.json()
