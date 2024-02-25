# First, ensure you have langserve.client installed, or install it using pip
# pip install langserve-client

from langserve.client import RemoteRunnable
import json


def translate_to_pirate_speak(text):
    # Initialize the RemoteRunnable with your service URL
    runnable = RemoteRunnable(
        "https://pirate-2e5e15cdca175f9e91229f8ec398dc0f-ffoprvkqsa-uc.a.run.app/pirate-speak"
    )

    # Prepare the request object
    request_object = {"text": text}

    # Execute the request and capture the response
    response = runnable.invoke(request_object)

    # Extracting the pirate speak directly from the response
    pirate_speak = response.content

    # Return the pirate-speak translation
    return pirate_speak


# Example usage:
text_to_translate = "where is my iced coffee?"
pirate_translation = translate_to_pirate_speak(text_to_translate)
print(pirate_translation)
