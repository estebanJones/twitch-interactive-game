from python_graphql_client import GraphqlClient


def create_variables():
    return {
        "lang": "fr",
        "type": "SOLO"
    }

def create_query():
    return """
        mutation StartMotus($type: String!, $lang: String!) {  
            startMotus(
                type: $type
                lang: $lang
            ) {    
                shortId    
                __typename  
            }
        }
    """


def start_motus():
    client = GraphqlClient(endpoint = "https://www.tusmo.xyz/graphql?opname=StartMotus")
    v = create_variables()
    q = create_query()
    return client.execute(query=q, variables=v, operation_name="StartMotus")