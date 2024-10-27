# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]


def write_responses(result):
    print('\n'.join(result))


def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = {}
    for cur_query in queries:
        cur_query_hash = get_hash(cur_query.number)
        # print(cur_query.type, cur_query.number, cur_query_hash)
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            if cur_query_hash not in contacts.keys():
                contacts[cur_query_hash] = [cur_query]
            else:
                exist = False
                for contact in contacts[cur_query_hash]:
                    if contact.number == cur_query.number:
                        exist = True
                        contact.name = cur_query.name
                        break
                if not exist:
                    contacts[cur_query_hash].append(cur_query)

            # print(contacts)

        elif cur_query.type == 'del':
            if cur_query_hash not in contacts.keys():
                continue
            if len(contacts[cur_query_hash]) == 1:
                del contacts[cur_query_hash]
            else:
                cur_query.type = "add"
                if cur_query in contacts[cur_query_hash]:
                    contacts[cur_query_hash].remove(cur_query)
            # print(contacts)
        else:
            response = 'not found'
            if cur_query_hash not in contacts.keys():
                result.append(response)
                # print(contacts)
                continue

            exist = False
            for contact in contacts[cur_query_hash]:
                if contact.number == cur_query.number:
                    exist = True
                    response = contact.name
                    result.append(response)
                    break
            if not exist:
                result.append(response)
            # print(contacts)
    return result


def get_hash(s):
    p = 10000019
    a = 34
    b = 2
    m = 10 ** 5
    return ((a * int(s) + b) % p) % m


if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

