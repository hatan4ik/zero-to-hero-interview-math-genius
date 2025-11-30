# System Estimation Framework

## Step 1: Scale Numbers (2 minutes)
```
Users: DAU, MAU, growth rate
Traffic: QPS read/write, seasonal patterns  
Data: Size per record, retention period
Geography: Regions, latency requirements
```

## Step 2: SLA Requirements (1 minute)
```
Latency: P50/P95/P99 targets
Availability: 99.9% vs 99.99% (cost difference)
Consistency: Strong vs eventual vs session
Durability: RPO (data loss tolerance)
```

## Step 3: Resource Calculation (3 minutes)
```
CPU: req/s ÷ (CPU_cores × 1000) < 0.7 utilization
Memory: working_set + cache + buffers + overhead
Storage: data_size × replication_factor × growth_buffer
Network: bandwidth × peak_multiplier × redundancy
```

## Step 4: Cost Modeling (2 minutes)
```
Infrastructure: Compute + storage + network + licenses
Operational: Monitoring + backup + DR + support
Opportunity: Engineering time + technical debt
```

## Step 5: Bottleneck Analysis (2 minutes)
```
Identify limiting factor:
- CPU bound: Horizontal scaling
- Memory bound: Caching strategy  
- I/O bound: Async processing
- Network bound: CDN + compression
```

## Quick Reference Numbers
```
Database: 1K QPS per core (OLTP), 10K QPS (read replica)
Cache: 100K ops/sec per Redis instance
Queue: 10K msg/sec per Kafka partition
CDN: 95% hit ratio typical, 99%+ for static assets
Network: 1Gbps = 125MB/s, RTT adds 2× latency minimum
```