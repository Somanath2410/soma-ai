# API Endpoints Documentation

## Base URL

```
http://localhost:8000
```

## Interactive API Documentation

After starting the server, visit:
- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`

---

## Health Check Endpoints

### Get Health Status
**GET** `/api/health/`

Check if the API is healthy.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2024-05-20T13:45:00.123456",
  "version": "0.1.0"
}
```

### Readiness Check
**GET** `/api/health/ready`

Check if the API is ready to accept requests.

**Response:**
```json
{
  "status": "ready",
  "timestamp": "2024-05-20T13:45:00.123456",
  "version": "0.1.0"
}
```

### Liveness Check
**GET** `/api/health/live`

Check if the API is alive.

**Response:**
```json
{
  "status": "alive",
  "timestamp": "2024-05-20T13:45:00.123456",
  "version": "0.1.0"
}
```

---

## Chat Endpoints

### Process Prompt
**POST** `/api/chat/process`

Send a prompt to the AI engine and get a response.

**Request Body:**
```json
{
  "prompt": "What is machine learning?",
  "model": "gpt-3.5-turbo",
  "temperature": 0.7
}
```

**Response:**
```json
{
  "response": "Machine learning is a subset of artificial intelligence...",
  "model": "gpt-3.5-turbo",
  "tokens_used": 150,
  "success": true
}
```

**Status Codes:**
- `200` - Success
- `422` - Validation error
- `500` - Server error

### Chat
**POST** `/api/chat/chat`

Interactive chat endpoint.

**Request Body:**
```json
{
  "prompt": "Tell me a joke",
  "temperature": 0.8
}
```

**Response:**
```json
{
  "success": true,
  "message": "Tell me a joke",
  "response": "Why did the AI go to school? To improve its learning!",
  "model": "gpt-3.5-turbo",
  "timestamp": null
}
```

### List Available Models
**GET** `/api/chat/models`

Get list of available AI models.

**Response:**
```json
{
  "success": true,
  "models": [
    {
      "id": "gpt-3.5-turbo",
      "name": "GPT-3.5 Turbo",
      "provider": "OpenAI"
    },
    {
      "id": "gpt-4",
      "name": "GPT-4",
      "provider": "OpenAI"
    },
    {
      "id": "claude-3-opus",
      "name": "Claude 3 Opus",
      "provider": "Anthropic"
    }
  ],
  "current_model": "gpt-3.5-turbo"
}
```

---

## Error Handling

All errors follow this format:

```json
{
  "detail": "Error message describing what went wrong"
}
```

**Common HTTP Status Codes:**
- `200` - OK
- `400` - Bad Request
- `422` - Validation Error
- `500` - Internal Server Error

---

## Request Validation

### PromptRequest Schema
```json
{
  "prompt": "string (required, 1-2000 characters)",
  "model": "string (optional)",
  "temperature": "number (optional, 0.0-1.0, default: 0.7)"
}
```

### AIResponse Schema
```json
{
  "response": "string (required)",
  "model": "string (required)",
  "tokens_used": "integer (optional)",
  "success": "boolean (required)"
}
```

---

## CORS

CORS is enabled for all origins. You can make requests from any domain.

**Allowed Methods:** GET, POST, PUT, DELETE, OPTIONS
**Allowed Headers:** All

---

## Example Requests

### Using cURL

Health check:
```bash
curl http://localhost:8000/api/health/
```

Process prompt:
```bash
curl -X POST http://localhost:8000/api/chat/process \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "What is AI?",
    "temperature": 0.7
  }'
```

### Using Python

```python
import requests

# Health check
response = requests.get('http://localhost:8000/api/health/')
print(response.json())

# Process prompt
response = requests.post(
    'http://localhost:8000/api/chat/process',
    json={
        'prompt': 'What is AI?',
        'temperature': 0.7
    }
)
print(response.json())
```

### Using JavaScript/TypeScript

```javascript
// Health check
fetch('http://localhost:8000/api/health/')
  .then(res => res.json())
  .then(data => console.log(data));

// Process prompt
fetch('http://localhost:8000/api/chat/process', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    prompt: 'What is AI?',
    temperature: 0.7
  })
})
  .then(res => res.json())
  .then(data => console.log(data));
```
