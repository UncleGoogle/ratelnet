import pytest
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

@pytest.mark.django_db
def test_post(client):
    url = reverse('check_content')

    content = SimpleUploadedFile("file.txt", b"file_content")

    response = client.post(url, {'content': content}, format='multipart')

    assert response.status_code == 200
    assert 'ok' in response.json()