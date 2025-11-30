# Tradeoff Decision Cheats

- **SQL vs NoSQL:** Strong consistency + joins + analytics → SQL. Massive scale + simple access + multi-region active-active → NoSQL (Dynamo/Cassandra).  
- **Cache strategy:** Read-heavy with temporal locality → Redis/Memcached. Write-heavy or strict consistency → database first with read-through or write-through cache.  
- **Queues vs sync calls:** Spiky traffic, retry safety, decouple failures → queue/stream. Low-latency user path with tight SLAs → synchronous + circuit breakers.  
- **Sharding timing:** Shard when CPU/io maxed AND traffic patterns stable. Premature sharding increases complexity and ops cost.  
- **CDN/edge:** Static assets and media → CDN by default. Dynamic content → edge compute only when latency/egress justify added complexity.  
- **Serverless vs containers:** <30% avg utilization, spiky workloads → serverless. Steady traffic or heavy dependencies → containers/VMs.  
- **Global vs regional:** User latency <100ms global? → multi-region active-active with conflict resolution. Otherwise single-region + DR.  
- **Consistency level:** Money/ledger → strong + idempotency keys. Social feed/search → eventual + background repair.  
- **Observability cost:** Sample traces (1-5%), pre-aggregate metrics; logs to cold storage with retention tiers.  
- **Security posture:** Public APIs → authN/authZ, rate limits, WAF. PII/PCI → tokenization, encryption at rest+transit, least privilege, audit trails.
