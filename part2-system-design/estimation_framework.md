# Estimation Framework — 10-Minute Flow

1. **Traffic math:** Peak QPS = daily volume / 86,400 × peak factor (2-5x). Concurrency = QPS × latency (s).  
2. **Storage:** (objects/day × avg size) × retention. Add 20-30% overhead for metadata/replication.  
3. **Hotset vs coldset:** Assume 20% of keys drive 80% traffic; cache size = hot objects × size × overhead.  
4. **Latency budget:** Network (WAN 50-150ms) + app (5-20ms) + datastore (1-10ms cache, 5-50ms DB) + queueing.  
5. **Availability:** A_system = Π A_component. Redundancy math: A=1-(1-a)^N. Target 99.9% unless otherwise stated.  
6. **Read/write mix:** Route reads to cache/replicas, writes to primaries; pick quorum config (N,R,W) to match consistency.  
7. **Back-of-envelope infra:**  
   - **Cache:** RPS_cache = hit_ratio × reads; size from hotset.  
   - **DB:** writes/QPS ÷ per-node capacity; add replicas = ceiling(load / capacity).  
   - **Queue:** λ, μ ⇒ ρ=λ/μ < 0.7.  
8. **Cost sanity:** Storage $0.02–0.03/GB-month (object), $0.08/GB-month (block), egress $0.09/GB first 10TB.  
9. **Bottlenecks:** Identify first limit (DB QPS, cache size, network egress, P99 latency).  
10. **Narrate constraints:** “At 2K QPS writes and 90/10 read/write, primary handles 200 writes/s; I’ll add 3 replicas for reads and a 4GB Redis hotset.”
