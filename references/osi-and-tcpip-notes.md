# OSI and TCP/IP Reference Notes

This repository uses the OSI and TCP/IP models as inspiration for layered architectural thinking.

## OSI model

The OSI model is commonly presented as seven layers:

1. Physical
2. Data Link
3. Network
4. Transport
5. Session
6. Presentation
7. Application

The value of the OSI model is separation of concerns. Each layer has a clear responsibility, and the model helps engineers diagnose where a communication problem belongs.

## TCP/IP model

The TCP/IP model is often presented as a more implementation-oriented model with fewer groups, commonly including:

1. Link
2. Internet
3. Transport
4. Application

## How this repository uses the idea

The AI Architecture Stack does not claim that AI systems are the same as networking systems. It borrows the educational value of layered thinking. The goal is to make AI system design easier to understand by separating physical resources, hardware, infrastructure, data, models, orchestration, applications, and governance.

## Suggested formal references

- ISO/IEC 7498-1: Information technology - Open Systems Interconnection - Basic Reference Model
- RFC 1122: Requirements for Internet Hosts - Communication Layers
- RFC 1123: Requirements for Internet Hosts - Application and Support