# Summarizer

Summarizer is a helper tool built with [ElevenLabs](https://elevenlabs.io/) and [Cohere](https://cohere.com/) to help summarize long texts and listen to a synthesis of them.
The idea is to help people save time when understanding a large volume of information, in a simple and agile way.

## Licence
[MIT](./LICENCE)

## How works

1. Get API key from [Cohere](https://cohere.com/) and [ElevenLabs](elevenlabs.io)
2. Install [Streamlit](https://streamlit.io/) or use Streamlit Cloud.
3. Install all libraries in [requirements.txt](./requirements.txt).
4. Add these secrets in Streamlit:
   - _cohere_api_key_: The API key from Cohere.
   - _elevenlabs_api_key_: The API key from ElevenLabs.
5. Run the web app (in Streamlit Cloud just wait to compile automatically).

Created by [Néstor Nicolás Campos Rojas](https://www.linkedin.com/in/nescampos/)
