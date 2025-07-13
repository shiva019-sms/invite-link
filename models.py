from pydantic import BaseModel
from typing import List, Optional

class FamilyMember(BaseModel):
    name: str
    age: Optional[int] = None

class Education(BaseModel):
    school: str
    degree: Optional[str] = None
    year: Optional[int] = None

class Experience(BaseModel):
    position: str
    company: str
    years: Optional[str] = None

class Connection(BaseModel):
    name: str
    relation: Optional[str] = None

class Investment(BaseModel):
    area: str
    investment: Optional[str] = None

class PersonRequest(BaseModel):
    full_name: str
    company: Optional[str] = None

class PersonResponse(BaseModel):
    name: str
    aliases: List[str] = []
    dob: Optional[str] = None
    age: Optional[int] = None
    spouse: Optional[FamilyMember] = None
    children: List[FamilyMember] = []
    education: List[Education] = []
    professional_background: List[Experience] = []
    private_banker: Optional[str] = None
    icici_bank_relationship: Optional[str] = None
    key_connections: List[Connection] = []
    interests_investments: List[Investment] = []