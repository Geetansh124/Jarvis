<div align="center">

<img src="https://shieldcn.dev/header/gradient.svg?title=J.A.R.V.I.S.&subtitle=Voice-enabled%20bilingual%20Django%20assistant&accent=%2322c55e&mode=dark" alt="Jarvis banner" width="100%" />

![Python](https://shieldcn.dev/badge/python-django-092E20.svg?logo=django&variant=secondary)
![Groq](https://shieldcn.dev/badge/LLM-Groq-f55036.svg?variant=secondary)
![Stars](https://shieldcn.dev/github/stars/Geetansh124/Jarvis.svg?variant=outline)

**A Django assistant prototype that sends prompts to Groq and supports browser-based speech input and spoken responses.**

[Source](https://github.com/Geetansh124/Jarvis) · [Issues](https://github.com/Geetansh124/Jarvis/issues)

</div>

## Features in the current code

- Django pages and JSON request handling for assistant prompts.
- Groq client integration configured with GROQ_API_KEY.
- Browser Web Speech APIs for voice input and speech synthesis; support and microphone access vary by browser.
- A Django ChatHistory model for local conversation records.

~~~mermaid
flowchart LR
  B[Browser text or speech] --> D[Django view]
  D --> G[Groq API]
  G --> D
  D --> B
  D --> DB[(Local Django database)]
~~~

## Run locally

From the repository root, create and activate a Python virtual environment. Install dependencies:

~~~bash
python -m pip install -r requirements.txt
~~~

Set GROQ_API_KEY in your shell or a local .env file that is not committed. Then run:

~~~bash
python manage.py migrate
python manage.py runserver
~~~

Open http://127.0.0.1:8000. Text input is the fallback when browser speech features are unavailable.

## Configuration and limitations

- Responses require a valid Groq API key, network access, and an available model configured in the code.
- Do not commit .env, API keys, or real conversation history. Review Django settings before deployment; runserver is for local development.
- Speech recognition is browser-dependent and may be processed by the browser's speech service.
- Treat generated answers as suggestions and verify important information.
