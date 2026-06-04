# Architecture Decision Guideline

This guide helps readers decide which layer they should focus on.

## If you want to develop an algorithm

Work mainly in Layer 5: Model and Learning.

Typical activities include model design, training, fine-tuning, model comparison, evaluation, compression, distillation, and performance testing.

## If you want to use internal documents or external knowledge

Work mainly in Layer 4: Data and Knowledge.

Typical activities include data collection, cleaning, chunking, embeddings, vector databases, retrieval, knowledge graphs, grounding, and citations.

## If you want to create an AI agent

Work mainly in Layer 6: Orchestration and Agents.

Typical activities include planning, tool calling, memory, task decomposition, routing, review steps, and workflow control.

## If you want to create a user-facing tool

Work mainly in Layer 7: Application and Experience.

Typical activities include interface design, workflow integration, feedback capture, reporting, dashboards, and user guidance.

## If you want to decide where the system should run

Work mainly in Layer 3: Compute Infrastructure.

Typical choices include cloud, on-premise, local workstation, private server, or edge deployment.

## If you want to optimise for hardware

Work across Layer 2 and Layer 3.

Typical activities include selecting GPU or CPU runtime, optimising memory use, using quantisation, selecting edge hardware, and managing latency.

## If you want to manage risk and governance

Apply controls across all layers.

Governance should include data quality, model evaluation, traceability, monitoring, user communication, privacy, security, cost, and responsible deployment.