from fastapi import APIRouter

from src.services.base_service import main_service

router=APIRouter()

@router.get('/')
def main():
    return main_service()