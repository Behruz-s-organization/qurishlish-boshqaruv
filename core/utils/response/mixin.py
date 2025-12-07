# rest framework
from rest_framework.response import Response
from rest_framework import status


class ResponseMixin:
    SUCCESS = "success"  # 200
    FAILURE = "failure"  # 400
    ERROR = "error"  # 500
    NOT_FOUND = "not_found" # 404
    DELETED = "deleted" # 204
    CREATED = "created" # 201

    @classmethod
    def success_response(cls, data=None, message=None):
        """
        Docstring for success_response
        
        :param cls: Description
        :param data: Description
        :param message: Description
        """
        response_data = {
            "status_code": status.HTTP_200_OK,
            "status": cls.SUCCESS,
        }
        if message is not None:
            response_data['message'] = message
        if data is not None:
            response_data['data'] = data
        return Response(response_data, status=response_data["status_code"])
    
    @classmethod
    def failure_response(cls, data=None):
        """
        Docstring for failure_response
        
        :param cls: Description
        :param data: Description
        :param message: Description
        """
        response_data = {
            "status_code": status.HTTP_400_BAD_REQUEST, 
            "status": cls.FAILURE
        }
        response_data["message"] = "Kiritayotgan malumotingizni tekshirib ko'ring"
        if data is not None:
            response_data["data"] = data
        return 
    
    @classmethod
    def not_found_response(cls, data=None, message=None):
        """
        Docstring for not_found_response
        
        :param cls: Description
        :param data: Description
        :param message: Description
        """
        response_data = {
            "status_code": status.HTTP_404_NOT_FOUND, 
            "status": cls.NOT_FOUND
        }
        if message is not None:
            response_data["message"] = message
        if data is not None:
            response_data["data"] = data
        return Response(response_data, status=response_data['status_code'])
    
    @classmethod
    def deleted_response(cls,message=None):
        """
        Docstring for deleted_response
        
        :param cls: Description
        :param message: Description
        """

        response_data = {
            "status_code": status.HTTP_204_NO_CONTENT, 
            "status": cls.DELETED
        }
        if message is not None:
            response_data["message"] = message
        return Response(response_data, status=response_data['status_code'])
    
    @classmethod
    def created_response(cls, data=None, message=None):
        """
        Docstring for created_response
        
        :param cls: Description
        :param data: Description
        :param message: Description
        """
        response_data = {
            "status_code": status.HTTP_201_CREATED, 
            "status": cls.CREATED
        }
        if message is not None:
            response_data["message"] = message
        if data is not None:
            response_data["data"] = data
        return Response(response_data, status=response_data['status_code'])
    
    @classmethod
    def error_response(cls, data=None):
        """
        Docstring for error_response
        
        :param cls: Description
        :param data: Description
        :param message: Description
        """
        response_data = {
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR, 
            "status": cls.ERROR
        }
        response_data["message"] = "Xatolik, Iltimos backend dasturchiga murojaat qiling"

        if data is not None:
            response_data["data"] = data

        return Response(response_data, status=response_data["status_code"])