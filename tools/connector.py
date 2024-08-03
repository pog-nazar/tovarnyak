def connect(short_desc, desc, specifications, price=0):
    from groq import Groq

    while len(desc) > 700:
        client = Groq(
            api_key="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",
        )

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"Скороти цей текст, повинно бути не більше 700 символів не втрачаючи змісту, ось текст: {desc}",
                }
            ],
            model="llama3-groq-70b-8192-tool-use-preview",
        )

        desc = chat_completion.choices[0].message.content

    description = f"🔥<b>{price}👍\n\n{short_desc}</b>\n\n{desc}\n\n"

    for name, spec in specifications.items():
        description += f"<b>● {name}: {spec}</b>\n"

    # max 1024 symbols
    return description
