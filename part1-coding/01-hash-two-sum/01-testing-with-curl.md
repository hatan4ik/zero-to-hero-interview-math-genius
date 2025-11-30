# Tooling Guide: Testing with cURL

`curl` is an essential tool for testing APIs and understanding system behavior. Here’s how you can use it to test the idempotency and retry logic discussed in the case studies.

## Testing Idempotency

To test idempotency, you send the same request multiple times with the same `Idempotency-Key` header. The server should process the request only once.

**First Request:**
```bash
# The server should process this and return a 200 OK.
curl -X POST https://api.example.com/payments \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: a1b2c3d4-e5f6-7890-1234-567890abcdef" \
  -d '{"amount": 1000, "currency": "usd"}'
```

**Second (Retry) Request:**
```bash
# Send the exact same request again.
# The server should recognize the key and return a cached 200 OK without reprocessing.
curl -X POST https://api.example.com/payments \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: a1b2c3d4-e5f6-7890-1234-567890abcdef" \
  -d '{"amount": 1000, "currency": "usd"}'
```

A correct implementation will charge the customer only once. This is a simple but powerful way to verify the safety of your API.