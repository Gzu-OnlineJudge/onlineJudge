def get_data(obj, serializer, dataList=[], context={}):
    nowFields = serializer.Meta.fields
    if not dataList:
        dataList = nowFields
    serializer.Meta.fields = dataList
    data = serializer(obj, context=context, many=True).data
    serializer.Meta.fields = nowFields
    return data