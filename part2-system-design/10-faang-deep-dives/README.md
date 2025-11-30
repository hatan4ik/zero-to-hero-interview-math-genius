# FAANG Deep Dives — Real Interview Questions

## Meta/Facebook Scale Problems
**News Feed (2.9B users)**
- **Write amplification:** 1 post → 1000 friends = 1000 writes to timeline cache
- **Fan-out strategies:** Push (pre-compute) vs Pull (compute on read) vs Hybrid
- **Celebrity problem:** Beyoncé posts → 100M fan-outs crash system
- **Solution:** Pull model for celebrities (>1M followers), push for regular users
- **Numbers:** 300M posts/day, 4.5B likes/day, 100TB/day new content

**Instagram Stories (500M daily users)**  
- **Ephemeral storage:** 24-hour TTL, optimized for sequential access
- **Video processing:** 15-second clips, 5 quality levels, 2-second segments
- **Global distribution:** 150+ edge locations, 99.9% served from cache
- **Storage math:** 500M users × 3 stories × 10MB = 15PB/day (before compression)

## Google Scale Problems  
**Search Index (8.5B pages)**
- **Crawling rate:** 20B pages/day, 200K pages/sec sustained
- **Index sharding:** By term frequency + geographic relevance  
- **Query processing:** <200ms P99 including network, ranking, personalization
- **Caching layers:** L1 (query results) + L2 (index shards) + L3 (page content)

**YouTube Recommendations (2B logged-in users)**
- **Candidate generation:** 1M videos → 100 candidates in <10ms
- **Ranking model:** 100 candidates → 10 recommendations in <50ms  
- **A/B testing:** 1000+ experiments running, 0.1% traffic per test
- **Cold start:** New users get trending + geographic signals

## Amazon Scale Problems
**Prime Video Streaming (200M subscribers)**
- **Bitrate adaptation:** 7 quality levels, switch every 2-10 seconds
- **CDN strategy:** 400+ edge locations, 95% cache hit ratio
- **Encoding pipeline:** 1 source → 28 variants (resolution × bitrate × codec)
- **Cost optimization:** $0.02/GB CDN vs $0.09/GB origin transfer

**Alexa Voice Processing (100M devices)**  
- **Wake word detection:** On-device, <500ms latency, 99.9% accuracy
- **Speech-to-text:** Cloud processing, <800ms end-to-end
- **Intent classification:** 100K+ skills, contextual understanding
- **Privacy:** Voice data encrypted, user deletion within 24 hours

## Netflix Scale Problems
**Content Delivery (230M subscribers)**
- **Encoding optimization:** Per-title encoding saves 20% bandwidth
- **Predictive caching:** Pre-position content based on viewing patterns  
- **Chaos engineering:** Simian Army, failure injection in production
- **Microservices:** 700+ services, 1M+ RPS, 99.99% availability

## Apple Scale Problems  
**App Store Search (500M weekly users)**
- **Real-time indexing:** New apps searchable within 1 hour
- **Personalization:** Download history + device type + location
- **Fraud detection:** ML models detect fake reviews, ratings manipulation
- **Global consistency:** 175 countries, localized results, <100ms latency