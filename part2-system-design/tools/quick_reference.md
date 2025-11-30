# Quick Reference — Numbers Every Engineer Should Know

## Latency Numbers (2024 Edition)
```
L1 cache reference:           0.5 ns
Branch mispredict:            5 ns  
L2 cache reference:           7 ns
Mutex lock/unlock:           100 ns
Main memory reference:       100 ns
Compress 1KB with Zippy:   10,000 ns = 10 μs
Send 1KB over 1 Gbps:      10,000 ns = 10 μs
Read 4KB randomly from SSD: 150,000 ns = 150 μs
Read 1MB sequentially from memory: 250,000 ns = 250 μs
Round trip within datacenter: 500,000 ns = 500 μs
Read 1MB sequentially from SSD: 1,000,000 ns = 1 ms
Disk seek: 10,000,000 ns = 10 ms
Read 1MB sequentially from disk: 30,000,000 ns = 30 ms
Send packet CA→Netherlands→CA: 150,000,000 ns = 150 ms
```

## Throughput Benchmarks
```
Redis: 100K ops/sec (single instance)
PostgreSQL: 1K TPS (OLTP), 10K QPS (read replica)  
MySQL: 1K TPS (OLTP), 15K QPS (read replica)
Kafka: 10K msg/sec per partition, 1M msg/sec per cluster
Elasticsearch: 10K docs/sec indexing, 100K queries/sec
MongoDB: 5K writes/sec, 50K reads/sec (typical workload)
```

## Storage & Network
```
1 Gbps network = 125 MB/s theoretical, ~100 MB/s practical
10 Gbps network = 1.25 GB/s theoretical, ~1 GB/s practical
SSD: 500 MB/s sequential, 50K IOPS random
NVMe SSD: 3 GB/s sequential, 500K IOPS random
HDD: 100 MB/s sequential, 100 IOPS random
```

## Cost Estimates (AWS us-east-1, 2024)
```
EC2 m5.large: $0.096/hour = $70/month
RDS db.t3.medium: $0.068/hour = $50/month  
S3 Standard: $0.023/GB/month
EBS gp3: $0.08/GB/month
Data transfer out: $0.09/GB (first 10TB)
CloudFront: $0.085/GB (first 10TB)
```

## Rule of Thumb Calculations
```
Database connections = CPU cores × 2-4
Cache hit ratio target = 85%+ (90%+ for hot data)
Load balancer utilization = <70% for burst capacity
Queue depth alert = >100 messages
Error budget (99.9%) = 43.8 minutes/month
Replication lag target = <1 second
```