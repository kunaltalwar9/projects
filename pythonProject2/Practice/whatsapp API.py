
import json
import http.client


def handler(event):
    VERIFY_TOKEN = "Set_your_verify_token_value_here"
    WHATSAPP_TOKEN = "Paste_whatsapp_access_token_here"

    response = {}
    if event.get("requestContext", {}).get("http", {}).get("method") == "GET":
        queryParams = event.get("queryStringParameters")
        if queryParams is not None:
            mode = queryParams.get("hub.mode")
            if mode == "subscribe":
                verifyToken = queryParams.get("hub.verify_token")
                if verifyToken == VERIFY_TOKEN:
                    challenge = queryParams.get("hub.challenge")
                    response = {
                        "statusCode": 200,
                        "body": int(challenge),
                        "isBase64Encoded": False
                    }
                else:
                    responseBody = "Error, wrong validation token"
                    response = {
                        "statusCode": 403,
                        "body": json.dumps(responseBody),
                        "isBase64Encoded": False
                    }
            else:
                responseBody = "Error, wrong mode"
                response = {
                    "statusCode": 403,
                    "body": json.dumps(responseBody),
                    "isBase64Encoded": False
                }
        else:
            responseBody = "Error, no query parameters"
            response = {
                "statusCode": 403,
                "body": json.dumps(responseBody),
                "isBase64Encoded": False
            }
    elif event.get("requestContext", {}).get("http", {}).get("method") == "POST":
        body = json.loads(event["body"])
        entries = body.get("entry")
        for entry in entries:
            for change in entry.get("changes"):
                value = change.get("value")
                if value is not None:
                    phone_number_id = value.get("metadata").get("phone_number_id")
                    if value.get("messages") is not None:
                        for message in value.get("messages"):
                            if message.get("type") == 'text':
                                from_num = message.get("from")
                                message_body = message.get("text").get("body")
                                reply_message = "Ack from AWS lambda: " + message_body
                                sendReply(phone_number_id, WHATSAPP_TOKEN, from_num, reply_message)
                                responseBody = "Done"
                                response = {
                                    "statusCode": 200,
                                    "body": json.dumps(responseBody),
                                    "isBase64Encoded": False
                                }
    else:
        responseBody = "Unsupported method"
        response = {
            "statusCode": 403,
            "body": json.dumps(responseBody),
            "isBase64Encoded": False
        }

    return response


def sendReply(phone_number_id, whatsapp_token, to, reply_message):
    json_data = {
        "messaging_product": "whatsapp",
        "to": to,
        "text": {"body": reply_message}
    }
    data = json.dumps(json_data)
    path = "/v12.0/" + phone_number_id + "/messages?access_token=" + whatsapp_token
    conn = http.client.HTTPSConnection("graph.facebook.com")
    headers = {"Content-Type": "application/json"}
    conn.request("POST", path, data, headers)
    response = conn.getresponse()
    # Handle response as needed
    conn.close()