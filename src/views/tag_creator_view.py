from src.views.http_types.http_resquest import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.tag_creator_controller import TagCreatorController

class TagCreatorView:
    '''
        Interate with http
    '''
    def validate_and_create(self, http_request:HttpRequest) -> HttpResponse:
        tag_creator_controller = TagCreatorController()

        body = http_request.body
        product_code = body["product_code"]
        response = tag_creator_controller.create(product_code)

        #business logic
        print("In the view")

        
        return HttpResponse(status_code=200, body=response)