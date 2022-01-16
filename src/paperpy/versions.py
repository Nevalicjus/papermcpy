from .utils import paper_request

__all_ = (
    'version',
    'build',
    'family',
    'family_builds'
)

async def version(proj: str, ver: str):
    return await paper_request(type= "get", url = f"projects/{proj}/versions/{ver}")

async def build(proj: str, ver: str, build: str):
    return await paper_request(type= "get", url = f"projects/{proj}/versions/{ver}/builds/{build}")

async def family(proj: str, family: str):
    return await paper_request(type= "get", url = f"projects/{proj}/version_group/{family}")

async def family_builds(proj: str, family: str):
    return await paper_request(type= "get", url = f"projects/{proj}/version_group/{family}/builds")
