def isMatch(item, slugList):
    itemSlugList = item.slug.split('-')

    result = True

    for n in range(min(len(itemSlugList), len(slugList))):
        if itemSlugList[n] == slugList[n]:
            continue
        else:
            if n == len(slugList):
                break
            else:
                result = False

    if len(itemSlugList) > len(slugList) + 1:
        result = False

    return result



def urlHandler(slug, queryset):
    result = []

    slugList = slug.split('-')

    for item in queryset:
        if isMatch(item, slugList):
            result.append(item)
    
    return result
