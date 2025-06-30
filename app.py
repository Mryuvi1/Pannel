from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Facebook Token Checker | YUVI</title>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap" rel="stylesheet">
  <style>
    /* Styles omitted here for brevity – include the full CSS block from your modern template */
    /* Your long CSS goes here */
  </style>
</head>
<body>
  <div class="container">
    <h1>Facebook Token Checker</h1>
    <form method="POST">
      <div class="form-group">
        <label for="token">Enter Access Token</label>
        <textarea name="access_token" id="token" placeholder="Paste your token here..." required>{{ token if token else '' }}</textarea>
      </div>
      <button class="btn" type="submit">Check Token</button>
    </form>

    {% if result %}
      <div class="result {{ 'success' if success else 'error' }}">
        <p>{{ result }}</p>
        {% if user_data %}
          <div class="token-info">
            {% if user_data.picture %}
              <img src="{{ user_data.picture.data.url }}" class="profile-pic" alt="Profile Picture" />
            {% endif %}
            <p><strong>Name:</strong> {{ user_data.name }}</p>
            <p><strong>ID:</strong> {{ user_data.id }}</p>
          </div>
        {% endif %}
      </div>
    {% endif %}
  </div>
  <footer>❤️ Developed by MR YUVI | Facebook Token Checker ❤️</footer>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    success = False
    user_data = None
    token = ""

    if request.method == "POST":
        token = request.form.get("access_token")
        fb_url = f"https://graph.facebook.com/me?fields=id,name,picture&access_token={token}"

        try:
            response = requests.get(fb_url)
            data = response.json()

            if "id" in data:
                success = True
                result = f"✅ Token is Valid: Welcome, {data['name']}!"
                user_data = data
            else:
                result = "❌ Invalid or expired token."
        except Exception as e:
            result = f"❌ Error while checking token: {str(e)}"

    return render_template_string(HTML_TEMPLATE, result=result, success=success, user_data=user_data, token=token)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
