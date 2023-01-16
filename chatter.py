import openai
import os


class Chatter:
    openai.api_key = "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"

    start_sequence = "\nAI:"
    restart_sequence = "\nHuman: "

    
    def __init__(self):
        """Chatter is a wrapper of acheong08's excellent Reverse Engineered ChatGPT"""
        
        self.api_key = "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"
        return None

    def get_response(self, prompt):
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
        )

        return response.choices[0].text

    def parse_job(self, job):
        """Creates a prompt from a job dict

        Parameters
        ----------
        job : dict
            expects a job dict as defined in app.py
            {
                "sender": sender,
                "recipient": recipient,
                "subject": subject,
                "topic": topic,
                "tone": tone,
            }
        """
        prompt = "An example of ".format(tone=job["tone"])

        if job["tone"] in ["excited", "angry"]:
            prompt += "an %s email " % job["tone"]
        elif job["tone"] in ["happy", "sad"]:
            prompt += "a %s email " % job["tone"]
        else:  # includes "neutral"
            prompt += "an email "
        if job["sender"] != "":
            prompt += "from %s " % job["sender"]
        if job["recipient"] != "":
            prompt += "to %s " % job["recipient"]
        if job["subject"] != "":
            prompt += "with the subject line '%s' " % job["subject"]
        if job["topic"] != "":
            prompt += "about %s " % job["topic"]

        while prompt[-1] == " ":
            prompt = prompt[:-1]
        return prompt

    def email_from_job(self, job):
        """Given a job dict, generates an email.

        Parameters
        ----------
        job : dict
            expects a job dict as defined in app.py
            {
                "sender": sender,
                "recipient": recipient,
                "subject": subject,
                "topic": topic,
                "tone": tone,
            }
        """
        prompt = self.parse_job(job)
        message = self.get_response(prompt)
        return message
