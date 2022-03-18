from fastapi import FastAPI, Response, responses
import uvicorn
from typing import Optional

api = FastAPI()

@api.get('/api/calculate/')
def calculate(x: int, y: int, z: Optional[int] = None):
    # arguments in the function are query strings in the case of get
    if z == 0:
        return Response(
            content="{'error': 0 not allowed for z}",
            media_type="application/json",
            status_code=400
        )
        # alternative: JSONResponse(status_code=, content=)
    value = x + y
    if z: value += z
    result = {
        'value': value
    }
    return result

html_response = (
    "<html><body>"
    "<div><h1>Hello Fast API!</h1></div>"
    "<div><p>Example: <a href='/api/calculate/?x=5&y=2&z=6'>here</a></p></div>"
    "</body></html>"
)

@api.get('/')
def hello_world():
    return responses.HTMLResponse(content=html_response)

uvicorn.run(api, port=8000, host="127.0.0.1", debug=True)

