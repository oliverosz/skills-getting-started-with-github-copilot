
def test_get_activities_returns_data(client):
    response = client.get("/activities")

    assert response.status_code == 200
    data = response.json()
    assert "Chess Club" in data
    assert "participants" in data["Chess Club"]


def test_signup_for_activity_adds_participant(client):
    response = client.post("/activities/Chess Club/signup?email=student@mergington.edu")

    assert response.status_code == 200
    assert response.json()["message"] == "Signed up student@mergington.edu for Chess Club"

    activities_response = client.get("/activities")
    activities = activities_response.json()["Chess Club"]
    assert "student@mergington.edu" in activities["participants"]


def test_unregister_participant_removes_email_from_activity(client):
    response = client.delete("/activities/Chess Club/participants/michael@mergington.edu")

    assert response.status_code == 200
    assert response.json()["message"] == "Unregistered michael@mergington.edu from Chess Club"

    activities_response = client.get("/activities")
    activities = activities_response.json()["Chess Club"]
    assert "michael@mergington.edu" not in activities["participants"]


def test_unregister_participant_returns_404_for_unknown_activity(client):
    response = client.delete("/activities/Unknown Activity/participants/test@example.com")

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"
