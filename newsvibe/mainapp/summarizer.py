from django.http import JsonResponse
import requests
from decouple import config

def summarize_text(text_to_summarize):
    account_id = config('ACCOUNT_ID')
    api_token = config('API_TOKEN')
    model = '@cf/meta/llama-3-8b-instruct'

    response = requests.post(
        f"https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run/{model}",
        headers={"Authorization": f"Bearer {api_token}"},
        json={
            "messages": [
                {"role": "system", "content": "You are a helpful assistant that summarizes news articles."},
                {"role": "user", "content": f"Please summarize the following news article in 3-4 sentences:\n\n{text_to_summarize}"}
            ]
        }
    )

    if response.status_code == 200:
        summary = response.json().get("result", {}).get("response", "")
        return summary
    else:
        return "Failed to generate summary."


# just an example -> 
text = """After seven hours of rescue efforts, the NDRF has ended its search at the coaching centre in Delhi's Old Rajinder Nagar area where three civil services aspirants died last night when the basement of the building was flooded following heavy rains, officials said on Sunday.

Students held a protest and raised slogans against authorities outside the coaching centre over the deaths in the basement, which according to preliminary probe houses a library.

Deputy Commissioner of Police (central) M Harsha Vardhan said, "NDRF's search operation has ended and three bodies have been recovered. NDRF's rescue operation went on for around seven hours."

Police is looking at CCTV footage to understand the sequence of events, the DCP said.

The bodies of two female students and a male student were retrieved from the site during the rescue operation by the NDRF, local police and fire department.

Police is yet to reveal the names of the victims.

According to the Delhi Fire Department (DFS), a call about waterlogging was received from Rau's IAS Study Circle at around 7 p.m. on July 27 and that that there was a possibility that some people were trapped.

Police said it appeared that the basement got flooded very fast due to which some people were trapped inside.

A fire department official said that a total of five tenders were rushed to the site. The basement was full of water when they arrived.

Revenue Minister Atishi has directed Chief Secretary Naresh Kumar to initiate an inquiry and submit a report within 24 hours on the incident.

Visuals from Delhi’s Old Rajinder Nagar, where 3 students died in a coaching centre last night when the basement of the building was flooded following heavy rains. | Photo Credit: Shashi Shekhar Kashyap

"A magisterial inquiry has been ordered to investigate how this incident happened. Whoever is responsible for this incident will not be spared," Ms. Atishi posted on X on July 27.

Delhi BJP chief Virendra Sachdeva and New Delhi MP Bansuri Swaraj visited the site and blamed the AAP administration for the incident, saying the local MLA had ignored repeated appeals by locals to get the drains cleaned.

"Delhi Government's criminal negligence is responsible for this mishap. Jal Board Minister Atishi and local MLA Durgesh Pathak should take responsibility and resign," Mr. Sachdeva said.

Ms. Swaraj said that divers had to be called to rescue the students.

"For the past week, locals were urging AAP MLA Durgesh Pathak to get the drain here cleaned. However, Durgesh Pathak didn't listen to them. Arvind Kejriwal, Durgesh Pathak and the AAP government are entirely responsible for this incident," she said.

Preliminary investigation suggests that the basement housed a library where several students were present. Water suddenly started flooding the basement. Ropes were used to evacuate the trapped students, officials said.

The furniture in the coaching centre started floating when it was flooded and this created obstruction in the rescue operation, a police officer said.

Earlier this week, a 26-year-old civil services aspirant was electrocuted after he touched an iron gate following heavy rain in central Delhi's Patel Nagar area."""

summary = summarize_text(text)
print(summary)
