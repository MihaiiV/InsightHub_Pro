from pydantic import BaseModel

class ResearchResult(BaseModel):
    topic: str
    summary: str
    source_count: int

# Aceasta este o simulare a logicii agentului
def get_research_data(topic: str) -> ResearchResult:
    return ResearchResult(
        topic=topic,
        summary=f"Analiză detaliată despre {topic} folosind Search Grounding.",
        source_count=5
    )