# ML Systems Design — FAANG AI/ML Roles

## Recommendation Systems (Netflix/YouTube scale)
**Candidate Generation:** 1M items → 1K candidates in <10ms
- **Collaborative filtering:** User-item matrix factorization, 100M+ users
- **Content-based:** Item embeddings, cosine similarity, real-time inference
- **Two-tower model:** User tower + Item tower, dot product scoring

**Ranking Stage:** 1K candidates → 10 recommendations in <50ms
- **Feature engineering:** 1000+ features, real-time + batch
- **Model serving:** TensorFlow Serving, 99.9% availability, <20ms P95
- **A/B testing:** 1000+ experiments, statistical significance, guardrail metrics

## Search Ranking (Google/Bing scale)
**Query Understanding:** 8.5B queries/day
- **Intent classification:** Navigational/Informational/Transactional
- **Query expansion:** Synonyms, typo correction, semantic matching
- **Personalization:** Search history, location, device type

**Document Scoring:** 100B+ documents indexed
- **TF-IDF baseline:** Term frequency × Inverse document frequency
- **Learning to Rank:** LambdaMART, RankNet, pairwise loss functions
- **Neural ranking:** BERT-based models, 768-dim embeddings

## Real-time ML Inference
**Feature Store Architecture:**
- **Batch features:** Daily ETL, historical aggregations, 24-hour freshness
- **Streaming features:** Kafka + Flink, <1 second freshness
- **Online features:** Redis/DynamoDB, <1ms lookup latency

**Model Serving Patterns:**
- **Synchronous:** REST API, <100ms timeout, circuit breakers
- **Asynchronous:** Message queues, batch prediction, cost optimization
- **Edge inference:** Mobile/IoT, model quantization, <10MB models

## Training Infrastructure
**Data Pipeline:** 100TB+ training data
- **Feature extraction:** Spark/Beam, distributed processing
- **Data validation:** Schema drift detection, statistical tests
- **Versioning:** DVC, MLflow, reproducible experiments

**Model Training:** Multi-GPU/TPU clusters
- **Distributed training:** Parameter servers, gradient synchronization
- **Hyperparameter tuning:** Bayesian optimization, early stopping
- **Resource management:** Kubernetes, auto-scaling, spot instances

## ML Monitoring & Observability
**Model Performance:**
- **Accuracy drift:** Statistical tests, confidence intervals
- **Latency monitoring:** P50/P95/P99 inference time
- **Throughput:** QPS, batch processing rates

**Data Quality:**
- **Schema validation:** Feature type/range checks
- **Distribution shift:** KL divergence, population stability index
- **Missing values:** Imputation strategies, default handling