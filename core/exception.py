from rest_framework.views import exception_handler
from rest_framework.response import Response


def api_exc_handler(exc, context):
    """ Program that is executed when an exception is raised
    in current processing.
    """
    response = exception_handler(exc, context);
    if response is not None:
        return response;
    else:
        # exec_list = str(exc).split('DETAIL: ');
        # return Response({'error_message': exec_list[-1]}, status=400);
        return Response({'error_message': (0xFF, list(exc.args))}, status=503);


pass;
