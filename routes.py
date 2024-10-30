# routes.py
from flask import request, jsonify
from app import app, db
from models import Patient
from services import stratify_risk

@app.route('/api/patient', methods=['POST'])
def add_patient():
    data = request.json
    if 'name' not in data or not data['name']:
        return jsonify({"error": "Patient name is required"}), 400
    if 'age' not in data or not (0 < data['age'] < 130):
        return jsonify({"error": "Valid age is required"}), 400
    if 'chronic_conditions' not in data or not data['chronic_conditions']:
        return jsonify({"error": "Chronic conditions are required"}), 400

    new_patient = Patient(
        name=data['name'],
        age=data['age'],
        gender=data.get('gender'),
        weight=data.get('weight'),
        height=data.get('height'),
        chronic_conditions=data['chronic_conditions'],
        medications=data.get('medications', ''),
        input_data=data['input_data']
    )
    db.session.add(new_patient)
    db.session.commit()
    return jsonify({"message": "Patient added successfully", "patient_id": new_patient.id}), 201

@app.route('/api/risk-stratification/<int:patient_id>', methods=['GET'])
def risk_stratification(patient_id):
    patient = Patient.query.get_or_404(patient_id)
    patient_data = {'age': patient.age}
    risk_score = stratify_risk(patient_data)
    patient.risk_score = risk_score[0]
    db.session.commit()
    return jsonify({"patient_id": patient_id, "risk_score": risk_score[0]}), 200
