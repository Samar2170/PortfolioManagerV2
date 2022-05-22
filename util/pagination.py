from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class ViewPaginatorMixin(object):
    min_limit=1
    max_limit=100
    def paginate(self,object_list,page,limit,**kwargs):
        try:
            page=int(page)
            if page<1:
                page=1
        except (ValueError,TypeError):
            page=1

        try:
            limit=int(limit)
            if limit<self.min_limit:
                limit=self.min_limit
            elif limit>self.max_limit:
                limit=self.max_limit
        except (ValueError,TypeError):
            limit=self.min_limit

        paginator=Paginator(object_list,limit)
        try:
            objects=paginator.page(page)
        except PageNotAnInteger:
            objects=paginator.page(1)
        except EmptyPage:
            objects=paginator.page(paginator.num_pages)
        
        data = {
            'next_page': objects.next_page_number() if objects.has_next() else None,
            'data':list(objects)
        }
        return data