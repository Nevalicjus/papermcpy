import paperpy
import asyncio

async def test(name):
     proj = await paperpy.proj(name)
     for ver in proj.versions:
             v = await paperpy.version(name, ver)
             print(f"Builds for {proj.name}'s version {v.version}: {v.builds}")

asyncio.run(test("paper"))
