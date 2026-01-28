from core.agent_manager import get_research_data

# 1. Definim un subiect de test
subiect = "Inteligenta Artificiala in 2026"

print(f"--- Se ruleaza simularea pentru: {subiect} ---")

# 2. Apelam functia ta
rezultat = get_research_data(subiect)

# 3. Afisam rezultatele in consola
print(f"Subiect: {rezultat.topic}")
print(f"Sumar: {rezultat.summary}")
print(f"Surse gasite: {rezultat.source_count}")

# 4. Demonstram puterea Pydantic (conversie in dictionar)
print(f"\nObiectul validat (JSON): {rezultat.model_dump()}")