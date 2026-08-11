import django
import groq
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ChatHistory
from groq import Groq
from dotenv import load_dotenv
from pathlib import Path
import json, datetime, random, os

# Load .env file

load_dotenv(Path(__file__).resolve().parent.parent / ".env")


def get_groq_client():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key or api_key == "gsk_dummyapikey":
        return None
    return Groq(api_key=api_key)


# Main page


def index(request):
    return render(request, "index.html")


# Jarvis logic


@csrf_exempt
def ask_jarvis(request):
    if request.method == "POST":
        data = json.loads(request.body)
        command = data.get("command", "").strip()
        cmd = command.lower()

        # Hello
        if any(w in cmd for w in ["hello", "hi", "namaste", "hey"]):
            response = (
                "Hello Sir! How can I help you?"
                if any(w in cmd for w in ["hello", "hi", "hey"])
                else "Namaste Sir! Kaise madad kar sakta hoon?"
            )

        # Groq AI — everything else
        else:
            client = get_groq_client()
            if not client:
                response = "Sir, my systems are offline. Please configure my GROQ_API_KEY in the Render dashboard."
            else:
                try:
                    res = client.chat.completions.create(
                        model="llama-3.1-8b-instant",
                        messages=[
                            {
                                "role": "system",
                                "content": (
                                    "You are JARVIS, an AI assistant like from Iron Man. "
                                    "Always start your reply with 'Sir,'. "
                                    "If the user writes in Hindi, reply in Hindi. "
                                    "If the user writes in English, reply in English. "
                                    "Keep answers short and helpful — max 3-4 sentences."
                                ),
                            },
                            {"role": "user", "content": command},
                        ],
                        max_tokens=300,
                    )
                    response = res.choices[0].message.content
                except Exception as e:
                    response = f"Sir, something went wrong: {str(e)}"

        ChatHistory.objects.create(user_message=command, jarvis_response=response)
        return JsonResponse({"response": response})

    return JsonResponse({"error": "POST request required"})
