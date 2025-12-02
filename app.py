# app.py - Python Flask Server

from flask import Flask, request, jsonify
from flask_cors import CORS # CORS zaroori hai

app = Flask(__name__)
# Sabhi endpoints ke liye CORS enable karein
CORS(app) 

# --- DUMMY DATABASE ---
MEMBER_RECORDS = []
DEPOSIT_RECORDS = []
LOAN_RECORDS = []


# ---------- API ENDPOINTS FOR FORMS ----------

@app.route('/submit_member', methods=['POST'])
def submit_member():
    data = request.json
    print("\n--- NEW MEMBER REGISTRATION RECEIVED ---")
    
    # Yahan rules check honge
    MEMBER_RECORDS.append(data)
    print("Received Data:", data)
    
    return jsonify({
        "status": "success",
        "message": f"Member '{data.get('name', 'New Member')}' ka data server par safaltapoorvak prapt hua."
    }), 200

@app.route('/submit_deposit', methods=['POST'])
def submit_deposit():
    data = request.json
    print("\n--- DEPOSIT RECEIVED ---")
    
    # Yahan late fee rule check hoga
    DEPOSIT_RECORDS.append(data)
    print("Received Data:", data)
    
    return jsonify({
        "status": "success",
        "message": f"Deposit ₹{data.get('amount')} for ID {data.get('member_id')} safaltapoorvak darj hua."
    }), 200

@app.route('/submit_loan', methods=['POST'])
def submit_loan():
    data = request.json
    print("\n--- LOAN APPLICATION RECEIVED ---")

    # Yahan eligibility aur interest calculation check hoga
    LOAN_RECORDS.append(data)
    print("Received Data:", data)
    
    return jsonify({
        "status": "success",
        "message": f"Loan application for ID {data.get('member_id')} server par darj hua aur approval ke liye bhej diya gaya."
    }), 200

@app.route('/deactivate_member', methods=['POST'])
def deactivate_member():
    data = request.json
    print("\n--- DEACTIVATION REQUEST RECEIVED ---")
    print("Deactivation Data:", data)
    return jsonify({
        "status": "success",
        "message": f"Member ID {data.get('member_id')} ko deactivate karne ki request safaltapoorvak darj hui."
    }), 200

if __name__ == '__main__':
    # Server 127.0.0.1:5000 par chalega
    print("\n*** FLASK SERVER STARTED ***")
    app.run(debug=True, host='0.0.0.0') 
