from pydantic import BaseModel, constr
from typing import Optional


class Profile(BaseModel):
    name: constr(strip_whitespace=True, min_length=1, max_length=512)
    about: Optional[constr(strip_whitespace=True,
                           min_length=0, max_length=512)]
