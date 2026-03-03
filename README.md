# Holiday-Management-Agent

1. Create Virtual environment
```
python -m venv venv

```

2. Activate Virtual environment

```
venv\Scripts\Activate.ps1
```

3. Install all required packages 
```
pip install -r requirements.txt
```

4. Push changes to Github
```
git add .
git commit -m "requirements added"
git push origin main 
```

5. Run the template file which will create the required folders

6. Create the Agents and Teams 
7. Write the code in main.py and test it using
```
python main.py
```

8. create the application using html and css 
9. Run the FastAPI Application
```
uvicorn app:app --reload
```
10. In google 
```
localhost:8000
```

## Deploying to Hugging Face Spaces

1. **Create a Hugging Face account** at https://huggingface.co

2. **Create an access token**:
   - Go to https://huggingface.co/settings/tokens
   - Click "New token"
   - Give it a name (e.g., "git-access")
   - Select "Write" access
   - Copy the token (starts with `hf_...`)

3. **Create a new Space**:
   - Go to https://huggingface.co/new-space
   - Enter a Space name
   - Select **Docker** as the SDK
   - Choose a license
   - Click "Create Space"

4. **Install Git LFS** (if not already installed):
```bash
git lfs install
```

5. **Add Hugging Face as remote** (replace USERNAME, TOKEN, and SPACE_NAME):
```bash
git remote add origin https://USERNAME:TOKEN@huggingface.co/spaces/USERNAME/SPACE_NAME
```

6. **Push to Hugging Face**:
```bash
git add .
git commit -m "Deploy to Hugging Face"
git push origin main
```

7. **Add API Key as Secret**:
   - Go to your Space Settings → Variables and secrets
   - Click "New secret"
   - Name: `OPENAI_API_KEY`
   - Value: Your OpenAI API key
   - Save

8. Your app will be live at `https://huggingface.co/spaces/USERNAME/SPACE_NAME`

## Deployment

This app is deployed on Hugging Face Spaces using Docker.
