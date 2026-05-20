# API Reference

## Base URL

```
http://localhost:8000
```

## Endpoints

### Process Prompt

**POST** `/api/process`

Process a prompt using the AI engine.

**Request Body:**
```json
{
  "prompt": "Your prompt here",
  "model": "gpt-3.5-turbo",
  "temperature": 0.7
}
```

**Response:**
```json
{
  "response": "AI response here",
  "model": "gpt-3.5-turbo",
  "tokens_used": 150,
  "success": true
}
```

**Status Codes:**
- `200` - Success
- `400` - Bad Request
- `500` - Internal Server Error

## Error Handling

All errors follow this format:

```json
{
  "error": "Error message",
  "details": "Additional details",
  "success": false
}
```

## Rate Limiting

- 100 requests per minute per IP

## Authentication

Currently uses API key authentication via header:

```
Authorization: Bearer YOUR_API_KEY
```
