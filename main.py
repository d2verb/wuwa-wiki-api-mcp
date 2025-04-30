from mcp.server.fastmcp import FastMCP
import client

mcp = FastMCP("wuwa-wiki-api-mcp")

@mcp.tool()
async def get_resonator(name: str):
    """共鳴者の情報を取得します。

    Args:
        name (str): 共鳴者の名前

    Returns:
        str: 共鳴者の情報
    """
    result = await client.get_resonator(name)
    resonator = result["resonator"]
    output = f"""
名前: {resonator["name"]}
属性: {resonator["attribute"]}
武器種: {resonator["weaponType"]}
出身: {resonator["nation"]}

ストーリー:
"""
    for story in resonator["stories"]:
        output += f"{story["title"]}: {story["content"]}\n"
    return output

@mcp.tool()
async def get_echo(name: str):
    """音骸の情報を取得します。

    Args:
        name (str): 音骸の名前

    Returns:
        str: 音骸の情報
    """
    result = await client.get_echo(name)
    output = f"""
名前: {result["echo"]["name"]}
属性: {result["echo"]["attribute"]}
クラス: {result["echo"]["enemyClass"]}
説明: {result["echo"]["description"]}
"""
    return output

@mcp.tool()
async def get_resonators():
    """共鳴者の一覧を取得します。

    Returns:
        str: 共鳴者の一覧
    """
    result = await client.get_resonators()
    output = "```"
    for resonator in result["resonators"]:
        output += f"- {resonator}\n"
    output += "```"
    return output

@mcp.tool()
async def get_echoes():
    """音骸の一覧を取得します。

    Returns:
        str: 音骸の一覧
    """
    result = await client.get_echoes()
    output = "```"
    for echo in result["echoes"]:
        output += f"- {echo}\n"
    output += "```"
    return output

if __name__ == "__main__":
    mcp.run(transport="stdio")