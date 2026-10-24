#!/usr/bin/env python3
"""
Webhook Fulfillment Service for Task 18: Dialogflow Chatbot with UiPath Integration
Implements Dialogflow ES webhook fulfillment API v2 and queries sample loan database.
"""

import json
import csv
import sys
from pathlib import Path
from http.server import HTTPServer, BaseHTTPRequestHandler

# Sample Loan Database
LOAN_DATABASE = {
    "8841": "Under Review",
    "8842": "Approved",
    "8843": "Rejected"
}

def get_loan_status_response(loan_id: str) -> dict:
    """
    Given a loan_id, formats the expected fulfillment message.
    """
    clean_id = str(loan_id).strip()
    status = LOAN_DATABASE.get(clean_id)
    
    if status == "Approved":
        msg = f"Your loan application {clean_id} has been approved."
    elif status == "Under Review":
        msg = f"Your loan application {clean_id} is currently under review."
    elif status == "Rejected":
        msg = f"Your loan application {clean_id} has been rejected."
    else:
        msg = f"Loan application {clean_id} was not found in the loan records. Please verify the application ID."

    return {
        "fulfillmentText": msg,
        "fulfillmentMessages": [
            {
                "text": {
                    "text": [msg]
                }
            }
        ],
        "outputContexts": [
            {
                "name": f"projects/loan-status-agent/agent/sessions/session-id/contexts/loan_verification_result",
                "lifespanCount": 2,
                "parameters": {
                    "loan_id": clean_id,
                    "application_status": status if status else "NotFound"
                }
            }
        ],
        "source": "UiPath-LoanStatus-RPA-Webhook"
    }

class DialogflowWebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        
        try:
            req_json = json.loads(post_data.decode('utf-8'))
            query_result = req_json.get('queryResult', {})
            params = query_result.get('parameters', {})
            loan_id = params.get('loan_id', '')
            
            # If loan_id is list or float/number
            if isinstance(loan_id, list) and loan_id:
                loan_id = loan_id[0]
            if isinstance(loan_id, (int, float)):
                loan_id = str(int(loan_id))
            
            resp_payload = get_loan_status_response(str(loan_id))
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(resp_payload, indent=2).encode('utf-8'))
        except Exception as e:
            self.send_response(400)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            err_resp = {"error": str(e), "fulfillmentText": "Error processing webhook."}
            self.wfile.write(json.dumps(err_resp).encode('utf-8'))

    def do_GET(self):
        # Health check
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        health = {
            "status": "healthy",
            "service": "UiPath Dialogflow Loan Status Webhook",
            "sample_records": LOAN_DATABASE
        }
        self.wfile.write(json.dumps(health, indent=2).encode('utf-8'))

def run_server(port: int = 5000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, DialogflowWebhookHandler)
    print(f"Loan Status Webhook Server running on port {port}...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down webhook server.")
        httpd.server_close()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        # Run local test
        print("Testing loan status responses:")
        for lid in ["8841", "8842", "8843", "9999"]:
            res = get_loan_status_response(lid)
            print(f"Loan {lid} -> {res['fulfillmentText']}")
    else:
        port = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 5000
        run_server(port)
