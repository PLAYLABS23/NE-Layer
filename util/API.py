from openai import OpenAI

class LMM:
    def __init__(self, api_key: str, model: str = "gpt-4o-mini") -> None:
        self.model = model
        self.client = OpenAI(api_key=api_key)
        self.history = [
            {
                "role": "system",
                "content":
                """
                    당신의 이름은 네오입니다.
                    착용형 AI 디바이스에 내장되며, 사용자 질문에 올바른 대답을 해야합니다.
                    이 기기를 사용하는 사람은 장애인 일 수도, 비장애인 일 수도 있습니다.
                    사용자에겐 친근하게 접근해야하며, 사용자와 함께하는 디바이스로써
                    거부감이 느껴지면 안됩니다. 또한, 오디오를 통해, 텍스트를 전달하기 때문에
                    명확하고, 짧고 정확성 있게 대답해야합니다.
                """,
            }
        ]

    def text_request(self, message: str):
        try:
            self.history.append({"role" : "user", "content" : f"{message}"})
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.history
            )
            response = response.choices[0].message.content
            self.history.append({"role" : "assistant", "content" : f"{response}"})
            return response
        except Exception as e:
            return "문제가 발생했어요."
        
