cd C:\Documents\Projects
.personalenv\Scripts\Activate.ps1
# Get ip address - on git bach
ipconfig
copy and paste the IPv4 Address in my-cycle-app\utils\trainingSuggester.ts

cd personal\Fast_like_a_girl
# Activate backend
cd app
uvicorn main:app --host 0.0.0.0 --port 8000

# Activate frontend
cd my-cycle-app
npx expo start