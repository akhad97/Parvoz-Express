from rest_framework.response import Response
from rest_framework import generics, views, status
from .pagination import CustomPagination



class RequestController:

    def get_language(self):
        """
        Public method
        @return: request headers language
        """
        return self.__check_language()

    def __check_language(self):
        """Private method"""
        lang = 'en'
        return lang


class CustomResponse(RequestController):
    success_message: dict = {"uz": "OK", "en": "OK", "ru": "ОК"} 
    error_message: dict = {"uz": "Something went wrong", "en": "Something went wrong", "ru": "Что-то пошло не так"}
    error_text: dict = {"uz": "", "de": "", "en": "", "ru": ""}
    exception: tuple = ""

    def success_response(self, *args, **kwargs):
        lang = self.get_language()
        msg_by_language = self.success_message.get(lang)
        response = {'success': True, 'message': msg_by_language}
        if kwargs:
            response.update({key: kwargs[key] for key in kwargs})
        return Response(response, status=status.HTTP_200_OK)

    def update_error_text(self, catch):
        self.error_text.update(dict.fromkeys(['uz', 'de', 'en', 'ru'], catch))

    def error_response(self):
        lang = self.get_language()
        error_by_language = self.error_text.get(lang, 'uz')
        try:
            message_by_language = self.error_message.get(lang) % error_by_language
        except TypeError:
            message_by_language = self.error_message.get(lang)
        response = {'success': False, 'message': message_by_language}
        if self.exception:
            response['debug'] = self.exception
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class CustomViewMixin(CustomResponse):
    ASC = "id"
    DESC = "-id"

    ORDER_BY = {
        "ASC": ASC,
        "DESC": DESC
    }

    def order_by_lookup(self, by):
        return self.ORDER_BY.get(by, self.DESC)


class CustomAPIView(CustomViewMixin, views.APIView):
    """ CustomAPIView """
    pass


class CustomGenericAPIView(CustomViewMixin, generics.GenericAPIView):
    """ CustomGenericAPIView """
    pass


class CustomCreateAPIView(CustomViewMixin, generics.CreateAPIView):
    """ CustomCreateAPIView """
    pass


class CustomListView(CustomViewMixin, generics.ListAPIView, CustomPagination):
    def list(self, request, *args, **kwargs):
        if not (qs := self.get_queryset()):
            # code = status.HTTP_404_NOT_FOUND

            return Response({"success": False, "message": "Not Found", "results": []})
        result = self.paginated_queryset(qs, request)
        serializer = self.serializer_class(result, many=True)
        response = self.paginated_response(data=serializer.data)
        return Response(response)


class CustomListCreateAPIView(CustomListView, CustomViewMixin, generics.CreateAPIView):
    """ CustomCreateAPIView """
    pass


class CustomDetailView(CustomViewMixin, generics.RetrieveUpdateDestroyAPIView):
    """ Retrieve Update Delete API View """    
    pass




    