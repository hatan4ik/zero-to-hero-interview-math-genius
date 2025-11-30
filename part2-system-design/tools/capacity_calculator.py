#!/usr/bin/env python3

def estimate_throughput(latency_ms, concurrent_users, think_time_s=0):
    """Little's Law: N = λ × L, solve for λ"""
    total_time = (latency_ms / 1000) + think_time_s
    return concurrent_users / total_time if total_time > 0 else 0

def cache_memory_needed(objects_count, avg_size_kb, overhead_factor=1.3):
    """Memory = objects × size × overhead (fragmentation, metadata)"""
    return objects_count * avg_size_kb * overhead_factor / 1024  # GB

def database_connections(cpu_cores, connection_multiplier=3):
    """Rule of thumb: 2-4x CPU cores for connection pool"""
    return cpu_cores * connection_multiplier

def storage_cost_aws(tb_per_month, storage_type="gp3"):
    """AWS EBS pricing (simplified)"""
    costs = {"gp3": 0.08, "io2": 0.125, "s3_standard": 0.023}
    return tb_per_month * 1024 * costs.get(storage_type, 0.08)

def bandwidth_cost(gb_per_month, region="us-east"):
    """AWS data transfer out pricing"""
    if gb_per_month <= 100: return 0
    elif gb_per_month <= 10240: return (gb_per_month - 100) * 0.09
    else: return 921.6 + (gb_per_month - 10240) * 0.085

if __name__ == "__main__":
    # Example calculations
    print(f"Throughput: {estimate_throughput(100, 1000):.1f} req/s")
    print(f"Cache memory: {cache_memory_needed(1000000, 4):.1f} GB")
    print(f"DB connections: {database_connections(8)} connections")
    print(f"Storage cost: ${storage_cost_aws(10):.2f}/month")