def test_root_endpoint(client):
    # Arrange
    url = "/"

    # Act
    response = client.get(url, follow_redirects=False)

    # Assert
    assert response.status_code == 307  # Temporary Redirect
    assert response.headers["location"] == "/static/index.html"