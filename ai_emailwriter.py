import requests
def genrate_email(sender_name,reciver,purpose,keypoint,tone):
    prompt = f"""You are an AI Email Writer. Create a complete Email using the following information.
    Sender Name: {sender_name}
    Receipenet Name: {reciver}
    purpose: {purpose}
    Key points: {keypoint}
    Tone: {tone}

    Instructions: Create a suitable subject.
    Include a greeting. Write a clear email.
    Use the provided key points. Do not invent information. Keep the mail consize.
    Include a professional closing, Sign using the snder name. Return only the email"""

    url="http://localhost:11434/api/generate"
    data={
    "model":"llama3.2:3b",
    "prompt": prompt,
    "stream":False}
    response=requests.post(url,json=data)
    result=response.json()
    return result["response"]

print("===================")
print("AI EMAIL WRITER")
print("===================")
sender_name=input("Your name: ")
reciver=input("Recipienet: ")
purpose=input("Purpose: ")
keypoint = input("key point: ")
tone = input("tone: ")
email = genrate_email(sender_name,reciver,purpose,keypoint,tone)
print("===================")
print("genrate_email")
print("===================")
print(email)
with open("genrate_email.txt","w",encoding="utf-8") as file:
    file.write(email)
print("\nemail genrated to .txt")