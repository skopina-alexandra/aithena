# Project Plan

## Week 1: FastAPI Foundation + Async DB

**Goal**: Monitored API with async PostgreSQL

**Assignment**:

```python
@app.post("/categorize")
async def categorize_transaction(transaction: TransactionSchema):
    # Async DB call with asyncpg
    await db.execute("INSERT INTO transactions...")
```

**Tools**: FastAPI, pytest, asyncpg

**Deliverable**: API with OpenAPI docs + 10 async pytest cases

## Week 2: Transaction Processing + Fraud Detection

**Goal**: Pipeline with anomaly detection

**Assignment**:

```python
if isolation_forest.predict(transaction) == -1:
    flag_fraud(transaction)
```

**Tools**: Pydantic, tenacity, scikit-learn
**Deliverable**: Validation system + fraud detection report

## Week 3: PostgreSQL Database

**Goal**: Vector-enabled finance schema

**Assignment**:

```sql
CREATE EXTENSION pgvector;  -- Add vector search
ALTER TABLE transactions ADD COLUMN embedding VECTOR(384);
```

**Tools**: PostgreSQL, SQLAlchemy, pgvector

**Deliverable**: Dockerized DB + vector migration scripts

## Week 4: Telegram Bot + State Management

**Goal**: Multi-step finance queries

**Assignment**:

```python
def expense_comparison(update, context):
    context.user_data['flow'] = "compare_months"  # Track state in Redis
```

**Tools**: python-telegram-bot, Redis

**Deliverable**: Bot with conversation flows

## Week 5: Agent Core + Evaluation

**Goal**: Transaction-aware agent

**Assignment**:

```python
agent = create_sql_agent(llm, db=db)  # LangChain agent w/ DB access
```

**Tools**: LangChain, LangSmith

**Deliverable**: Agent + accuracy/latency metrics

## Week 6: Redis Caching + Optimization

**Goal**: Low-latency responses

**Assignment**:

```python
@cache(ttl=300, key="user:{user_id}:spending")  # Auto-invalidate on writes
def get_monthly_spending(user_id): ...
```

**Tools**: Redis, asyncpg

**Deliverable**: 40% latency reduction report

## Week 7: CI/CD + Feature Flags

**Goal**: Safe rollout of agent features

**Assignment**:

```yaml
- name: Toggle feature
  run: flipper enable "new_categorization_agent"
```

**Tools**: Docker, Render, Flipper

**Deliverable**: Deployment with canary releases

## Week 8: Monitoring + Tracing

**Goal**: Track agent decisions

**Assignment**:

```python
with tracer.start_as_current_span("categorize_transaction"):  # OpenTelemetry
    agent.run(query)
```

**Tools**: Prometheus, Grafana, OpenTelemetry

**Deliverable**: Dashboard + trace visualization

## Week 9: Security Hardening

**Goal**: Encrypted PII/rate limits

**Assignment**:

```sql
-- Encrypt sensitive columns
CREATE EXTENSION pgcrypto;
INSERT INTO users (ssn) VALUES (pgp_sym_encrypt('123-45-6789', 'key'));
```

**Tools**: OWASP ZAP, slowapi, pgcrypto

**Deliverable**: Pen test report + encrypted DB

## Week 10: RAG for Personal Finance

**Goal**: User-specific financial logic

**Assignment**:

```python
retriever = db.as_retriever(search_type="mmr")  # Find similar transactions
agent = RetrievalAgent.from_llm(llm, retriever)
```

**Tools**: LangChain, pgvector, scikit-learn

**Deliverable**: Proactive alerts + spend forecasting

## Week 11: Agent Load Testing

**Goal**: Simulate real user flows

**Assignment**:

```python
class AgentUser(User):
    @task
    def categorize_transaction(self):
        self.client.post("/categorize", json={...})
```

**Tools**: Locust, k6

**Deliverable**: 1000 RPM load test report

## Week 12: Chaos Engineering

**Goal**: Transaction pipeline resilience

**Assignment**:

```python
@retry(stop=stop_after_attempt(3))  # Tenacity retries
def categorize_transaction(transaction): ...
```

**Tools**: Chaos Toolkit, pumba

**Deliverable**: Automated failure recovery plan

## Week 13: Portfolio Packaging

**Goal**: Professional showcase

**Assignment**:

![plan](aithena-plan.svg)

**Tools**: Mermaid.js, OBS Studio, Sentry

**Deliverable**: GitHub repo + demo video + error monitoring