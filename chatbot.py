import os
from openai import ChatCompletion
from openai.error import OpenAIError


api_key = os.getenv("OPENAI_API_KEY")

completion = ChatCompletion(api_key)

predefined_responses = {
    "Quel est le jeu le plus populaire en ce moment ?": "Le jeu le plus populaire en ce moment est Fortnite, avec des millions de joueurs actifs chaque jour.",
    "Quels sont les meilleurs jeux de rôle (RPG) sortis cette année ?": "Parmi les meilleurs RPG sortis cette année, on trouve Cyberpunk 2077, Final Fantasy VII Remake et Persona 5 Royal.",
    "Quels sont les jeux indépendants les plus appréciés par les joueurs ?": "Certains des jeux indépendants les plus appréciés incluent Hollow Knight, Celeste et Stardew Valley."
}

def chatbot_jeux_video():
    print("Bienvenue dans le chatbot jeux vidéo ! Posez vos questions sur les jeux vidéo.")
    while True:
        question = input("Votre question : ")
        if question in predefined_responses:
            print("La réponse est : " + predefined_responses[question])
        else:
            response = send_question(question)
            print("La réponse est : " + response)

def send_question(question):
    try:
        completion_response = completion.create(
            model="gpt-3.5-turbo",  
            messages=[
                {"role": "system", "content": "Tu es un assistant de jeux vidéos."},
                {"role": "user", "content": question},
            ]
        )

        response = completion_response.choices[0].message.content
        return response
    except OpenAIError as e:
        print("Une erreur s'est produite lors de la communication avec l'API : ", e)
        return "Désolé, une erreur est survenue. Veuillez réessayer plus tard."

if __name__ == "__main__":
    chatbot_jeux_video()
    
