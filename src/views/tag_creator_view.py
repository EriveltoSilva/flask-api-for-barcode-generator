from src.views.http_types.http_resquest import HttpRequest
from src.views.http_types.http_response import HttpResponse

class TagCreatorView:
    '''
        Interate with http
    '''
    def validate_and_create(self, http_request:HttpRequest) -> HttpResponse:
        body = http_request.body
        product_code = body["product_code"]

        #logica de regra de negocio
        print("In the view")
        #retorn http
        return HttpResponse(status_code=200, body={"status":"very succeful"})