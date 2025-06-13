import requests
import json

def analyse(text_to_analyse):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    header = {
        "grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"
    }
    myobj = { 
        "raw_document": { 
            "text": text_to_analyse 
        } 
    }
    response = requests.post(url, json = myobj, headers=header)
    response_text = json.loads(response.text)

    if response.status_code == 200:
        output = {
            'score': response_text['documentSentiment']['score'],
            'label': response_text['documentSentiment']['label']
        }
    else:
        output = {
            'score': None,
            'label': None
        }
    return output


def main():
    print(analyse("I'd like to go to the wilderness, and never come back!"))

if __name__ == "__main__":
    main()