from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchRank, SearchQuery


from goods.models import Products

# Реализация поиска
def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    
    vector = SearchVector("name", "description")
    query = SearchQuery(query)
    
    Products.objects.annotate(rank=SearchRank(vector, query)).order_by("-rank")
    

    

    # # Реализация поиска по словам
    # keywords = [word for word in query.split() if len(word) > 2]

    # q_objects = Q()

    # #
    # for token in keywords:
    #     # |= или равно
    #     q_objects |= Q(description__icontains=token)
    #     q_objects |= Q(name__icontains=token)


    # return Products.objects.filter(q_objects)



