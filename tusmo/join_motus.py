from python_graphql_client import GraphqlClient


def create_variables(shortId, playerId):
    # "playerId": "1593d7d09ae39510b762e6b001"
    return {
        "accessToken": "",
        "playerId": playerId,
        "playerName": "null",
        "shortId": shortId
    }

def create_query():
    return """
        mutation JoinMotus($shortId: ID!, $playerId: ID!, $playerName: String, $accessToken: String) {
            joinMotus(
                shortId: $shortId
                playerId: $playerId
                playerName: $playerName
                accessToken: $accessToken
            ) {
                shortId
                type
                state
                lang
                currentRound
                isStarted
                isEnded
                playersNumber
                rounds {
                        _id
                        firstLetter
                        length
                        __typename
                }
                me {
                    _id
                    name
                    hasWon
                    currentRound
                    state
                    rounds {
                            score
                            hasFoundWord
                            tries {
                                    word
                                    validation
                                    wordExists
                                    hasFoundWord
                                    mask
                                    __typename
                             }
                            __typename
                    }
                     __typename
                }
                __typename
            }
        }
    """


def join_motus(shortId, playerId):
    client = GraphqlClient(endpoint = "https://www.tusmo.xyz/graphql?opname=JoinMotus")
    v = create_variables(shortId, playerId)
    q = create_query()
    return client.execute(query=q, variables=v, operation_name="JoinMotus")
    