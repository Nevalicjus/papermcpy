import papermcpy, asyncio

async def main(name):
     proj = await papermcpy.proj(name)
     for ver in proj.versions:
             v = await papermcpy.version(name, ver)
             print(f"Builds for {proj.name}'s version {v.version}: {v.builds}")

asyncio.run(main("paper"))
