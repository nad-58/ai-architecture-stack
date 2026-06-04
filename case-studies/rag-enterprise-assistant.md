# Case Study: Enterprise RAG Assistant

## Use case

An organisation wants an assistant that answers questions using internal documents and provides citations.

## Relevant layers

| Layer | Role |
|---:|---|
| 7 | User interface, feedback, citations, workflow integration |
| 6 | Query routing, prompt flow, tool use, answer review |
| 5 | Model selection and answer quality evaluation |
| 4 | Document sources, chunking, embeddings, vector database, retrieval |
| 3 | Cloud, on-premise, or private deployment |

## Architecture questions

- What documents are allowed to be used?
- How are documents processed and updated?
- Which vector database or retrieval method is suitable?
- Should the model be hosted externally, privately, or locally?
- How are citations shown to the user?
- How will the organisation monitor answer quality and user feedback?

## Key trade-off

The main trade-off is between ease of deployment, data control, retrieval quality, cost, and user trust.