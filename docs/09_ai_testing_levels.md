# AI Testing Levels

AI systems need more than a single accuracy test. Testing should happen at different levels because an AI system includes data, models, software, infrastructure, user interaction, and governance.

This page explains the main testing levels in a practical way.

## Testing levels overview

| Test level | What is tested | Example focus |
|---|---|---|
| Component testing | one isolated part | data function, model endpoint, retrieval module, prompt template |
| Integration testing | connected parts | model plus retrieval, agent plus tools, API plus UI |
| System testing | the complete AI system | end-to-end behaviour under realistic conditions |
| Acceptance testing | fitness for intended use | user needs, workflow fit, usability, operational readiness |
| Data quality testing | data used by the AI system | completeness, duplicates, imbalance, provenance, representativeness |
| Model testing | model behaviour | performance, robustness, subgroup results, calibration |
| Deployment testing | runtime environment | latency, availability, security, scalability, monitoring |

## Component testing

Component testing checks whether an individual part works as expected. In AI systems, this can include data loading functions, preprocessing scripts, model inference endpoints, retrieval functions, prompt templates, post-processing functions, or logging components.

## Integration testing

Integration testing checks whether connected parts work together. For example, a retrieval system may work alone and a model may work alone, but the combined RAG workflow may still fail if the wrong context is retrieved or if the prompt does not use the retrieved information correctly.

## System testing

System testing checks the full AI system. It should include realistic inputs, realistic operating conditions, expected user workflows, and known edge cases.

## Acceptance testing

Acceptance testing checks whether the system is suitable for the intended users and intended context. This is where usability, workflow fit, trust, documentation, limitations, and user feedback become important.

## Data quality testing

Data quality testing checks whether the data is suitable for the intended AI task. Useful checks include missing values, duplicates, class imbalance, label quality, data drift, representativeness, provenance, and data constraints.

## Model testing

Model testing checks the behaviour of the model itself. This can include performance metrics, subgroup analysis, robustness testing, calibration, stress testing, and comparison with baseline models.

## Deployment testing

Deployment testing checks whether the system works in the target runtime environment. This includes latency, throughput, monitoring, access control, availability, rollback, and cost behaviour.

## Practical message

Testing should be selected based on the risk and the layer. A data risk needs data testing. A model risk needs model testing. An orchestration risk needs workflow or integration testing. An application risk needs usability and acceptance testing.