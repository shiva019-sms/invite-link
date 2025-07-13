from connectors_peopledatalabs import get_person_data
from models import PersonRequest, PersonResponse, FamilyMember, Education, Experience, Connection, Investment

async def aggregate_person_info(request: PersonRequest) -> PersonResponse:
    pdl_data = await get_person_data(request.full_name, request.company)

    # Map PDL data to response fields (expand as needed)
    name = pdl_data.get("full_name", request.full_name)
    aliases = pdl_data.get("aliases", [])
    dob = pdl_data.get("birth_date")
    age = pdl_data.get("age")

    # Education
    education = []
    for edu in pdl_data.get("education", []):
        education.append(Education(
            school=edu.get("school"),
            degree=edu.get("degree"),
            year=edu.get("graduation_year")
        ))

    # Professional background
    professional_background = []
    for exp in pdl_data.get("experience", []):
        professional_background.append(Experience(
            position=exp.get("title"),
            company=exp.get("company"),
            years=exp.get("start_date")
        ))

    # Family (spouse/children)
    spouse = None
    children = []
    for rel in pdl_data.get("relationships", []):
        if rel.get("type") == "spouse":
            spouse = FamilyMember(name=rel.get("name"), age=rel.get("age"))
        elif rel.get("type") == "child":
            children.append(FamilyMember(name=rel.get("name"), age=rel.get("age")))

    # Key connections (not always available)
    key_connections = []
    for conn in pdl_data.get("connections", []):
        key_connections.append(Connection(name=conn.get("name"), relation=conn.get("relation")))

    # Interests/Investments (not always available)
    interests_investments = []
    for inv in pdl_data.get("interests", []):
        interests_investments.append(Investment(area=inv.get("name")))

    return PersonResponse(
        name=name,
        aliases=aliases,
        dob=dob,
        age=age,
        spouse=spouse,
        children=children,
        education=education,
        professional_background=professional_background,
        private_banker=None,
        icici_bank_relationship=None,
        key_connections=key_connections,
        interests_investments=interests_investments
    )