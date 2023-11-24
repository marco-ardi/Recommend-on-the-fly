from starlette.applications import Starlette
from starlette.responses import JSONResponse
from model import create_model, generate_recommendation

model = create_model()
app = Starlette()

@app.route("/{user_id}", methods=['GET'])
async def say_hello(request):
    user_id = request.path_params['user_id']  

    recommendation = generate_recommendation(model, user_id)

    return JSONResponse({'recommendations': recommendation})