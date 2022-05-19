from portfolio.views import APIViewWithPermission
from rest_framework.response import Response

class UploadFile(APIViewWithPermission):
    
    def post(self, request, *args, **kwargs):
        # import ipdb; ipdb.set_trace()
        files = request.FILES
        try:
            file_names = [f for f in files.keys()]
        except KeyError:
            return Response({'error':'No file found'}, status=400)
        user = request.user
        response_dict=[]
        for name, file in zip(file_names,files.values()):
            created_file = File.objects.create(
                user=user,
                file_path=file_handler(file),
                file_name=file.name,
                category=name,
                format=name.split('.')[-1]
            )
            response_dict.append({'file_name':file.name, 'category':name})
        
        return Response(response_dict, status=201)

