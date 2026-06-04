# AI Architecture Stack Compared with OSI and TCP/IP

The AI Architecture Stack is inspired by layered thinking in networking. The OSI model separates network communication into seven conceptual layers. TCP/IP uses a simpler practical grouping. Both models are useful because they help engineers separate concerns and diagnose problems.

This repository uses that idea to explain AI systems. The goal is not to replace OSI or TCP/IP, and not to claim that AI systems are identical to networks. The goal is to give AI developers, product teams, infrastructure teams, and governance teams a shared language.

## Conceptual mapping

| OSI layer | Networking role | AI architecture analogy | AI design question |
|---:|---|---|---|
| 7 | Application | Application and Experience | What does the user need to achieve? |
| 6 | Presentation | Model and Representation | How are inputs transformed into useful outputs? |
| 5 | Session | Orchestration and Agents | How is task state, memory, and tool use coordinated? |
| 4 | Transport | Data and Knowledge | How is information prepared and delivered reliably? |
| 3 | Network | Compute Infrastructure | Where does the system run and how does it scale? |
| 2 | Data Link | Chips and Accelerators | What hardware enables efficient computation? |
| 1 | Physical | Physical Foundation | What physical resources support the system? |

## TCP/IP-style simplified view

A TCP/IP-style view can be simpler for implementation teams:

| TCP/IP-style group | AI architecture group | Included layers |
|---|---|---|
| Application | User value and workflows | Application, orchestration, model behaviour |
| Transport | Information and task reliability | Data, knowledge, retrieval, state management |
| Internet | Runtime and deployment environment | Cloud, on-premise, local, edge, distributed runtime |
| Link | Hardware and physical resources | Chips, accelerators, power, cooling, devices |

## Why the comparison helps

The OSI comparison helps readers understand that AI architecture is not just a model. A production AI system has layers and dependencies. A model may be powerful, but the full system can still fail if the data layer is weak, the orchestration layer is unreliable, the infrastructure layer is too slow, or the application layer does not fit the user workflow.

## Important limitation

The mapping is educational and architectural. It should not be treated as a formal standard or exact equivalence. It is a practical guide for reasoning about AI systems.