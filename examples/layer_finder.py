"""Simple layer finder for the AI Architecture Stack."""

LAYERS = {
    "algorithm": "Layer 5 - Model and Learning",
    "model": "Layer 5 - Model and Learning",
    "rag": "Layer 4 - Data and Knowledge",
    "data": "Layer 4 - Data and Knowledge",
    "agent": "Layer 6 - Orchestration and Agents",
    "tool": "Layer 6 - Orchestration and Agents",
    "app": "Layer 7 - Application and Experience",
    "ui": "Layer 7 - Application and Experience",
    "cloud": "Layer 3 - Compute Infrastructure",
    "on premise": "Layer 3 - Compute Infrastructure",
    "edge": "Layer 2 - Chips and Accelerators",
    "gpu": "Layer 2 - Chips and Accelerators",
    "power": "Layer 1 - Physical Foundation",
}


def find_layer(goal):
    text = goal.lower().replace("-", " ")
    for keyword, layer in LAYERS.items():
        if keyword in text:
            return layer
    return "Cross-layer decision"


if __name__ == "__main__":
    goals = [
        "develop a new algorithm",
        "build a RAG system",
        "create an agent with tools",
        "deploy on premise",
        "run on edge hardware",
    ]
    for goal in goals:
        print(goal, "=>", find_layer(goal))
