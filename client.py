from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

transport = AIOHTTPTransport(url="http://localhost:8000/graphql")
client = Client(transport=transport, fetch_schema_from_transport=True)

async def get_resonator(name: str):
    async with client as session:
        query = gql(
            f"""
            query {{
                resonator(name: "{name}") {{
                    name
                    attribute
                    weaponType
                    nation
                    stories {{
                        title
                        content
                    }}
                }}
            }}
            """
        )
        result = await session.execute(query)
        return result

async def get_echo(name: str):
    async with client as session:
        query = gql(
            f"""
            query {{
                echo(name: "{name}") {{
                    name
                    attribute
                    enemyClass
                    description
                }}
            }}
            """
        )
        result = await session.execute(query)
        return result

async def get_resonators():
    async with client as session:
        query = gql(
            """
            query {
                resonators
            }
            """
        )
        result = await session.execute(query)
        return result

async def get_echoes():
    async with client as session:
        query = gql(
            """
            query {
                echoes
            }
            """
        )
        result = await session.execute(query)
        return result
