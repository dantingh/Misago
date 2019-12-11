from typing import Optional

from ..loaders import load_user
from ..types import GraphQLContext, User


async def get_user(context: GraphQLContext, user_id: int) -> Optional[User]:
    user = await load_user(context, user_id)
    if not user or user.is_deactivated:
        return None
    return user
