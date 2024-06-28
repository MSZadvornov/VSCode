from apis.organizations.organization_api import OrganizationApi
import pytest
from pprint import pprint
import jsonschema
from allure import step

@step("Создание")
def test_create(get_base_url_ELK, get_auth_token):
    """
    Создание
    """
    organization = OrganizationApi(host=get_base_url_ELK, token=get_auth_token)

    response = organization.create_organization()

    pprint(response.json()["data"]["id"])

    assert response.status_code == 200, "Не удалось создать организацию"


@step("Удаление")
def test_delete(get_base_url_ELK, get_auth_token):
    """
    Удаление
    """
    organization = OrganizationApi(host=get_base_url_ELK, token=get_auth_token)
    
    # Получение id организации для дальнейшего удаления
    organization_id = organization.create_organization().json()["data"]["id"]

    # Удаление организации
    response = organization.delete_organization(organization_id)

    assert response.status_code == 200, "Удаление прошло успешно"
    assert response.json()['errors'] is None , "Удаление прошло успешно"
    # Проверка схемы ответа 
    schema = {
        "type": "object",
        "properties": {
            "errors": {"type": "null"},
            "data": {"type": "array", "items": {"items": {}}},
            "requestId": {"type": "string"},
        },
        "required": ["errors", "data", "requestId"],
    }

    try:
        jsonschema.validate(response.json(), schema)
    except jsonschema.exceptions.ValidationError as elem:
        print(f"Ошибка валидации: {elem}")

    if __name__ == "__main__":
        pytest.main()


