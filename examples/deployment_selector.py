"""Simple deployment selector for the AI Architecture Stack."""


def select_deployment(data_sensitivity, latency_need, scale_need):
    if latency_need == "high":
        return "Edge or local deployment"
    if data_sensitivity == "high" and scale_need == "high":
        return "Private cloud or on-premise deployment"
    if data_sensitivity == "high":
        return "On-premise or local deployment"
    if scale_need == "high":
        return "Cloud deployment"
    return "Local or small cloud deployment"


if __name__ == "__main__":
    scenarios = [
        ("low", "low", "high"),
        ("high", "low", "medium"),
        ("medium", "high", "low"),
    ]
    for scenario in scenarios:
        print(scenario, "=>", select_deployment(*scenario))
