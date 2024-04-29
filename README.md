# GitHub API Integration

This Django application integrates with the GitHub API to search for repositories based on a keyword provided by the user.

## Setup and Usage

1. Clone the repository:<br>
>git clone https://github.com/MarcinGralka/api_github.git

2. Create virtual environment:<br>
>python3 -m venv "virtual environment name"<br>
source "virtual environment name"/bin/activate

3. Install the required packages:
>pip install -r packages.txt

4. Run the Django development server:
>python manage.py runserver

5. Open your web browser and go to http://localhost:8000/github/search/?keyword=<keyword> to search for repositories. Replace `<keyword>` with your search term.

6. To use authorization token you need to change it in the `views.py` file
## API Endpoint

### Search Repositories
- **URL:** /github/search/
- **Method:** GET
- **Parameters:**
- `keyword`: The keyword to search for repositories

### Tests
Type this command to run tests:
>python manage.py test
