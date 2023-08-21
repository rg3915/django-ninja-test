from ninja import NinjaAPI
from backend.crm.api import router as crm_router

api = NinjaAPI()

api.add_router('/crm/', crm_router)