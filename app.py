from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# Load the model and data
pipe = pickle.load(open('./models/model.pkl', 'rb'))
df = pickle.load(open('./models/data.pkl', 'rb'))

@app.route('/')
def index():
    # Sort the unique values for dropdowns
    protocol_type_sort = sorted(df['protocol_type'].unique())
    service_sort = sorted(df['service'].unique())
    flag_sort = sorted(df['flag'].unique())
    
    return render_template('index.html', protocol_type_sort=protocol_type_sort, service_sort=service_sort, flag_sort=flag_sort)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form inputs
        src_bytes = float(request.form['src_bytes'])
        dst_bytes = float(request.form['dst_bytes'])
        count = float(request.form['count'])
        same_srv_rate = float(request.form['same_srv_rate'])
        dst_host_srv_count = float(request.form['dst_host_srv_count'])
        dst_host_same_srv_rate = float(request.form['dst_host_same_srv_rate'])
        dst_host_same_src_port_rate = float(request.form['dst_host_same_src_port_rate'])
        
        protocol_type = request.form['protocol_type']
        service = request.form['service']
        flag = request.form['flag']
        
        # Create a dictionary of input values
        input_data = {
            'src_bytes': src_bytes,
            'dst_bytes': dst_bytes,
            'count': count,
            'same_srv_rate': same_srv_rate,
            'dst_host_srv_count': dst_host_srv_count,
            'dst_host_same_srv_rate': dst_host_same_srv_rate,
            'dst_host_same_src_port_rate': dst_host_same_src_port_rate,
            'protocol_type': protocol_type,
            'service': service,
            'flag': flag
        }

        # Convert to DataFrame
        input_df = pd.DataFrame([input_data])

        # Apply one-hot encoding to match training features
        input_encoded = pd.get_dummies(input_df)
        
        # Align columns with model input
        input_encoded = input_encoded.reindex(columns=pipe.feature_names_in_, fill_value=0)

        # Predict using the model
        prediction = pipe.predict(input_encoded)[0]
        
        # Fetch dropdown options again
        protocol_type_sort = sorted(df['protocol_type'].unique())
        service_sort = sorted(df['service'].unique())
        flag_sort = sorted(df['flag'].unique())
        
        return render_template(
            'index.html',
            prediction=prediction,
            protocol_type_sort=protocol_type_sort,
            service_sort=service_sort,
            flag_sort=flag_sort,
            protocol_type=protocol_type,
            service=service,
            flag=flag
        )
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
