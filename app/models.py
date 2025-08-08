# from pydantic import BaseModel, Field
# from typing import Optional, Dict, Any
# from datetime import datetime

# class NormalizedCall(BaseModel):
#     city: str
#     timestamp: Optional[datetime]
#     incident_type: str
#     location: Optional[Dict[str, Any]]
#     address: Optional[str]
    
#     class Config:
#         extra = "allow"  # Allow additional fields

# class ErrorResponse(BaseModel):
#     detail: str
#     timestamp: datetime = Field(default_factory=datetime.utcnow)



from pydantic import BaseModel,Field
from typing import List, Dict, Any
from datetime import datetime

class EmergencyCallResponse(BaseModel):
    count: int
    data: List[Dict[str, Any]]
    timestamp: datetime = Field(default_factory=datetime.utcnow)