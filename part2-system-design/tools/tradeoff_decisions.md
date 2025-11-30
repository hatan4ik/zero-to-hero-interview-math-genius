# Trade-off Decision Trees

## Consistency Model Decision
```
Strong Consistency Required?
├── Yes (Financial, Inventory)
│   ├── Single Region → ACID DB + Sync replication
│   └── Multi Region → Consensus (Raft/Paxos) + Higher latency
└── No (Social, Analytics)
    ├── Real-time Updates → Eventually consistent + Conflict resolution
    └── Batch Updates → Async replication + Reconciliation
```

## Database Choice Decision  
```
Data Structure?
├── Relational (ACID, Complex queries)
│   ├── <1TB → Single PostgreSQL/MySQL
│   └── >1TB → Sharded RDBMS or NewSQL
├── Document (Flexible schema)
│   ├── <100GB → MongoDB single node
│   └── >100GB → MongoDB sharded or DynamoDB
└── Key-Value (Simple access patterns)
    ├── In-memory → Redis/Memcached
    └── Persistent → DynamoDB/Cassandra
```

## Caching Strategy Decision
```
Access Pattern?
├── Read Heavy (90%+ reads)
│   ├── Static Data → CDN + Long TTL
│   └── Dynamic Data → Application cache + Short TTL
├── Write Heavy (50%+ writes)
│   ├── Write-through → Consistency + Latency penalty
│   └── Write-behind → Performance + Complexity
└── Mixed Workload
    ├── Cache-aside → Manual management + Flexibility
    └── Read-through → Automatic + Cache warming needed
```

## Scaling Strategy Decision
```
Current Bottleneck?
├── CPU Bound
│   ├── Stateless → Horizontal scaling (load balancer)
│   └── Stateful → Vertical scaling or partitioning
├── Memory Bound  
│   ├── Cache Miss → Increase cache size or better eviction
│   └── Memory Leak → Profiling + garbage collection tuning
├── I/O Bound
│   ├── Database → Read replicas or connection pooling
│   └── Disk → SSD upgrade or async processing
└── Network Bound
    ├── Bandwidth → CDN or compression
    └── Latency → Edge computing or protocol optimization
```

## Microservices vs Monolith
```
Team Size & Complexity?
├── <8 people, <10 services → Modular monolith
├── 8-20 people, 10-50 services → Microservices + Service mesh
└── >20 people, >50 services → Domain-driven design + Platform team

Deployment Frequency?
├── Weekly/Monthly → Monolith (simpler deployment)
└── Daily/Hourly → Microservices (independent deployment)

Technology Diversity?
├── Single stack → Monolith (shared libraries)
└── Polyglot → Microservices (best tool per service)
```