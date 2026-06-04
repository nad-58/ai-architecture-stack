# Deployment Patterns

AI architecture decisions depend strongly on where the system runs. A model that works well in a notebook may not be suitable for a private production environment, embedded device, or real-time application.

## Cloud deployment

Cloud deployment is useful when the system needs scalability, managed services, rapid experimentation, or access to large models and GPUs.

Advantages:

- fast setup;
- scalable compute;
- managed storage and monitoring;
- access to hosted model services.

Challenges:

- ongoing cost;
- data governance requirements;
- vendor dependency;
- latency for some applications.

## On-premise deployment

On-premise deployment is useful when organisations require strong control over data, infrastructure, and internal governance.

Advantages:

- stronger local control;
- easier alignment with internal infrastructure policy;
- useful for sensitive data;
- predictable ownership model.

Challenges:

- high upfront cost;
- maintenance burden;
- hardware refresh cycles;
- need for internal expertise.

## Local deployment

Local deployment means running on a workstation, laptop, local server, or small private environment.

Advantages:

- useful for prototyping;
- can support offline work;
- suitable for smaller models;
- good for education and experimentation.

Challenges:

- limited compute;
- difficult scaling;
- hardware constraints;
- less suitable for heavy multi-user workloads.

## Edge deployment

Edge deployment means running AI close to sensors, devices, machines, or users.

Advantages:

- low latency;
- reduced dependency on internet connectivity;
- useful for industrial, robotics, medical, and remote systems;
- can reduce data transfer.

Challenges:

- limited compute and memory;
- model compression may be needed;
- hardware-specific optimisation;
- harder fleet management.

## Choosing a pattern

| Requirement | Likely option |
|---|---|
| Large model, rapid scale | Cloud |
| Sensitive internal data | On-premise or private cloud |
| Offline prototype | Local |
| Low latency near sensors | Edge |
| Regulated environment | On-premise, private cloud, or carefully governed cloud |
| Cost-sensitive small system | Local or small model deployment |

The best option depends on data sensitivity, latency, cost, scale, hardware availability, and governance requirements.