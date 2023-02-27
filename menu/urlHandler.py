def defineLevel(arr):
    result = [{ 
        "data": item,
        "level": len(item["slug"].split('-'))
        } for item in arr] 

    return result


def urlHandler(slug, queryset):

    if slug == None:
        result = [{
            "data": item,
            "level": 0
            } for item in queryset if len(item.slug.split('-')) == 1]

        return result

    
    slug_list = slug.split('-')
    result = queryset.values()
    
    for n in range(len(slug_list)):
        pattern  = slug_list[n]

        new_result = []

        for item in result:
            if item["slug"].find(pattern) >= 0 or len(item["slug"].split('-')) <= n + 1:
                if len(item["slug"].split('-')) <= len(slug_list) + 1:    
                    new_result.append(item)
        
        result = new_result
    
    result.sort(key=lambda result: result["slug"])

    result = defineLevel(result)

    return result
