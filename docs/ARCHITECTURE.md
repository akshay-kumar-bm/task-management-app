# Architecture: Task Management App

## Tech Stack
- Backend: FastAPI (Python 3.11)
- Frontend: React 18 (SPA)
- Database: PostgreSQL 14
- Auth: OAuth2 / JWT
- Containerisation: Docker + Docker Compose
- CI/CD: GitHub Actions

## Folder Structure
```
task-management-app/
  app/           # FastAPI backend
  frontend/      # React SPA
  docs/          # Architecture & design docs
  .github/workflows/
  Dockerfile
  docker-compose.yml
  requirements.txt
```

## Database Schema
- users(id, email, name, created_at)
- tasks(id, title, description, assignee_id, due_date, status, created_at)
- comments(id, task_id, author_id, body, created_at)
- notifications(id, user_id, message, read, created_at)

## Non-Functional Requirements
- Load in < 2s for 500 concurrent users
- GDPR-compliant data encryption at rest and in transit
- HTTPS enforced, secrets via environment variables

## References
- PRD: https://akshaykuamrbm.atlassian.net/wiki/spaces/TASKMANAGE/pages/2064385
