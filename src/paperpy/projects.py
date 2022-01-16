from .utils import paper_request

__all_ = (
    'proj',
    'projs'
)

async def proj(proj: str):
    return await paper_request(type= "get", url = f"projects/{proj}")

async def projs():
    return await paper_request(type= "get", url = "projects")
