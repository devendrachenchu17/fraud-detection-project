from datetime import datetime

def preprocess_input(user_data):
    # Ensure 'datetime' key exists
    if 'datetime' not in user_data:
        raise ValueError("Datetime is missing from the input data")

    # Convert datetime to features
    try:
        dt = datetime.strptime(user_data['datetime'], '%Y-%m-%dT%H:%M')  # 'T' in datetime-local format
    except ValueError:
        raise ValueError("Datetime format is incorrect. Expected format: 'YYYY-MM-DDTHH:MM'")
    
    user_data['Year'] = dt.year
    user_data['Month'] = dt.month
    user_data['Day'] = dt.day
    user_data['Hour'] = dt.hour
    user_data['Minute'] = dt.minute
    user_data['Second'] = dt.second
    
    # Drop datetime
    user_data.pop('datetime')

    # Define the feature order
    feature_order = [
        'Transaction_Amount', 'Transaction_Type', 'Account_Balance', 'Device_Type', 'IP_Address_Flag', 
        'Previous_Fraudulent_Activity', 'Daily_Transaction_Count', 'Avg_Transaction_Amount_7d', 
        'Failed_Transaction_Count_7d', 'Card_Type', 'Transaction_Distance', 'Authentication_Method', 
        'Is_Weekend', 'Year', 'Month', 'Day', 'Hour', 'Minute', 'Second'
    ]
    
    # Ensure that all required fields are present in user_data
    processed_data = []
    for feature in feature_order:
        # Append feature or None if missing
        processed_data.append(user_data.get(feature, None))
    
    # Validate if any required feature is None
    if None in processed_data:
        raise ValueError("Some required features are missing or invalid.")
    
    return processed_data
