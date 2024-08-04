def cut_text(text):
    from groq import Groq

    client = Groq(
        api_key="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",
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Скороти цей текст, повинно бути не більше 700 символів не втрачаючи змісту, ось текст: {text}",
            }
        ],
        model="llama3-groq-70b-8192-tool-use-preview",
    )

    return chat_completion.choices[0].message.content
