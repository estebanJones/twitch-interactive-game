from python_graphql_client import GraphqlClient


def create_variables(word, shortId, playerId):
    return {
        "word": word,
        "shortId": shortId,
        "playerId": playerId,
        "accessToken": "",
        "lang": "fr"
    }

def create_query():
    return """
        mutation TryWord($shortId: ID!, $word: String!, $playerId: ID!, $lang: String!, $accessToken: String) {
            tryWord(
                shortId: $shortId
                word: $word
                playerId: $playerId
                lang: $lang
                accessToken: $accessToken
            ) {
                word
                validation
                wordExists
                hasFoundWord
                mask
                score
                __typename
            }
        }
    """



def check_word_if_correct(word, shortId, playerId):
    client = GraphqlClient(endpoint = "https://www.tusmo.xyz/graphql?opname=TryWord")
    v = create_variables(word, shortId, playerId)
    q = create_query()
    return client.execute(query=q, variables=v, operation_name="TryWord")