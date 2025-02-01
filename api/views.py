from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime
import pytz


@api_view(["GET"])
def get_info(request):
    data = {
        "email": "sodiqramon0@gmail.com",
        "current_datetime": datetime.now(pytz.utc).isoformat(),
        "github_url": "https://github.com/lanxCity/Stage0_Project1_hng_api",
    }
    return Response(data)
