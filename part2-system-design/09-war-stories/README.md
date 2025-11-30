# War Stories & Anti-Patterns

## The Great Database Migration of 2019
**Problem:** 50TB MySQL → PostgreSQL with zero downtime  
**Solution:** Dual-write pattern + lag monitoring + gradual traffic shift  
**Lesson:** Migration time = data_size / (bandwidth × efficiency_factor × available_hours)  
**Reality check:** 50TB took 6 weeks, not the planned 2 weeks

## Cache Stampede at Scale
**Incident:** Popular cache key expired during Black Friday  
**Impact:** 10,000 concurrent requests hit database, 30s response time  
**Fix:** Probabilistic early expiration: expire_time - random(0, 60s)  
**Prevention:** Cache warming + circuit breakers + request coalescing

## The Microservices Monolith
**Anti-pattern:** 47 services for a 5-person team  
**Overhead:** 2 weeks/quarter just for dependency updates  
**Rule:** Start with modular monolith, extract services when team > 8 people  
**Conway's Law:** System design mirrors org structure, not the other way around

## Premature Sharding Disaster
**Mistake:** Sharded user table at 100K users "for future scale"  
**Cost:** 6 months of cross-shard query complexity  
**Reality:** Vertical scaling handles 10M+ users on modern hardware  
**Lesson:** Shard when CPU/memory maxed AND traffic patterns are stable

## The Kubernetes Overkill
**Scenario:** 3-service app deployed on 12-node K8s cluster  
**Monthly cost:** $2,400 vs $200 for equivalent VMs  
**Complexity:** 40 YAML files, 3 operators, 2 service meshes  
**Sweet spot:** K8s pays off with 20+ services OR multi-team deployment needs

## Vendor Lock-in Escape
**Challenge:** Migrate from proprietary NoSQL to open source  
**Timeline:** 18 months, $2M engineering cost  
**Strategy:** Abstract data layer + parallel writes + gradual cutover  
**Prevention:** Multi-cloud from day 1 costs 20% more, saves 10x in exit scenarios